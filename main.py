import robin_stocks.robinhood as r
import time
import env
from stock import Stock
import utils
import pyotp

totp = pyotp.TOTP("My2factorAppHere").now()
login = r.authentication.login(env.username,env.password, store_session=True, mfa_code=totp)
#login = r.authentication.login(env.username,env.password, store_session=False, mfa_code=totp)

my_stocks = r.build_holdings()
for key,value in my_stocks.items():
    print(key,value)
print()

#stock names
stock1 = "SPHD"
stock2 = "ICLN"

#initialize stocks
s1 = Stock(stock1)
s2 = Stock(stock2)

stocks = [stock1,stock2]

#ratio margin
margin = 0.001

#starting loss and loss limit
loss = 0.00
lossLimit = 25.00

print("initial " + s1.stockName + " price: " + s1.getLatestPrice())
print("initial " + s2.stockName + " price: " + s2.getLatestPrice())

initialRatio = utils.ratio(s1.getLatestPrice(),s2.getLatestPrice())
print("initial ratio between stocks: ", end="")
print(initialRatio)

print()

s1.buy(50)
s2.buy(50)

while(loss < lossLimit):
    print("Current Loss: ", end="")
    print(loss)
    lastPriceS1 = s1.getLatestPrice()
    lastPriceS2 = s2.getLatestPrice()

    for i in range(5):
        performance = utils.performance(s1, s2)

        if performance < 0:
            loss = abs(performance)

        for j in range(60):
            print("\rTime for next transaction: {} seconds.".format(300 - (60*i + j)), end='')
            time.sleep(1)

    ratioDif = utils.ratioDif(s1, s2, initialRatio)

    print()
    print(s1.stockName + " price: " + s1.getLatestPrice())
    print(s2.stockName + " price: " + s2.getLatestPrice())

    print("Ratio difference between previous and current period: ", end="")
    print(ratioDif)
    print()

    # if current ratio between stocks has shifted by more than margin, buy
    # most expensive stock and sell cheaper one
    if ratioDif >= margin:
        print("Margin exceeded")
        if s1.getLatestPriceDif(lastPriceS1) > s2.getLatestPriceDif(lastPriceS2):
            print("Bought $2 of " + s1.stockName + "and Sold $2 of " + s2.stockName)
            s1.buy(2)
            s2.sell(2)
        else:
            print("Bought $2 of " + s2.stockName + "and Sold $2 of " + s1.stockName)
            s2.sell(2)
            s1.buy(2)

        initialRatio = utils.ratio(s1.getLatestPrice(),s2.getLatestPrice())

    else:
        print("Margin not exceeded")

print("Finished")


