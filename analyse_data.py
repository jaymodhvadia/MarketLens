import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

data = pd.read_csv("ftse100_history.csv")

# Convert columns to numbers
data["Close"] = pd.to_numeric(data["Close"], errors="coerce")
data["High"] = pd.to_numeric(data["High"], errors="coerce")
data["Low"] = pd.to_numeric(data["Low"], errors="coerce")

# Convert dates
data["Date"] = pd.to_datetime(data["Date"])

# Remove rows with missing values
data = data.dropna(subset=["Close", "High", "Low"])

# Calculate daily percentage returns
data["daily_return"] = data["Close"].pct_change() * 100

# Calculate volatility
volatility = data["daily_return"].std()

# Calculate 30-day moving average
data["30_day_average"] = data["Close"].rolling(window=30).mean()

# Latest values
latest_close = data["Close"].iloc[-1]
latest_average = data["30_day_average"].iloc[-1]

# Overall percentage change
first_close = data["Close"].iloc[0]
percentage_change = ((latest_close - first_close) / first_close) * 100

# Trend signal
if latest_close > latest_average:
    signal = "Positive trend"
else:
    signal = "Negative trend"

# Risk level
if volatility < 1:
    risk_level = "Low"
elif volatility < 2:
    risk_level = "Moderate"
else:
    risk_level = "High"

# Best and worst trading days
best_day = data.loc[data["daily_return"].idxmax()]
worst_day = data.loc[data["daily_return"].idxmin()]

# Print summary
print()
print("=" * 45)
print("          FTSE 100 MARKET ANALYSIS")
print("=" * 45)

print("Trading days analysed:", len(data))
print("Average closing value:", round(data["Close"].mean(), 2))
print("Highest value:", round(data["High"].max(), 2))
print("Lowest value:", round(data["Low"].min(), 2))
print("Overall change:", round(percentage_change, 2), "%")
print("Daily volatility:", round(volatility, 2), "%")

print()
print("Latest FTSE 100:", round(latest_close, 2))
print("30-Day Moving Average:", round(latest_average, 2))
print("Trend Signal:", signal)
print("Risk Level:", risk_level)

print()
print("Best trading day:")
print(
    best_day["Date"].strftime("%d %B %Y"),
    round(best_day["daily_return"], 2),
    "%"
)

print("Worst trading day:")
print(
    worst_day["Date"].strftime("%d %B %Y"),
    round(worst_day["daily_return"], 2),
    "%"
)

print("=" * 45)

# Create graph
plt.figure(figsize=(12, 6))

plt.plot(
    data["Date"],
    data["Close"],
    label="FTSE 100"
)

plt.plot(
    data["Date"],
    data["30_day_average"],
    label="30-Day Moving Average"
)

plt.title("FTSE 100 vs 30-Day Moving Average")
plt.xlabel("Date")
plt.ylabel("FTSE 100 Value")

plt.legend()

# Format x-axis
plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
plt.gca().xaxis.set_major_formatter(
    mdates.DateFormatter("%b %Y")
)

plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()

plt.show()

# Compare FTSE 100 with GBP/USD

gbp_data = pd.read_csv("gbpusd_history.csv")

gbp_data["Date"] = pd.to_datetime(gbp_data["Date"], utc=True).dt.date
data["Date"] = pd.to_datetime(data["Date"], utc=True).dt.date

# Rename GBP/USD column
gbp_data = gbp_data.rename(columns={"Close": "GBPUSD"})

# Merge the two datasets using their dates
combined = pd.merge(
    data[["Date", "Close"]],
    gbp_data[["Date", "GBPUSD"]],
    on="Date",
    how="inner"
)

# Calculate correlation
correlation = combined["Close"].corr(combined["GBPUSD"])

print()
print("FTSE 100 vs GBP/USD")
print("Trading days compared:", len(combined))
print("Correlation:", round(correlation, 2))

if correlation > 0.5:
    print("Relationship: Strong positive relationship")
elif correlation > 0:
    print("Relationship: Weak positive relationship")
