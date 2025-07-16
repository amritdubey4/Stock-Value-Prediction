import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("TATAMOTORS.csv", index_col=0, parse_dates=True)

# Plot close price
plt.figure(figsize=(14,6))
plt.plot(df['Close'], label='Tata Motors Closing Price')
plt.title("Tata Motors Stock Price (Close)")
plt.xlabel("Date")
plt.ylabel("Price (INR)")
plt.legend()
plt.grid(True)
plt.show()