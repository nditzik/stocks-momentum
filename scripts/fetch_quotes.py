"""Fetches delayed quotes from Yahoo Finance for every symbol present in the
latest Barchart CSVs and writes data/quotes.json. Designed to run from a
GitHub Action every 15 minutes during US market hours."""

import csv
import glob
import json
import os
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone

import requests

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data")
OUT_PATH = os.path.join(DATA_DIR, "quotes.json")

YAHOO_URL = "https://query1.finance.yahoo.com/v8/finance/chart/{sym}?range=1d&interval=1d"
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    )
}


def collect_symbols() -> list[str]:
    """Read every CSV in data/ and union the Symbol column."""
    symbols: set[str] = set()
    for path in glob.glob(os.path.join(DATA_DIR, "*.csv")):
        try:
            with open(path, newline="", encoding="utf-8") as fh:
                reader = csv.reader(fh)
                header = next(reader, None)
                if not header or header[0].lower() != "symbol":
                    continue
                for row in reader:
                    if not row:
                        continue
                    sym = row[0].strip().strip('"').upper()
                    # Skip footer rows like "Downloaded from Barchart..."
                    if not sym or len(sym) > 10 or " " in sym:
                        continue
                    symbols.add(sym)
        except Exception as exc:
            print(f"[warn] {path}: {exc}", file=sys.stderr)
    return sorted(symbols)


def fetch_one(sym: str, session: requests.Session) -> tuple[str, dict | None]:
    try:
        r = session.get(YAHOO_URL.format(sym=sym), timeout=10)
        if r.status_code != 200:
            return sym, None
        meta = r.json()["chart"]["result"][0]["meta"]
        price = meta.get("regularMarketPrice")
        prev = meta.get("chartPreviousClose") or meta.get("previousClose")
        if price is None or not prev:
            return sym, None
        change_pct = ((price - prev) / prev) * 100.0
        return sym, {
            "price": round(float(price), 4),
            "prev_close": round(float(prev), 4),
            "change_pct": round(change_pct, 3),
            "time": int(meta.get("regularMarketTime") or 0),
            "state": meta.get("marketState", "UNKNOWN"),
        }
    except Exception:
        return sym, None


def main() -> int:
    symbols = collect_symbols()
    if not symbols:
        print("[error] no symbols found in data/*.csv", file=sys.stderr)
        return 1
    print(f"[info] fetching {len(symbols)} symbols")

    session = requests.Session()
    session.headers.update(HEADERS)

    quotes: dict[str, dict] = {}
    market_state = "UNKNOWN"
    t0 = time.time()
    with ThreadPoolExecutor(max_workers=16) as pool:
        futures = [pool.submit(fetch_one, s, session) for s in symbols]
        for fut in as_completed(futures):
            sym, q = fut.result()
            if q is not None:
                quotes[sym] = q
                if market_state in ("UNKNOWN", "CLOSED") and q["state"] in ("PRE", "REGULAR", "POST"):
                    market_state = q["state"]

    elapsed = time.time() - t0
    print(f"[info] got {len(quotes)}/{len(symbols)} quotes in {elapsed:.1f}s — state={market_state}")

    payload = {
        "fetched_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "market_state": market_state,
        "symbol_count": len(quotes),
        "quotes": quotes,
    }

    os.makedirs(DATA_DIR, exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as fh:
        json.dump(payload, fh, separators=(",", ":"))
    print(f"[info] wrote {OUT_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
