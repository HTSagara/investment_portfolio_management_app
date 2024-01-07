from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def prediction_main():
    choice = menu()
    while True:
        if choice == '1':
            stockPrediction = input("Enter the stock ticker: ")
            single_stock(stockPrediction)
            choice = menu()
        elif choice == '2':
            portfolio_forecast("portfolio")
            choice = menu()
        else:
            break

def menu():
    print("Select the Forecast Option:")
    choice = input("1: Single stock\n2: Whole portfolio\n3: Quit\nSelect an option: ")
    return choice

def single_stock(ticker):
    # Predict the price of a single stock 
    print("Predicting {}...".format(ticker))

def portfolio_forecast(portfolio):
    # Predict the price of the whole portfolio in the csv
    print("Portfolio forecast {}".format(portfolio))
