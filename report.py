import pandas as pd

# Load FTSE data
data = pd.read_csv("ftse100_history.csv")

data["Date"] = pd.to_datetime(data["Date"])
data["Close"] = pd.to_numeric(data["Close"], errors="coerce")

data = data.dropna(subset=["Close"])

# Basic statistics
average = data["Close"].mean()
highest = data["Close"].max()
lowest = data["Close"].min()

first = data["Close"].iloc[0]
latest = data["Close"].iloc[-1]

overall_change = ((latest - first) / first) * 100

# Daily returns
returns = data["Close"].pct_change().dropna() * 100

daily_volatility = returns.std()

# Annualised volatility
annualised_volatility = daily_volatility * (252 ** 0.5)

# Moving average
moving_average = data["Close"].tail(30).mean()

# Trend
if latest > moving_average:
    trend = "Positive"
else:
    trend = "Negative"

# Maximum drawdown
data["Running_Max"] = data["Close"].cummax()

data["Drawdown"] = (
    (data["Close"] - data["Running_Max"])
    / data["Running_Max"]
) * 100

maximum_drawdown = data["Drawdown"].min()

# Sharpe ratio
annual_return = returns.mean() * 252
risk_free_rate = 4.0

sharpe_ratio = (
    (annual_return - risk_free_rate)
    / annualised_volatility
)

# Print report
print()
print("=" * 50)
print("       FTSE 100 INVESTMENT REPORT")
print("=" * 50)

print("Trading days:", len(data))
print("Average closing value:", round(average, 2))
print("Highest value:", round(highest, 2))
print("Lowest value:", round(lowest, 2))

print()
print("Overall change:", round(overall_change, 2), "%")
print("Average daily return:", round(returns.mean(), 2), "%")
print("Annualised volatility:", round(annualised_volatility, 2), "%")

print()
print("Latest FTSE 100:", round(latest, 2))
print("30-day moving average:", round(moving_average, 2))
print("Trend:", trend)

print()
print("Maximum drawdown:", round(maximum_drawdown, 2), "%")
print("Sharpe ratio:", round(sharpe_ratio, 2))

print("=" * 50)

# Investment interpretation

print()
print("INVESTMENT INTERPRETATION")
print("---------------------------------------------")

if trend == "Positive":
    print("The FTSE 100 is currently above its 30-day moving average,")
    print("indicating positive short-term momentum.")
else:
    print("The FTSE 100 is currently below its 30-day moving average,")
    print("indicating negative short-term momentum.")

if annualised_volatility < 15:
    print("Volatility is relatively moderate.")
elif annualised_volatility < 25:
    print("Volatility is relatively high.")
else:
    print("Volatility is very high.")

if sharpe_ratio > 1:
    print("The Sharpe ratio indicates a favourable return relative to risk.")
elif sharpe_ratio > 0:
    print("The Sharpe ratio indicates a positive return relative to risk.")
else:
    print("The Sharpe ratio indicates an unfavourable return relative to risk.")

print("Maximum drawdown shows the largest decline from a previous peak was",
      round(abs(maximum_drawdown), 2), "%.")