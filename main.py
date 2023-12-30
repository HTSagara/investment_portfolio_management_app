import sys
import RiskReturn
import StockListMgr
 

def menu():
    print("Welcome to Investment Portfolio Management App Demo\n")
    choice = input("A: Manage stock list\nB: See completed portfolio\nC: Search stock data\nQ: Logout\n\nPlease enter your choice: ")
    return choice
    

if __name__=="__main__":
    choice = menu()
    while choice.lower() != "q":
        if choice.lower() == "a":
            print("Manage stock list")
            StockListMgr.stock_list_mgr()
            choice = menu()

        elif choice.lower() == "b":
            print("See completed portfolio")
            choice = menu()

        elif choice.lower() == "c":
            print("Risk and return calculator")
            RiskReturn.risk_return()
            choice = menu()

        else:
            print("please chose a valid input")
            choice = menu()
    sys.exit()