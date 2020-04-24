"""
this file benchmarks the deque abstract datatype implementation, note that operations from "the front" are much faster than from "the rear"

"""
import time, random
from deque import Deque

testCase = [random.randint(0, 10000000) for x in range(100000)]
forwardDeque = Deque()
reverseDeque = Deque()

forwardLoadStart = time.time()
for num in testCase:
    forwardDeque.pushFront(num)
forwardLoadTime = time.time() - forwardLoadStart

reverseLoadStart = time.time()
for num in testCase:
    reverseDeque.pushRear(num)
reverseLoadTime = time.time() - reverseLoadStart

forwardDumpStart = time.time()
while not forwardDeque.isEmpty():
    forwardDeque.pullFront()
forwardDumpTime = time.time() - forwardDumpStart

reverseDumpStart = time.time()
while not reverseDeque.isEmpty():
    reverseDeque.pullRear()
reverseDumpTime = time.time() - reverseDumpStart

print("Time to load deque from front: %8.5fs" % forwardLoadTime)
print("Time to load deque from rear: %8.5fs" % reverseLoadTime)
print("Time to empty deque from front: %8.5fs" % forwardDumpTime)
print("Time to empty deque from rear: %8.5fs" % reverseDumpTime)
