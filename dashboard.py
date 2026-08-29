import pandas as pd
import matplotlib.pyplot as plt

# Load FTSE data
data = pd.read_csv("ftse100_history.csv")

data["Date"] = pd.to_datetime(data["Date"])
data["Close"] = pd.to_numeric(data["Close"], errors="coerce")

data = data.dropna(subset=["Close"])

# Calculate moving average
data["Moving_Average"] = data["Close"].rolling(30).mean()

# Calculate daily returns
data["Daily_Return"] = data["Close"].pct_change() * 100

# Create dashboard
fig = plt.figure(figsize=(14, 9))

fig.suptitle(
    "FTSE 100 MARKET DASHBOARD",
    fontsize=20,
    fontweight="bold"
)

# Main price chart
ax1 = plt.subplot(2, 1, 1)

ax1.plot(
    data["Date"],
    data["Close"],
    label="FTSE 100"
)

ax1.plot(
    data["Date"],
    data["Moving_Average"],
    label="30-Day Moving Average"
)

ax1.set_title("FTSE 100 Closing Value")
ax1.set_ylabel("Index Value")
ax1.legend()
ax1.grid(True)

# Daily returns chart
ax2 = plt.subplot(2, 1, 2)

ax2.plot(
    data["Date"],
    data["Daily_Return"],
    label="Daily Return"
)

ax2.axhline(0, linewidth=0.8)

ax2.set_title("Daily Percentage Returns")
ax2.set_ylabel("Return (%)")
ax2.set_xlabel("Date")
ax2.legend()
ax2.grid(True)

plt.tight_layout()

plt.savefig("ftse100_dashboard.png", dpi=300, bbox_inches="tight")

print("Dashboard saved as ftse100_dashboard.png")

plt.show()