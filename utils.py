import stock
import robin_stocks.robinhood as r
import time
def ratio(p1, p2):
    return float(p1)/float(p2)

def ratioDif(ratio1, ratio2):
    return abs((ratio1 - ratio2) / ratio1)

def calculateLoss(stock1):
    return stock1.getPrice() * len(stock1.orders()) - stock1.spent()

def performance():
    holdings = r.account.get_open_stock_positions()
    tickers = [r.get_symbol_by_url(item["instrument"]) for item in holdings]
    quantities = [float(item["quantity"]) for item in holdings]
    prevClose = r.get_quotes(tickers, "previous_close")
    lastPrice = r.get_quotes(tickers, "last_trade_price")
    profitPerShare = [float(lastPrice[i]) - float(prevClose[i]) for i in range(len(tickers))]
    profit = [profitPerShare[i] * quantities[i] for i in range(len(tickers))]

    return profit
