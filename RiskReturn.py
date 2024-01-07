import Utils

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt


def risk_return():

    stocks = Utils.load_data()

    # Fetch historical stocks data using yfinance 
    for stock in stocks:
        data = yf.download(stock['ticker'], start='2022-01-01', end='2023-12-23')
        stock['data'] = data['Close']

    # Calculate the daily or periodic returns for each stock in your portfolio
    for stock in stocks:
        stock['returns'] = stock['data'].pct_change()

    # Combine the returns of individual stocks to calculate the portfolio returns
    portfolioReturns = pd.DataFrame()
    for stock in stocks:
        portfolioReturns[stock['ticker']] = stock['returns']

    portfolioReturns['portfolio'] = portfolioReturns.mean(axis=1)

    # Calculate the volatility (risk) of the portfolio 
    portfolioRisk = portfolioReturns['portfolio'].std()

    # Print risk and return statistics
    print("Portfolio Risk: {:.2%}".format(portfolioRisk))
    print("Portfolio Annualized Return: {:.2%}".format(portfolioReturns['portfolio'].mean() * 252)) # Assuming 252 trading days in a year

    # Plot risk and return graph
    plt.scatter(portfolioRisk, portfolioReturns['portfolio'].mean() * 252, label='Portfolio')
    for stock in stocks:
        plt.scatter(stock['returns'].std(), stock['returns'].mean() * 252, label = stock['ticker'])

    plt.title('Risk-Return Trade-off')
    plt.xlabel('Volatility (Risk)')
    plt.ylabel('Return')
    plt.legend()
    plt.show()


