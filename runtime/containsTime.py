"""
this file compares runtimes of the 'contains' operation between list and dictionary implementations, modified from Miller and Ranum example
iterating over a range of collection sizes demonstrates the O(1) behavior when used with a dictionary, compared to O(n) with list

"""

import timeit, random

print("Size\t\tList\tDictionary")
for size in range(10000, 1000001, 20000):
    runtime = timeit.Timer("random.randrange(%d) in collection" % size, "from __main__ import random, collection")
    collection = list(range(size))
    listTime = runtime.timeit(number=1000)
    collection = {index:None for index in range(size)}
    dictTime = runtime.timeit(number=1000)
    print("%-10d %10.3fs %10.3fs" % (size, listTime, dictTime))
