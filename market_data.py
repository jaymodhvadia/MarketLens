import yfinance as yf
import pandas as pd

ftse = yf.download("^FTSE", period="1y", interval="1d")

ftse = ftse.reset_index()

ftse.to_csv("ftse100_history.csv", index=False)

print("FTSE 100 historical data downloaded!")
print("Number of trading days:", len(ftse))