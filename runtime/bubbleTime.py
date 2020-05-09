"""
this file benchmarks two different versions of the bubble sort algorithm, just because I was curious.
'ffi' stands for 'For-For-If'
'wfi' stands for 'While-For-If'
SPOILER... they're identical. Substituting a while loop has no noticable effect on runtime.
the third version of the algorithm utilizes Python's simultaneous assignment property to reduce the number of steps, however it also shows no noticable improvement in runtime.

"""
import timeit, random
from timeit import Timer
from sorting.bubbleSort import *

ffiData = [random.randint(0,100) for num in range(1000)]
wfiData = ffiData[:]
simData = ffiData[:]

ffiBubble = Timer("bubble(ffiData)", "from __main__ import bubble, ffiData")
wfiBubble = Timer("bubbleAlt(wfiData)", "from __main__ import bubbleAlt, wfiData")
simBubble = Timer("bubbleSim(simData)", "from __main__ import bubbleSim, simData")

ffiTime = ffiBubble.timeit(number=1000)
wfiTime = wfiBubble.timeit(number=1000)
simTime = simBubble.timeit(number=1000)

print("Sorting, this may take a while...")
print("FFI Bubble Sort Algorithm: %5.3fs" % ffiTime)
print("WFI Bubble Sort Algorithm: %5.3fs" % wfiTime)
print("Simul-Swap Bubble Sort Algorithm: %5.3fs" % simTime)
