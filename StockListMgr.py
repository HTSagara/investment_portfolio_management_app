import csv

class Stock:
    def __init__(self, ticker, quantity, avgPrice):
        self.ticker = ticker
        self.quantity = quantity
        self.avgPrice = avgPrice

    def to_dict(self):
        return {
            'ticker': self.ticker,
            'quantity': self.quantity,
            'avgPrice': self.avgPrice
        }
    
    def __str__(self):
        return f"{self.ticker} - Quantity: {self.quantity}, Average Price: {self.avgPrice}"
    
class StockListManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.stocks = self.load_stocks()

    def load_stocks(self):
        try:
            with open(self.file_path, 'r') as file:
                reader = csv.DictReader(file)
                stocks = [Stock(row['ticker'], int(row['quantity']), float(row['avgPrice'])) for row in reader]
            return stocks
        except FileNotFoundError:
            return []
        
    def save_stocks(self):
        with open(self.file_path, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['ticker', 'quantity', 'avgPrice'])
            writer.writeheader()
            for stock in self.stocks:
                writer.writerow(stock.to_dict())

    def add_stock(self, ticker, quantity, avgPrice):
        new_stock = Stock(ticker, quantity, avgPrice)
        self.stocks.append(new_stock)
        self.save_stocks()

    def delete_stock(self, ticker):
        self.stocks = [stock for stock in self.stocks if stock.ticker != ticker]
        self.save_stocks()

    def display_stocks(self):
        for stock in self.stocks:
            print(stock)

def stock_list_mgr():
    stock_manager = StockListManager('stocks.csv')

    while True:
         print("\n1: Add Stock\n2: Delete Stock\n3: Display Stocks\nQ: Quit")
         choice = input("Please enter your choice: ")

         if choice.lower() == 'q':
             break
         elif choice == '1':
             ticker = input("Enter stock ticker: ")
             quantity = int(input("Enter quantity: "))
             avg_price = float(input("Enter average price: "))
             stock_manager.add_stock(ticker, quantity, avg_price)
         elif choice == '2':
             ticker = input("Enter stock ticker to delete: ")
             stock_manager.delete_stock(ticker)
         elif choice == '3':
             stock_manager.display_stocks()
         else:
             print("Invalid choice. Please try again.")