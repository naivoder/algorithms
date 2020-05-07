"""
this file implements the bubble sort algorithm, which makes multiple passes through a list comparing adjacent items and exchanging when necessary
the algorithm requires n-1 passes to guarantee a sorted collection, O(n^2) runtime.
the advantage to bubble sort is that a pass with no swaps indicates a sorted list, which might be a faster solution for collections with few items, demonstrated in the shortBubble function.

"""
def bubbleSim(collection):
    for loop in range(len(collection) - 1, 0, -1):
        for index in range(loop):
            if collection[index] > collection[index + 1]:
                collection[index], collection[index + 1] = collection[index + 1], collection[index]
    return collection

def bubble(collection):
    for loop in range(len(collection) - 1, 0, -1):
        for index in range(loop):
            if collection[index] > collection[index + 1]:
                hold = collection[index]
                collection[index] = collection[index + 1]
                collection[index + 1] = hold
    return collection

def bubbleAlt(collection):
    loop = len(collection) -1
    while loop > 0:
        for index in range(loop):
            if collection[index] > collection[index + 1]:
                hold = collection[index]
                collection[index] = collection[index + 1]
                collection[index + 1] = hold
        loop -= 1
    return collection

def shortBubble(collection):
    exchange = True
    loop = len(collection) - 1
    while loop > 0 and exchange:
        exchange = False
        for index in range(loop):
            if collection[index] > collection[index + 1]:
                collection[index], collection[index + 1] = collection[index + 1], collection[index]

if __name__=="__main__":
    testA = [86, 49, 13, 45, 39, 55, 94, 21, 39]
    testB = testA[:]; testC = testA[:]; testD = testA[:]
    print("###---Bubble Sort---###")
    print("Test Data:", testA)
    print("Sorted Data:", bubble(testA))
    print("###---Bubble Sort (Alt)---###")
    print("Test Data:", testB)
    print("Sorted Data:", bubbleAlt(testB))
    print("###---Bubble Sort (Simul-Swap)---###")
    print("Test Data:", testC)
    print("Sorted Data:", bubbleAlt(testC))
    print("###---Bubble Sort (Short)---###")
    print("Test Data:", testD)
    print("Sorted Data:", bubbleAlt(testD))
