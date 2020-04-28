"""
this file implements a radix sorting machine for base 10 integers. the radix machine contains one main bin and 10 digit bins. Every number starts in main bin, all numbers are sorted by ones position into digit bins, and then digit bins are emptied into main bin in order. This process is repeated for tens, hundreds, etc... places until all data is sorted.
will use a queue abstract datatype to simulate behavior of sorting bins.

"""

from queue import Queue
import random

mainBin = Queue()
zeroBin = Queue()
oneBin = Queue()
twoBin = Queue()
threeBin = Queue()
fourBin = Queue()
fiveBin = Queue()
sixBin = Queue()
sevenBin = Queue()
eightBin = Queue()
nineBin = Queue()

unsortedData = [random.randint(0,1000) for num in range(100)]
bins = [zeroBin, oneBin, twoBin, threeBin, fourBin, fiveBin, sixBin, sevenBin, eightBin, nineBin]

def radix(bins, unsortedData):

    for num in unsortedData:
        mainBin.push(num)
    print("Unsorted Data:")
    print(mainBin)

    maxNum = max(unsortedData)
    maxPlace = 0

    while(maxNum > 0):
        maxNum = maxNum // 10
        maxPlace += 1

    for place in range(maxPlace):
        while not mainBin.isEmpty():
            num = mainBin.pull()
            txt = str(num)
            try:
                dig = int(txt[-(place+1)])
            except:
                dig = 0
            bins[dig].push(num)
        for bin in bins:
            while not bin.isEmpty():
                num = bin.pull()
                mainBin.push(num)

    print("Sorted Data:")
    print(mainBin)
    return mainBin

if __name__=="__main__":
    radix(bins, unsortedData)
