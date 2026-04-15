# Momentum Scanner Dashboard

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
