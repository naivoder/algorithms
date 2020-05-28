"""
this file implements an algorithm to divide 'x' by 'y' using bitwise operations

to compute the quotient the approach is to find the largest 'K' such that 2**(k*y) <= x
while x > y:
-> subtract 2**(k*y) from x
--> add 2**k to quotient
x = remainder

import to note that k will always decrease from its initial value
save time by keeping track of k from previous iteration

"""
import random

def divide(x, y):
    # arbitrarily set at 32
    # would need to increase for VERY large x...
    quotient, power = 0, 32
    # '<<' is essentially 'times 2 to the...'
    y_power = y << power
    while x >= y:
        while y_power > x:
            # divide by 2
            y_power = y_power >> 1
            power -= 1
        quotient += 1 << power
        x -= y_power
    return (quotient, x)

if __name__=="__main__":
    x_data = [random.randint(500,1000) for num in range(10)]
    y_data = [random.randint(0, 500) for num in range(10)]
    for i in range(len(x_data)):
        result = divide(x_data[i], y_data[i])
        print("%3s divided by %3s = %3s with a remainder of %3s" % (x_data[i], y_data[i], result[0], result[1]))