elif correlation > -0.5:
    print("Relationship: Weak negative relationship")
else:
    print("Relationship: Strong negative relationship")

    # Scatter plot showing the relationship

plt.figure(figsize=(10, 6))

plt.scatter(
    combined["GBPUSD"],
    combined["Close"],
    alpha=0.6
)

plt.title("FTSE 100 vs GBP/USD")
plt.xlabel("GBP/USD Exchange Rate")
plt.ylabel("FTSE 100 Closing Value")

plt.grid(True)
plt.tight_layout()

plt.show()

# Compare FTSE 100 with Bitcoin

bitcoin_data = pd.read_csv("bitcoin_history.csv")

bitcoin_data["Date"] = pd.to_datetime(
    bitcoin_data["Date"], utc=True
).dt.date

bitcoin_data = bitcoin_data.rename(
    columns={"Close": "Bitcoin"}
)

ftse_bitcoin = pd.merge(
    data[["Date", "Close"]],
    bitcoin_data[["Date", "Bitcoin"]],
    on="Date",
    how="inner"
)

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

    # Compare daily percentage returns

ftse_bitcoin["FTSE_Return"] = ftse_bitcoin["Close"].pct_change() * 100
ftse_bitcoin["Bitcoin_Return"] = ftse_bitcoin["Bitcoin"].pct_change() * 100

# Remove the first row because it has no previous day
returns_data = ftse_bitcoin.dropna()

return_correlation = returns_data["FTSE_Return"].corr(
    returns_data["Bitcoin_Return"]
)

print()
print("FTSE 100 vs Bitcoin - Daily Returns")
print("Trading days compared:", len(returns_data))
print("Return correlation:", round(return_correlation, 2))

if return_correlation > 0.5:
    print("Relationship: Strong positive relationship")
elif return_correlation > 0:
    print("Relationship: Weak positive relationship")
elif return_correlation > -0.5:
    print("Relationship: Weak negative relationship")
else:
    print("Relationship: Strong negative relationship")

# Scatter plot of daily returns

plt.figure(figsize=(10, 6))

plt.scatter(
    returns_data["Bitcoin_Return"],
    returns_data["FTSE_Return"],
    alpha=0.6
)

plt.title("Daily Returns: Bitcoin vs FTSE 100")
plt.xlabel("Bitcoin Daily Return (%)")
plt.ylabel("FTSE 100 Daily Return (%)")

plt.axhline(0, linewidth=0.8)
plt.axvline(0, linewidth=0.8)

plt.grid(True)
plt.tight_layout()

plt.show()

# FTSE 100 Risk Analysis

ftse_returns = data["Close"].pct_change().dropna() * 100

average_return = ftse_returns.mean()
best_return = ftse_returns.max()
worst_return = ftse_returns.min()

# Annualised volatility
annualised_volatility = ftse_returns.std() * (252 ** 0.5)

print()
print("FTSE 100 RISK ANALYSIS")
print("Average daily return:", round(average_return, 2), "%")
print("Best daily return:", round(best_return, 2), "%")
print("Worst daily return:", round(worst_return, 2), "%")
print("Annualised volatility:", round(annualised_volatility, 2), "%")

# FTSE 100 Sharpe Ratio

annual_return = ftse_returns.mean() * 252
risk_free_rate = 4.0

sharpe_ratio = (
    (annual_return - risk_free_rate)
    / annualised_volatility
)

print()
print("FTSE 100 PERFORMANCE")
print("Estimated annual return:", round(annual_return, 2), "%")
print("Assumed risk-free rate:", risk_free_rate, "%")
print("Sharpe ratio:", round(sharpe_ratio, 2))

# FTSE 100 Maximum Drawdown

data["Running_Max"] = data["Close"].cummax()

data["Drawdown"] = (
    (data["Close"] - data["Running_Max"])
    / data["Running_Max"]
) * 100

maximum_drawdown = data["Drawdown"].min()

print()
print("FTSE 100 DRAWDOWN ANALYSIS")
print("Maximum drawdown:", round(maximum_drawdown, 2), "%")