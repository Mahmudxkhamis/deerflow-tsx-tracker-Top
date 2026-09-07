import pandas as pd
import yfinance as yf
from datetime import datetime

# Load tickers from Excel file
tickers = pd.read_excel("Toronto Stock Exchange Tickers.xlsx")["Symbol"].tolist()

results = []
for symbol in tickers:
    try:
        data = yf.Ticker(symbol).history(period="1d")
        price = data["Close"].iloc[-1]
        results.append({
            "Symbol": symbol,
            "Price": price,
            "Date": datetime.now().strftime("%Y-%m-%d")
        })
    except Exception as e:
        print(f"Error fetching {symbol}: {e}")

df = pd.DataFrame(results)
df.to_csv("tsx_prices.csv", index=False)
print("Tracking complete — data saved to tsx_prices.csv")
