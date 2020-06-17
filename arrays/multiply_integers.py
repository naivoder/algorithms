"""
this file implements an algorithm to multiply two arbitrary precision integers as arrays to avoid potential overflow

"""

import random

def multiply_arrays(number_1:list, number_2:list, debug:bool = False) -> list:
    # xor to determine if product will be negative
    # example case: -1 ^ 1 ==> -1
    sign = -1 if (number_1[0] < 0) ^ (number_2[0] < 0) else 1
    # keep positive version for multiplication
    # example case: [1, 2, 3], [1, 2, 3]
    number_1[0], number_2[0] = abs(number_1[0]), abs(number_2[0])

    # initialize new list size of n+m (at most)
    # example case: [0] * 6
    product = [0] * (len(number_1) + len(number_2))

    for i in reversed(range(len(number_1))):
        for j in reversed(range(len(number_2))):
            # first pass: calculate ones place, overflow to 10s place
            # second pass: calculate tens place, overflow to hundreds place etc.
            if debug is True:
                print("\nproduct[%s + %s + 1] += %s * %s" % (i, j, number_1[i], number_2[j]))
                print("product[%s + %s] += product[%s + %s + 1] // 10" % (i, j, i, j))
            product[i + j + 1] += number_1[i] * number_2[j]
            product[i + j] += product[i + j + 1] // 10
            product[i + j + 1] %= 10

    # trim leading zeros
    product = product[next((i for i, x in enumerate(product) if x != 0), len(product)):] or [0]
    # return product with appropriate sign
    return [sign * product[0]] + product[1:]

if __name__=="__main__":
    print("###---Multipy Integer Arrays---###")
    number_1 = [-1, 2, 3]
    number_2 = [ 1, 2, 3]
    print("Simple example case: %s * %s" % (number_1, number_2))
    print("\nResult:", multiply_arrays(number_1, number_2, debug=True))
    number_1 = [-1] + [random.randint(1, 9) for x in range(10)]
    number_2 = [random.randint(1, 9) for x in range(10)]
    print("\nLarge example case: %s * %s" % (number_1, number_2))
    print("Result:", multiply_arrays(number_1, number_2))
