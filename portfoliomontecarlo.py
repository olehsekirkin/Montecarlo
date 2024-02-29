import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os


def fetch_stock_data(tickers, start_date, end_date):
    stock_data = yf.download(tickers, start=start_date, end=end_date)['Adj Close']
    return stock_data


def calculate_portfolio_returns_and_parameters(stock_data, weights):
    returns = stock_data.pct_change().dropna()
    portfolio_returns = (returns * weights).sum(axis=1)

    volatility = portfolio_returns.ewm(span=30, adjust=False).std().iloc[-1]
    mean_daily_return = portfolio_returns.mean()

    drift = mean_daily_return - 0.5 * volatility ** 2

    return returns, portfolio_returns, mean_daily_return, volatility, drift


def generate_random_input(num_simulations, num_days, volatility, drift, last_price):
    dt = 1 / 252
    random_input = np.random.normal(0, 1, size=(num_simulations, num_days))

    random_returns = drift * dt + volatility * np.sqrt(dt) * random_input.T

    simulated_prices = last_price * np.exp(np.cumsum(random_returns, axis=0))

    return simulated_prices


def plot_correlation_matrix(returns):
    correlation_matrix = returns.corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
    plt.title('Correlation Matrix of Stock Returns')
    plt.show()


def monte_carlo_simulation(tickers, weights, start_date, end_date, num_simulations, num_days):
    stock_data = fetch_stock_data(tickers, start_date, end_date)

    returns, portfolio_returns, mean_daily_return, volatility, drift = calculate_portfolio_returns_and_parameters(
        stock_data, weights)

    last_prices = (stock_data.iloc[-1] * weights).sum()

    simulated_prices = generate_random_input(num_simulations, num_days, volatility, drift, last_prices)

    plot_correlation_matrix(returns)

    return simulated_prices, mean_daily_return, volatility, returns


# Portfolio parameters
tickers = ['NVDA', 'AAPL', 'MSFT']
weights = np.array([0.4, 0.3, 0.3])
start_date = '2020-01-01'
end_date = '2024-02-02'
num_simulations = 150
num_days = 100

simulated_prices, mean_daily_return, volatility, returns = monte_carlo_simulation(tickers, weights, start_date,
                                                                                  end_date, num_simulations, num_days)

plt.figure(figsize=(10, 6))
plt.plot(simulated_prices)
plt.title('Monte Carlo Simulation - Portfolio Value Scenarios')
plt.xlabel('Days')
plt.ylabel('Portfolio Value')
plt.show()

print(f'Mean Daily Return: {mean_daily_return:.6f}')
print(f'Volatility: {volatility:.6f}')

