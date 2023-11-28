import robin_stocks.robinhood as r

class Stock:
    units = 0
    cost = 0
    stockName = ""
    def __init__(self, stockName):
        self.stockName = stockName

    def getInfo(self):
        return r.stocks.find_instrument_data(self.stockName)[0]

    def getLatestPrice(self):
        return r.stocks.get_latest_price(self.stockName)[0]

    def getQuote(self):
        return r.stocks.get_stock_quote_by_symbol(self.stockName)

    def buy(self, price):
        order = r.orders.order_buy_fractional_by_price(self.stockName, price)
        self.cost += order["price"]
        self.units += order["quantity"]

    def sell(self, price):
        order = r.orders.order_sell_fractional_by_price(self.stockName, price)
        self.cost -= order.price()
        self.units -= order.quantity()

    def getLatestPriceDif(self, lastPrice):
        return self.getLatestPrice() - lastPrice
