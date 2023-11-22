Robinhood trading application

This application takes 2 etfs, initially buys $50 of both.

The stop condition is if the loss since start exceed a loss limit.
Set to $25 constant.

At start, calculate the current rate between the 2 stock prices,
and every 10 minutes, if that rate has increased by a margin,
buy $2 of the most expensive, and sell $2 of the cheapest.

