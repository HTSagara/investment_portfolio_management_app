import sys
import RiskReturn
import StockListMgr
import Predictions
import FundamentalAnalysis
 

def menu():
    print("\n***************************************************")
    print("Welcome to Investment Portfolio Management App Demo\n")
    print("\n***************************************************")
    choice = input("A: Manage stock list\nB: Stock fundamental analysis \nC: Calculate risk and return\nD: Stock price and portfolio prediction (upcoming)\nQ: Logout\n\nPlease enter your choice: ")
    return choice
    

if __name__=="__main__":
    choice = menu()
    while choice.lower() != "q":
        if choice.lower() == "a":
            print("\n***Manage stock list***")
            StockListMgr.stock_list_mgr()
            choice = menu()

        elif choice.lower() == "b":
            print("\n***Stock fundamental analysis***")
            while True:
                stockTicker = input("Enter the stock that you would like to analyze or exit: ").upper()
                if stockTicker != 'EXIT':
                    fundamental_ratios = FundamentalAnalysis.FundamentalData(stockTicker)
                    fundamental_ratios.display()
                else:
                    break
            choice = menu()

        elif choice.lower() == "c":
            print("\n***Risk and return calculator***")
            RiskReturn.risk_return()
            choice = menu()

        elif choice.lower() == 'd':
            print("\n***Stock price and portfolio prediction (upcoming)***")
            Predictions.prediction_main()
            choice = menu()

        else:
            print("please chose a valid input")
            choice = menu()
    sys.exit()