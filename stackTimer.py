"""
this file benchmarks the "good" and "bad" stack implementations in stack.py to demonstrate difference in runtimes

"""

import random
import time
from stack import *

testCase = [random.randint(0, 1000000) for x in range(100000)]

goodStack = Stack()
badStack = BadStack()

for item in testCase:
    goodStack.push(item)
    badStack.push(item)

goodStart = time.time()
while not goodStack.isEmpty():
    goodStack.pull()
goodTime = time.time() - goodStart

badStart = time.time()
while not badStack.isEmpty():
    badStack.pull()
badTime = time.time() - badStart

print("Time to empty good stack: %8.5fs" % goodTime)
print("Time to empty bad stack: %8.5fs" % badTime)
