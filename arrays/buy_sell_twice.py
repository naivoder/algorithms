"""
this file is a variation on buy_and_sell_stock.py, in which the goal has been modified slightly to instead determine the most profitible combination of two buy/sell decisions

the brute force algorithm mentioned in the first solution could also be applied here, resulting in O(n^4) time complexity and O(n) space complexity as each combination of buy/sell trades is calculated alongside each potential second buy/sell pair. this can be improved to O(n^2) using a divide an conquer algorithm applied to two subarrays.

a more elegant solution is to keep track of previous computations to reduce the total work. we find the best solution starting at each day iteratively (a[0, j]), and then perform a reverse iteration computing the best buy and sell solution prior to that day (a[j, n-1])

example: [12, 11, 13, 9, 12, 8, 14, 13, 15] --> forward pass = [0, 0, 2, 2, 3, 3, 6, 6, 7]
so the most profit can be made by selling at 15...
                                            --> reverse pass = [7, 7, 7, 7, 7, 7, 2, 2, 0]

adding the forward and reverse passes = [7, 7, 7, 9, 9, 10, 5, 8, 6]
therefore max profit = 10 (buy @ 9, sell @ 12, buy @ 8, sell @ 15)

"""

from random import random

def buy_and_sell_twice(prices:list) -> float:
    min_price, max_profit, max_price = float('inf'), 0.0, float('-inf')
    # init array for forward pass
    first_profits = [0.0] * len(prices)
    # first pass computes largest buy/sell pair
    for i, share_price in enumerate(prices):
        sell_today = share_price - min_price
        max_profit = max(max_profit, sell_today)
        min_price = min(min_price, share_price)
        first_profits[i] = max_profit
    # second pass computes optimal sell/buy pivot
    for i, share_price in reversed(list(enumerate(prices[1:], 1))):
        max_price = max(max_price, share_price)
        potential_total_profit = max_price - share_price + first_profits[i]
        max_profit = max(max_profit, potential_total_profit)
    return round(max_profit, 2)

if __name__=="__main__":
    example_prices = [12, 11, 13, 9, 12, 8, 14, 13, 15]
    random_prices  = [round(random()*100, 2) for day in range(9)]
    print("###---Buy and Sell Stock Twice---###")
    print("Example prices:", example_prices)
    print("Max profit:", buy_and_sell_twice(example_prices))
    print("Randomly generated prices:", random_prices)
    print("Max profit:", buy_and_sell_twice(random_prices))
