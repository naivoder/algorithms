"""
this file benchmarks the "forward" and "reverse" stack implementations in queue.py to demonstrate difference in runtimes
interesting to note that the forward queue is 5x faster, which implies that the pop(0) operation is significantly more expensive than the insert(0, i) operation.

"""
import random
import time
from queue import *

testCase = [random.randint(0, 1000000) for x in range(100000)]

forwardQueue = Queue()
reverseQueue = ReverseQueue()

for item in testCase:
    forwardQueue.push(item)
    reverseQueue.push(item)

forwardStart = time.time()
while not forwardQueue.isEmpty():
    forwardQueue.pull()
forwardTime = time.time() - forwardStart

reverseStart = time.time()
while not reverseQueue.isEmpty():
    reverseQueue.pull()
reverseTime = time.time() - reverseStart

print("Time to empty forward queue: %8.5fs" % forwardTime)
print("Time to empty reverse queue: %8.5fs" % reverseTime)
