import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

# Step 1: Look for historical stock data from the yfinance library
def fetch_stock_data(ticker, start_date, end_date):
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    return stock_data["Adj Close"]

# Step 2: Calculate daily returns and estimate parameters
def calculate_returns_and_parameters(stock_prices):
    returns = stock_prices.pct_change().dropna()

    # 2.1 Use exponentially weighted moving average for volatility
    volatility = returns.ewm(span=30, adjust=False).std().iloc[-1]
    mean_daily_return = returns.mean()

    # 2.2 Calculate average daily return
    drift = mean_daily_return - 0.5 * volatility ** 2

    return returns, mean_daily_return, volatility, drift

# Step 3: Define a random input or variable
def generate_random_input(num_simulations, num_days, volatility, drift, last_price):
    dt = 1 / 252  # assuming 252 trading days in a year
    random_input = np.random.normal(0, 1, size=(num_simulations, num_days))

    # 3.1 Calculate random returns
    random_returns = drift * dt + volatility * np.sqrt(dt) * random_input.T

    # 3.2 Calculate simulated prices
    simulated_prices = last_price * np.exp(np.cumsum(random_returns, axis=0))

    return simulated_prices

# Step 4: Run the simulation
def monte_carlo_simulation(ticker, start_date, end_date, num_simulations, num_days):

    # 4.1: Fetch historical stock data
    stock_prices = fetch_stock_data(ticker, start_date, end_date)

    # 4.2: Calculate returns and estimate parameters
    returns, mean_daily_return, volatility, drift = calculate_returns_and_parameters(stock_prices)

    # 4.3: Define a random input or variable
    last_price = stock_prices.iloc[-1]
    simulated_prices = generate_random_input(num_simulations, num_days, volatility, drift, last_price)

    return simulated_prices, mean_daily_return, volatility

# Parameters that you can play with it :)
ticker = "NVDA" # Stock ticker symbol
start_date = "2020-01-01"  # Start date for historical data
end_date = "2024-02-02"  # End date for historical data
num_simulations = 150 # Number of simulations; for reference 50k takes around 20 seconds to create both images
# (first one almost crashed) CPU i9-12900H, and the .csv is 132MB. Do with this info what you please.
num_days = 100  # Number of days you want to run these simulations through

# Run Monte Carlo simulation
simulated_prices, mean_daily_return, volatility = monte_carlo_simulation(ticker, start_date, end_date, num_simulations, num_days)

# Save simulated prices and days to a .csv file
simulation_data = pd.DataFrame({
    "Simulation": np.arange(1, num_days + 1),
    "Mean_Price": simulated_prices.mean(axis=1),
    "5th_Percentile": np.percentile(simulated_prices, 5, axis=1),
    "95th_Percentile": np.percentile(simulated_prices, 95, axis=1)
})

# Add simulated prices for each day
simulation_data = pd.concat([simulation_data, pd.DataFrame(simulated_prices.T, columns=[f"Day_{i+1}" for i in range(num_days)])], axis=1)
# Save to .csv on the desktop
desktop_path = os.path.join(os.path.join(os.path.expanduser("~")), "Desktop")
csv_file_path = os.path.join(desktop_path, "monte_carlo_simulation_results.csv")
simulation_data.to_csv(csv_file_path, index=False, float_format="%.6f")

# Display simulation results using pandas
pd.set_option("display.max_rows", None)  # To display all rows in the DataFrame
print("Simulation Results:")
print(simulation_data)

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(simulated_prices)
plt.title(f"Monte Carlo Simulation - {ticker} Stock Price Scenarios")
plt.xlabel("Days")
plt.ylabel("Stock Price")
plt.show()

# Plot the results with confidence intervals (5th percentile, 95th percentile)
plt.figure(figsize=(10, 6))
plt.plot(simulated_prices, color="gray", alpha=0.1)
plt.plot(np.percentile(simulated_prices, 5, axis=1), label="5th Percentile", linestyle="dashed", color="red")
plt.plot(np.percentile(simulated_prices, 95, axis=1), label="95th Percentile", linestyle="dashed", color="blue")
plt.title(f"Monte Carlo Simulation - {ticker} Stock Price Scenarios with Confidence Intervals")
plt.xlabel("Days")
plt.ylabel("Stock Price")
plt.legend()
plt.show()

# Display estimated parameters
print(f"Mean Daily Return: {mean_daily_return:.6f}")
print(f"Volatility: {volatility:.6f}")

