"""
this file compares runtime of pop(i) vs pop(), initially over a list of size 2 million, then again over a range of list sizes demonstrating the O(1) vs O(n) behavior.

"""
import timeit
from timeit import Timer

attempts = 2000000

popFromZero = Timer("bubble.pop(0)", "from __main__ import bubble")
popFromEnd = Timer("bubble.pop()", "from __main__ import bubble")

bubble = list(range(attempts))
zeroTime = popFromZero.timeit(number=1000)

bubble = list(range(attempts))
endTime = popFromEnd.timeit(number=1000)

print("Speed comparison:")
print("Pop( ): %8.5fs" % endTime)
print("Pop(0): %8.5fs" % zeroTime)

print("\nRuntime comparison:")
print("pop( )\t\tpop(0)")

for size in range(1000000, 10000001, 1000000):
        bubble = list(range(size))
        zeroTime = popFromZero.timeit(number=1000)
        bubble = list(range(size))
        endTime = popFromEnd.timeit(number=1000)
        print("%.5fs\t%.5fs" % (endTime, zeroTime))
