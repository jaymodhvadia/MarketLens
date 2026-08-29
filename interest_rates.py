import yfinance as yf
import pandas as pd

# Download GBP/USD data
gbp = yf.Ticker("GBPUSD=X")

data = gbp.history(period="1y")

# Keep only the useful columns
data = data[["Close"]]

# Remove missing values
data = data.dropna()

# Save the cleaned data
data.to_csv("gbpusd_history.csv")

# Display information
print("GBP/USD data prepared!")
print("Trading days:", len(data))
print("Latest GBP/USD:", round(data["Close"].iloc[-1], 4))
print()
print(data.head())