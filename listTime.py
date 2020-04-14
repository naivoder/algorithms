"""
This file creates identical lists via four methods and uses the timeit module to compare the runtimes.

"""

def concatenate():
    lst = []
    for number in range(1000):
        lst = lst + [number]

def append():
    lst = []
    for number in range(1000):
        lst.append(number)

def comprehend():
    lst = [number for number in range(1000)]

def construct():
    lst = list(range(1000))

import timeit

concatenateTime = timeit.Timer("concatenate()", "from __main__ import concatenate")
print("Concatenate: ", concatenateTime.timeit(10000), "seconds")

appendTime = timeit.Timer("append()", "from __main__ import append")
print("Append: ", appendTime.timeit(10000), "seconds")

comprehendTime = timeit.Timer("comprehend()", "from __main__ import comprehend")
print("Comprehend: ", comprehendTime.timeit(10000), "seconds")

constructTime = timeit.Timer("construct()", "from __main__ import construct")
print("Construct: ", constructTime.timeit(10000), "seconds")
