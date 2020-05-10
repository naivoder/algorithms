"""
this file benchmarks implementations of various sorting algorithms

"""
import timeit, random
from timeit import Timer

from sorting.bubbleSort import *
from sorting.insertionSort import *
from sorting.mergeSort import *
from sorting.quickSort import *
from sorting.selectionSort import *
from sorting.shellSort import *

print("Sorting, this may take a while...")
for size in range(100, 10100, 1000):
    test_data = [random.randrange(0, 1000) for num in range(size)]
    bData, iData, mData, qData, seData, shData = test_data[:], test_data[:], test_data[:], test_data[:], test_data[:], test_data[:]
    bubbleSort = Timer("bubble(bData)", "from __main__ import bubble, bData")
    insertionSort = Timer("insertion(iData)", "from __main__ import insertion, iData")
    mergeSort = Timer("merge(mData)", "from __main__ import merge, mData")
    quickSort = Timer("quick(qData)", "from __main__ import quick, qData")
    selectionSort = Timer("selection(seData)", "from __main__ import selection, seData")
    shellSort = Timer("shell(shData)", "from __main__ import shell, shData")
    bubbleTime = bubbleSort.timeit(number=100)
    insertionTime = insertionSort.timeit(number=100)
    mergeTime = mergeSort.timeit(number=100)
    quickTime = quickSort.timeit(number=100)
    selectionTime = selectionSort.timeit(number=100)
    shellTime = shellSort.timeit(number=100)

    print("\nSize:", size)
    print("Bubble Sort: %14.5fs" % bubbleTime)
    print("Selection Sort: %11.5fs" % selectionTime)
    print("Quick Sort: %15.5fs" % quickTime)
    print("Merge Sort: %15.5fs" % mergeTime)
    print("Insertion Sort: %11.5fs" % insertionTime)
    print("Shell Sort: %15.5fs" % shellTime)
