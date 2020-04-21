"""
this file benchmarks the "kthSmallestNumber" solutions to demonstrate the difference in runtimes

"""

import timeit
from timeit import Timer
from kthSmallestNumber import *

linear = Timer("kthNumber_Linear(2, [5, 7, 3, 1, 9, 7, 4])", "from __main__ import kthNumber_Linear")
log = Timer("kthNumber_Log(2, [5, 7, 3, 1, 9, 7, 4])", "from __main__ import kthNumber_Log")

linearTime = linear.timeit()
logTime = log.timeit()

print("Linear Solution: %7.5fs" % linearTime)
print("Log Solution: %7.5fs" % logTime)
