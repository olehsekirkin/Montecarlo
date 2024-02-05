# Monte Carlo Simulation
Monte Carlo simulation, a computational technique that uses random sampling to model and analyze complex systems or processes by simulating multiple possible outcomes.

# Description
Monte Carlo simulation is a versatile computational method used to model and analyze systems that involve randomness. Named after the famous Monte Carlo Casino in Monaco, the technique relies on generating numerous random samples or scenarios to estimate probabilities and outcomes. The underlying concept is based on the law of large numbers, which states that as the number of random samples increases, the simulated results converge toward accurate statistical representations of the system being modeled.

The technique is particularly useful when analyzing the potential outcomes of financial investments, assessing portfolio performance, and making strategic decisions. One of the key applications of Monte Carlo simulations in finance is the evaluation of investment portfolios. For each simulated scenario, the Monte Carlo simulation calculates the portfolio's performance, providing a range of potential outcomes. By repeating this process thousands of times, the analyst obtains a probability distribution of portfolio returns. This distribution offers insights into the likelihood of achieving certain financial goals, the potential downside risks, and the overall resilience of the portfolio under various market conditions.

In summary, Monte Carlo simulation in finance enables a more sophisticated and realistic assessment of investment strategies by incorporating the uncertainty inherent in financial markets.

# Getting started
I tried to explain as much as I could as I was coding this one. Install yfinance, numpy, matplotlib and pandas.

Line 54 to 59 are parameters you can change. 

This creates a .csv in your desktop, open with Excel and: 1) select column A, go to Data, Text to Columns, Delimited, Comma and Finish; II) select column A again, ctrl+shit+right arrow, Home, Format, Column width, 14.
Now you can clearly see your simulations data! :D

# What I Learned
- Even more about pandas and the uses this library has
- Numpy (I will be using this in the future for sure)
- Matplotlib

# What's left
Oh well, I feel like there is a lot left for this project. First I need to add the possibility of adding more than one stock to the simulation, creating a proper portfolio (correlations between them, etc), I need to fix the .csv (I know where the error is, I just don't know how to fix it right now) and I want to add some kind of "analyzer" of the data that the simulations creates. Any other suggestion is welcome!

