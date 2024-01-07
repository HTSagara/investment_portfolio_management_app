import yfinance as yf

class FundamentalData:
    def __init__(self,stock_ticker):
        self.stock = yf.Ticker(stock_ticker)

    def get_pe_ratios(self):
        profitMargins = self.stock.info['profitMargins']
        trailingPE = self.stock.info['trailingPE']
        forwardPE = self.stock.info['forwardPE']
        pegRatio = self.stock.info['pegRatio']

        return {
            'Profit Margins': profitMargins,
            'Trailing P/E': trailingPE,
            'Forward P/E': forwardPE,
            'PEG Ratio': pegRatio
        }
        
    def get_price_to_sales(self):
        return self.stock.info['priceToSalesTrailing12Months']

    def get_price_to_book(self):
        return self.stock.info['priceToBook']

    def get_debt_to_equity(self):
        return self.stock.info['debtToEquity']

    def get_ebitda_margin(self):
        return self.stock.info['ebitdaMargins']

    def get_dividend_info(self):
        dividend_yield = self.stock.info['dividendYield']
        payout_ratio = self.stock.info['payoutRatio']

        return {
            'Dividend Yield': dividend_yield,
            'Payout Ratio': payout_ratio
        }

    def display(self):
        # print("Price to earnings ratios:\n" , self.get_pe_ratios() , "\n")
        peRatios = self.get_pe_ratios()
        for ratio, value in peRatios.items():
            print(f"{ratio}: {value}\n")

        print("Price to sales: " , self.get_price_to_sales() , "\n")
        print("Price to book: " , self.get_price_to_book() , "\n")
        print("Debit to equity: " , self.get_debt_to_equity() , "\n")
        print("EBITDA Margin: " , self.get_ebitda_margin() , "\n")
        # print("Dividends ratios: " , self.get_dividend_info() , "\n")

        dividendsRatios = self.get_dividend_info()
        for ratio, value in dividendsRatios.items():
            print(f"{ratio}: {value}\n")
