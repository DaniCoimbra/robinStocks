import robin_stocks.robinhood as r
import time
from stock import Stock
import utils

#login
login = r.login("elena.asparouhova@utah.utah.edu","CoronaLearning")

#stock names
stock1 = "SPHD"
stock2 = "SPHD"

#initialize stocks
s1 = Stock(stock1)
s2 = Stock(stock2)

#ratio margin
margin = 0.1

#starting loss and loss limit
loss = 0.00
lossLimit = 25.00

performance = utils.performance()

initialRatio = utils.ratio(s1.getPrice(),s2.getPrice())

s1.buy(50)
s2.buy(50)

while(loss < lossLimit):

    for i in range(60):
        performance = utils.performance()

        if performance < 0:
            loss += abs(performance)

        time.sleep(10)

    # time.sleep(600)

    ratio = utils.ratio(s1.getPrice(),s2.getPrice())

    # if current ratio between stocks has shifted by more than margin, buy
    # most expensive stock and sell cheaper one
    if utils.ratioDif(ratio, initialRatio) >= margin:
        if s1.getPrice() > s2.getPrice():
            s1.buy(2)
            s2.sell(2)
        else:
            s2.sell(2)
            s1.buy(2)

        initialRatio = ratio

    # performance = utils.performance()
    #
    # if performance < 0:
    #     loss += abs(performance)




