# Monte Carlo Simulation
Monte Carlo simulation, a computational technique that uses random sampling to model and analyze complex systems or processes by simulating multiple possible outcomes.

<p align="center">
  <img src="https://miro.medium.com/v2/resize:fit:1400/1*eSpxYWfHSm_JKDH0tR6F6g.png" alt="Title" width="600px" height="300px">
</p>

## Description
A Monte Carlo simulation is a computational technique that utilizes random sampling to model and analyze the behavior of complex systems or processes. It involves running numerous simulations using random inputs, allowing for the assessment of a wide range of possible outcomes and their associated probabilities. The method is particularly useful when dealing with problems that have significant uncertainty or involve multiple interacting variables. In finance, Monte Carlo simulations are widely employed for risk assessment, portfolio optimization, and option pricing. Here's a more detailed explanation of how Monte Carlo simulations are applied in finance:

### Risk Assessment:
Investors and financial analysts use Monte Carlo simulations to assess the risk associated with different investment portfolios. By incorporating random variations in key financial parameters, such as asset returns and interest rates, the simulation can generate a distribution of possible portfolio returns. This distribution helps investors understand the range of potential outcomes and the likelihood of achieving specific financial goals.

### Portfolio Optimization:
Monte Carlo simulations are instrumental in the optimization of investment portfolios. By simulating various asset allocation strategies and weighting schemes, investors can identify combinations that provide the highest expected returns for a given level of risk or achieve specific risk-return trade-offs.

### Option Pricing:
Options, which are financial derivatives, derive their value from the underlying asset's price and other factors. Monte Carlo simulations are often employed to model the future price movements of the underlying asset. By simulating a large number of possible price paths, analysts can estimate the option's fair value and assess the associated risk.

### Financial Planning:
Monte Carlo simulations are valuable tools in financial planning. They can help individuals and financial planners model different scenarios for factors like investment returns, inflation, and life expectancy. This aids in creating more robust financial plans that account for uncertainties and unforeseen events.

### Credit Risk Assessment:
Financial institutions use Monte Carlo simulations to assess credit risk by modeling potential future scenarios and their impact on borrowers' ability to meet their obligations.

Overall, Monte Carlo simulations provide a powerful framework for decision-making in finance by incorporating the uncertainty inherent in financial markets and enabling stakeholders to make more informed and robust choices.

## Getting started
I tried to explain as much as I could as I was coding this one. Install yfinance, numpy, matplotlib and pandas.

Line 54 to 59 are parameters you can change. 

This creates a .csv in your desktop, open with Excel and: 1) select column A, go to Data, Text to Columns, Delimited, Comma and Finish; II) select column A again, ctrl+shit+right arrow, Home, Format, Column width, 14.
Now you can clearly see your simulations data! :D

If not you can just use the simulation data as a dataset for whatever you need.

## What I Learned
- Even more about pandas and the uses this library has
- Numpy
- Matplotlib

## What's left
Oh well, I feel like there is a lot left for this project. First I need to add the possibility of adding more than one stock to the simulation, creating a proper portfolio (correlations between them, etc), I need to fix the .csv (I know where the error is, I just don't know how to fix it right now) and I want to add some kind of "analyzer" of the data that the simulations creates. Will probably use the dataset it creates for some Machine Learning model. Any other suggestion is welcome!

