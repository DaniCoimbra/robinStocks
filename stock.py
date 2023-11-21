import robin_stocks.robinhood as r

class Stock:
    def __init__(self, stockName):
        self.stockName = stockName

    def getInfo(self):
        return r.stocks.find_instrument_data(self.stockName)[0]["simple_name"]

    def getPrice(self):
        return r.stocks.get_latest_price(self.stockName)[0]

    def getQuote(self):
        return r.stocks.get_stock_quote_by_symbol(self.stockName)

    def buy(self, price):
        return r.orders.order_buy_fractional_by_price(self.stockName, price)

    def sell(self, price):
        return r.orders.order_sell_fractional_by_price(self.stockName, price)