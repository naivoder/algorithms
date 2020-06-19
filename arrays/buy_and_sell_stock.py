"""
this file implements an algorithm to determine the maximum profit that could have been made buying and selling a certain stock given an array of prices

a condition is imposed that buying or selling must take place at the very beginning of a day, and therefore on different days.

while a brute force algorithm would iterate through every combination of high and low prices using O(n^2) time and O(n) space, a more elegant solution is to keep track of the minimum element and maximum difference seen thus far and simply check if the difference between each day's starting price and known minimum is higher than the current maximum

this algorithm uses O(n) time and O(1) space complexity

"""

import random

def buy_and_sell(prices:list) -> float:
    min_price, max_profit = float('inf'), 0.0
    for price in prices:
        sell_today = price - min_price
        max_profit = max(max_profit, sell_today)
        min_price = min(min_price, price)
    return max_profit

if __name__=="__main__":
    test_prices = [round(random.random()*100, 2) for day in range(30)]
    print("Stock prices:\n", test_prices)
    print("###---Buy and Sell for Max Profit---###")
    print("Max profit:", buy_and_sell(test_prices))
