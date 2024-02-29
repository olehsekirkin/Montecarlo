import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

def fetch_stock_data(ticker, start_date, end_date):
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    return stock_data["Adj Close"]

def calculate_returns_and_parameters(stock_prices):
    returns = stock_prices.pct_change().dropna()
   
    volatility = returns.ewm(span=30, adjust=False).std().iloc[-1]
    mean_daily_return = returns.mean()
    
    drift = mean_daily_return - 0.5 * volatility ** 2

    return returns, mean_daily_return, volatility, drift

def generate_random_input(num_simulations, num_days, volatility, drift, last_price):
    dt = 1 / 252  # assuming 252 trading days in a year
    random_input = np.random.normal(0, 1, size=(num_simulations, num_days))

    random_returns = drift * dt + volatility * np.sqrt(dt) * random_input.T

    simulated_prices = last_price * np.exp(np.cumsum(random_returns, axis=0))

    return simulated_prices

def monte_carlo_simulation(ticker, start_date, end_date, num_simulations, num_days):

    stock_prices = fetch_stock_data(ticker, start_date, end_date)
    
    returns, mean_daily_return, volatility, drift = calculate_returns_and_parameters(stock_prices)

    last_price = stock_prices.iloc[-1]
    simulated_prices = generate_random_input(num_simulations, num_days, volatility, drift, last_price)

    return simulated_prices, mean_daily_return, volatility

# Parameters
ticker = "NVDA" # Stock ticker symbol
start_date = "2020-01-01"  # Start date for historical data
end_date = "2024-02-02"  # End date for historical data
num_simulations = 150 # Number of simulations; for reference 50k takes around 20 seconds to create both images
# (first one almost crashed) CPU i9-12900H, and the .csv is 132MB. Do with this info what you please.
num_days = 100  # Number of days you want to run these simulations through

simulated_prices, mean_daily_return, volatility = monte_carlo_simulation(ticker, start_date, end_date, num_simulations, num_days)

simulation_data = pd.DataFrame({
    "Simulation": np.arange(1, num_days + 1),
    "Mean_Price": simulated_prices.mean(axis=1),
    "5th_Percentile": np.percentile(simulated_prices, 5, axis=1),
    "95th_Percentile": np.percentile(simulated_prices, 95, axis=1)
})

simulation_data = pd.concat([simulation_data, pd.DataFrame(simulated_prices.T, columns=[f"Day_{i+1}" for i in range(num_days)])], axis=1)
desktop_path = os.path.join(os.path.join(os.path.expanduser("~")), "Desktop")
csv_file_path = os.path.join(desktop_path, "monte_carlo_simulation_results.csv")
simulation_data.to_csv(csv_file_path, index=False, float_format="%.6f")

pd.set_option("display.max_rows", None) 
print("Simulation Results:")
print(simulation_data)

plt.figure(figsize=(10, 6))
plt.plot(simulated_prices)
plt.title(f"Monte Carlo Simulation - {ticker} Stock Price Scenarios")
plt.xlabel("Days")
plt.ylabel("Stock Price")
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(simulated_prices, color="gray", alpha=0.1)
plt.plot(np.percentile(simulated_prices, 5, axis=1), label="5th Percentile", linestyle="dashed", color="red")
plt.plot(np.percentile(simulated_prices, 95, axis=1), label="95th Percentile", linestyle="dashed", color="blue")
plt.title(f"Monte Carlo Simulation - {ticker} Stock Price Scenarios with Confidence Intervals")
plt.xlabel("Days")
plt.ylabel("Stock Price")
plt.legend()
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(simulated_prices.T, color="gray", alpha=0.1)
plt.title(f"Monte Carlo Simulation - {ticker} Stock Price Scenarios")
plt.xlabel("Days")
plt.ylabel("Stock Price")
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(simulation_data["Mean_Price"], label="Mean Price", color="black")
plt.fill_between(simulation_data.index, simulation_data["5th_Percentile"], simulation_data["95th_Percentile"], color="gray", alpha=0.3)
plt.title(f"Monte Carlo Simulation - {ticker} Stock Price Scenarios with Confidence Intervals")
plt.xlabel("Days")
plt.ylabel("Stock Price")
plt.legend()
plt.show()

print(f"Mean Daily Return: {mean_daily_return:.6f}")
print(f"Volatility: {volatility:.6f}")
