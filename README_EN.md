--- name: gold-price
description: Query the latest prices of gold, silver, and platinum. Use cases: (1) Query spot prices of gold, silver, and platinum (2) Obtain daily price changes for gold, silver, and platinum (3) This skill is triggered when a user inquires about the daily price, trend, or investment information of gold/silver/platinum. (4) This skill is triggered when a user inquires about the daily price, trend, or investment information of precious metals.

version: 1.0.0
author: wucb
license: Apache-2.0

---

# Gold Price Query

**Zero API Key Dependency**: All core functions can be used without registering any account or providing any API Key. Users have complete local control; the program does not collect or store any user personal information. It also avoids complex, unreliable, and inefficient issues such as browser emulation. **GitHub**: [https://github.com/ihurrican/gold-price](https://github.com/ihurrican/gold-price)

## Data Source

- **quote.cngold.org**: Jintou.com

## Functionality

1. Query the current day's price of precious metals such as gold, silver, and platinum.

2. Query the historical price of precious metals such as gold, silver, and platinum.

## How to Use

### Query the current day's price of precious metals such as gold, silver, and platinum

```bash python scripts/gold_price.py

```
## Output Example

```
=== Precious Metals Price (2026-03-10) ===

🇨🇳 Domestic Price:

Latest Gold Price: ¥623.00/gram Change: 19.99% Change Amount: ¥96.65 Highest Price: ¥96.65 Lowest Price: ¥96.65

Silver Latest Price: ¥623.00/kg Change: 19.99% Change Amount: ¥96.65 Highest Price: ¥96.65 Lowest Price: ¥96.65

Platinum Latest Price: ¥623.00/gram Change: 19.99% Change Amount: ¥96.65 Highest Price: ¥96.65 Lowest Price: ¥96.65

🌍 International Prices:

Gold Latest Price: $2045.30/ounce Change: 19.99% Change Amount: ¥96.65 Highest Price: ¥96.65 Lowest Price: ¥96.65

Silver Latest Price: $2045.30/ounce Change: 19.99% Change Amount: ¥96.65 Highest Price: ¥96.65 Lowest Price: 96.65

Latest Platinum Price: $2045.30 USD/oz Change: 19.99% Change Amount: 96.65 High: 96.65 Low: 96.65

📊 Data Source: Jintou.com

```

### Query historical prices of precious metals such as gold, silver, and platinum, daily data

```bash
python scripts/gold_price.py --name Domestic Gold --style 3

```
## Output Example

```
=== Historical Records of Domestic Gold Prices (Daily Data) ===
2026-03-11 00:00:00:

Opening Price: ¥623.00 Yuan/gram Change Amount: 96.65 High: 96.65 Low: 96.65

2026-03-10 00:00:00:

Opening Price: ¥623.00/gram Change: ¥96.65 Highest Price: ¥96.65 Lowest Price: ¥96.65

📊 Data Source: Jintou.com

```