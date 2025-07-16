import yfinance as yf
import pandas as pd

# Download historical data for Tata Motors (NSE)
df = yf.download("TATAMOTORS.NS", start="2015-01-01", end="2024-12-31")
df.to_csv("TATAMOTORS.csv")
print("✅ Data saved as TATAMOTORS.csv")