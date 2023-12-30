# Investment Portfolio Management App

## Overview

The Investment Portfolio Management App is a simple Python application that allows users to manage their investment portfolio. The app provides functionality to calculate the risk and return of a stock portfolio and manage a list of stocks.

## Features

- **Risk and Return Calculator:** Calculate the risk and return of your investment portfolio based on historical stock data obtained from Yahoo Finance using `yfinance`.
- **Stock Management:** Add and delete stocks to/from your portfolio. The app stores stock information such as ticker, quantity, and average price in a CSV file (`stocks.csv`).

## Getting Started

### Install Dependencies

```bash
pip install yfinance pandas matplotlib
```

### Run the app

```bash
python main.py
```

## Usage

### 1. Manage stock list:

#### 1.1. Add a Stock:

- Choose option '1' in the main menu
- Enter the stock ticker, quantity, and average price.

#### 1.2. Delete a Stock:

- Choose option '2' in the main menu.
- Enter the stock ticker to delete.

#### 1.3. Display Stocks:

- Choose option '3' in the main menu to view the current list of stocks.

### 2. Calculate Risk and Return:

- Choose option 'A' in the main menu to calculate the risk and return of your portfolio.

### 3. Quit the App:

- Choose option 'Q' in the main menu to exit the app.

## Data Storage

- Stock information is stored in a CSV file named 'stocks.csv'.
- The CSV file includes columns for ticker, quantity, and average price.

## Dependencies

- yfinance: Fetch historical stock data.
- pandas: Data manipulation and analysis.
- matplotlib: Plotting graphs.

## Contributing

Feel free to contribute by submitting issues or pull requests. Your feedback and contributions are welcomed!

## Upcoming features

- Retrieve stock's fundamental data from analysis.
- Create stock price prediction.
- Provide the portfolio's feedback.
