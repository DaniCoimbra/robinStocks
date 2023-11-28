import stock
import robin_stocks.robinhood as r
def ratio(p1, p2):
    return float(p1)/float(p2)

def ratioDif(s1, s2, ratio2):
    ratio1 = ratio(s1.getLatestPrice(),s2.getLatestPrice())
    return abs((ratio1 - ratio2) / ratio1)

# performance is how much share is worth - total payed per share
def performance(s1,s2):
    stock1quote = float(s1.getLatestPrice()) * s1.units - s1.cost
    stock2quote = float(s2.getLatestPrice()) * s2.units - s2.cost
    return stock1quote+stock2quote


def Performance(stocks):
    holdings = r.account.get_open_stock_positions()
    #tickers = [r.get_symbol_by_url(item["instrument"]) for item in holdings]
    tickers = stocks
    quantities = [float(item["quantity"]) for item in holdings if r.get_symbol_by_url(item["instrument"]) in tickers]
    prevClose = r.get_quotes(tickers, "previous_close")
    lastPrice = r.get_quotes(tickers, "last_trade_price")
    profitPerShare = [float(lastPrice[i]) - float(prevClose[i]) for i in range(len(tickers))]
    profit = [profitPerShare[i] * quantities[i] for i in range(len(tickers))]
    return sum(profit)

# def p2(stocks):
#     holdings = r.account.get_open_stock_positions()
#     #tickers = [r.get_symbol_by_url(item["instrument"]) for item in holdings]
#     tickers = stocks
#     quantities = [float(item["quantity"]) for item in holdings if r.get_symbol_by_url(item["instrument"]) in tickers]
#     prevClose = r.get_quotes(tickers, "previous_close")
#     lastPrice = r.get_quotes(tickers, "last_trade_price")
#     print(prevClose)
#     print(lastPrice)