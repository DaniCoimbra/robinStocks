import robin_stocks.robinhood as r
import time

import env
from stock import Stock
import utils
import pyotp
import os

totp = pyotp.TOTP("My2factorAppHere").now()

#login
login = r.authentication.login(env.username,env.password, mfa_code=totp)
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

#ratio margin
margin = 0.0001

#starting loss and loss limit
loss = 0.00
lossLimit = 25.00

loss = initialPerformance = utils.performance()

print("initial performance: ", end="")
print(initialPerformance)

initialRatio = utils.ratio(s1.getPrice(),s2.getPrice())

print("initial ratio between stocks: ", end="")
print(initialRatio)

print("initial " + s1.stockName + " price: " + s1.getPrice())
print("initial " + s2.stockName + " price: " + s2.getPrice())

#print(r.account.load_account_profile())

print()
# s1.buy(50)
# s2.buy(50)

while(loss < lossLimit):
    print("Current Loss: ", end="")
    print(loss)

    for i in range(5):
        performance = utils.performance()

        if performance < 0:
            loss = abs(performance)

        for j in range(60):
            print("\rTime for next transaction: {} seconds.".format(300- (60*i + j)), end='')
            time.sleep(1)


    # time.sleep(600)
    print()
    ratio = utils.ratio(s1.getPrice(),s2.getPrice())
    print(s1.stockName + " price: " + s1.getPrice())
    print(s2.stockName + " price: " + s2.getPrice())
    print("Current ratio between stocks: ", end="")
    print(ratio)
    print()
    # if current ratio between stocks has shifted by more than margin, buy
    # most expensive stock and sell cheaper one

    if utils.ratioDif(ratio, initialRatio) >= margin:
        print("Margin exceeded")
        if s1.getPrice() > s2.getPrice():
            print("Bought $2 of " + s1.stockName + "and Sold $2 of " + s2.stockName)
            s1.buy(2)
            s2.sell(2)
        else:
            print("Bought $2 of " + s2.stockName + "and Sold $2 of " + s1.stockName)
            s2.sell(2)
            s1.buy(2)

        initialRatio = ratio
    else:
        print("Margin did not exceed")

    # performance = utils.performance()
    #
    # if performance < 0:
    #     loss += abs(performance)

print("End")


