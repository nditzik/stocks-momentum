# Momentum Scanner Dashboard

A multi-signal stock analysis dashboard built on Barchart data.

## Key Features

### Signals
The dashboard analyzes 5 signals from Barchart CSV files:
- **Strength+Direction** — Stocks with strong trend momentum and positive direction
- **6M High** — Stocks approaching their 6-month high
- **TTM Squeeze** — Stocks in technical squeeze before a breakout
- **MACD Buy** — MACD buy signal triggered
- **Hot Prospects** — Stocks with strong technical support

### Tabs
| Tab | Description |
|-----|-------------|
| All Stocks | All stocks passing the base filter |
| Watchlist | Stocks marked as ⭐ favorites |
| Smart Track | Pre-entry stocks (🎯 MA Bounce / 🌀 Coiled / ⚡ New Entry / 📊 Consistent) |
| Signal Scanner | Advanced search by signals, RSI, BB%, moving averages, sentiment |

### Base Filters
A stock must meet all of the following to appear in the dashboard:
- Average volume (200-day) above 750K
- Positive Weighted Alpha
- MA20 available
- RSI available
- Price available

### Chart
Clicking a stock opens a candlestick chart with MA20/50/150, Bollinger Bands, RSI, Stochastic and MACD.

### Export
- Export watchlists to ThinkorSwim (TOS)
- Export to CSV
- Export/import favorites as JSON

## Usage

1. Download CSV files from Barchart into the `data/` folder
2. The dashboard auto-loads the most recent files
3. Required filename format: `ttm-squeeze-triggered-MM-DD-YYYY.csv`

### Required Files
```
data/stocks-screener-strength-and-direction-MM-DD-YYYY.csv
data/stocks-screener-nearing-6-month-highs-MM-DD-YYYY.csv
data/ttm-squeeze-triggered-MM-DD-YYYY.csv
data/12-26-9-day-emacd-new-buy-signals-MM-DD-YYYY.csv
data/stocks-screener-hot-prospects-MM-DD-YYYY.csv
```

## Tech Stack
- Pure HTML/CSS/JavaScript — no external dependencies
- Data: Barchart.com
- Live prices: Yahoo Finance API

---

# Momentum Scanner Dashboard — עברית

דשבורד לניתוח מניות מבוסס מולטי-סיגנל, בנוי על נתוני Barchart.

## תכונות עיקריות

### סיגנלים
הדשבורד מנתח 5 סיגנלים מתוך קבצי CSV מ-Barchart:
- **Strength+Direction** — מניות עם חוזק מגמה גבוה וכיוון חיובי
- **6M High** — מניות הקרובות לשיא 6 חודשים
- **TTM Squeeze** — מניות בסחיטה טכנית לפני פריצה
- **MACD Buy** — איתות קנייה ב-MACD
- **Hot Prospects** — מניות עם תמיכה טכנית חזקה

### טאבים
| טאב | תיאור |
|-----|--------|
| כל המניות | כל המניות שעברו את הפילטר הבסיסי |
| מועדפים | מניות שסימנת כ-⭐ |
| מעקב חכם | מניות לפני נקודת כניסה (🎯 MA Bounce / 🌀 Coiled / ⚡ New Entry / 📊 Consistent) |
| סורק סיגנלים | חיפוש מתקדם לפי סיגנלים, RSI, BB%, ממוצעים נעים, סנטימנט |

### פילטרים בסיסיים
מניה חייבת לעמוד בכל התנאים הבאים להופיע בדשבורד:
- ווליום ממוצע (200 יום) מעל 750K
- Weighted Alpha חיובי
- MA20 קיים
- RSI קיים
- מחיר קיים

### גרף
לחיצה על מניה פותחת גרף נרות עם MA20/50/150, Bollinger Bands, RSI, Stochastic ו-MACD.

### ייצוא
- ייצוא רשימות ל-ThinkorSwim (TOS)
- ייצוא ל-CSV
- ייצוא/ייבוא מועדפים כ-JSON

## שימוש

1. הורד את הקבצים מ-Barchart לתיקיית `data/`
2. הדשבורד טוען אוטומטית את הקבצים העדכניים ביותר
3. פורמט שם קובץ נדרש: `ttm-squeeze-triggered-MM-DD-YYYY.csv`

### קבצים נדרשים
```
data/stocks-screener-strength-and-direction-MM-DD-YYYY.csv
data/stocks-screener-nearing-6-month-highs-MM-DD-YYYY.csv
data/ttm-squeeze-triggered-MM-DD-YYYY.csv
data/12-26-9-day-emacd-new-buy-signals-MM-DD-YYYY.csv
data/stocks-screener-hot-prospects-MM-DD-YYYY.csv
```

## טכנולוגיות
- HTML/CSS/JavaScript — ללא dependencies חיצוניים
- נתונים: Barchart.com
- מחירים חיים: Yahoo Finance API
