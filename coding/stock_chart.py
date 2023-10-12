# filename: stock_chart.py
import matplotlib.pyplot as plt
from alpha_vantage.timeseries import TimeSeries

# Define your Alpha Vantage API key
api_key = "YOUR_API_KEY"

# Define the list of stock tickers
tickers = ["NVDA", "AAPL", "TSLA"]

# Instantiate the TimeSeries object
ts = TimeSeries(key=api_key, output_format="pandas")

# Fetch the stock price data for the tickers
data = {}
for ticker in tickers:
    ticker_data, _ = ts.get_daily_adjusted(symbol=ticker, outputsize="full")
    data[ticker] = ticker_data["5. adjusted close"]

# Merge the stock price data into a single DataFrame
df = pd.concat(data, axis=1)

# Plot the stock price change YTD
df.plot(figsize=(10, 6))
plt.xlabel("Date")
plt.ylabel("Price")
plt.title("Stock Price Change YTD")
plt.legend(tickers)
plt.grid(True)

# Display the chart
plt.show()