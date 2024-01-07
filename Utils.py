import csv

def load_data():
    try:
        with open('stocks.csv', 'r') as file:
            reader = csv.DictReader(file)
            return [{'ticker': row['ticker'], 'quantity': int(row['quantity']), 'avgPrice': float(row['avgPrice'])} for row in reader]
    except FileNotFoundError:
        print("Error: stocks.csv not found.")
        return 