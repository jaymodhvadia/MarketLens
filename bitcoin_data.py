import yfinance as yf
import pandas as pd

bitcoin = yf.Ticker("BTC-USD")

data = bitcoin.history(period="1y")

data = data[["Close"]]

data = data.reset_index()

data = data.dropna()

data.to_csv("bitcoin_history.csv", index=False)

print("Bitcoin data prepared!")
print("Trading days:", len(data))
print("Latest Bitcoin price:", round(data["Close"].iloc[-1], 2))
print()
print(data.head())

# Compare FTSE 100 with Bitcoin

bitcoin_data = pd.read_csv("bitcoin_history.csv")

# Convert dates to the same format
bitcoin_data["Date"] = pd.to_datetime(
    bitcoin_data["Date"], utc=True
).dt.date

# Convert FTSE data
ftse_data = pd.read_csv("ftse100_history.csv")

ftse_data["Date"] = pd.to_datetime(
    ftse_data["Date"], utc=True
).dt.date

# Rename Bitcoin column
bitcoin_data = bitcoin_data.rename(
    columns={"Close": "Bitcoin"}
)

# Combine FTSE and Bitcoin data
ftse_bitcoin = pd.merge(
    ftse_data[["Date", "Close"]],
    bitcoin_data[["Date", "Bitcoin"]],
    on="Date",
    how="inner"
)

# Calculate correlation
bitcoin_correlation = ftse_bitcoin["Close"].corr(
    ftse_bitcoin["Bitcoin"]
)

print()
print("FTSE 100 vs Bitcoin")
print("Trading days compared:", len(ftse_bitcoin))
print("Correlation:", round(bitcoin_correlation, 2))

if bitcoin_correlation > 0.5:
    print("Relationship: Strong positive relationship")
elif bitcoin_correlation > 0:
    print("Relationship: Weak positive relationship")
elif bitcoin_correlation > -0.5:
    print("Relationship: Weak negative relationship")
else:
    print("Relationship: Strong negative relationship")