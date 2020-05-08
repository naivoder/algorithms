"""
this file implements the shell sort algorithm, which improves upon insertion sort by breaking the collection into several smaller "sublists" which are each sorted via insertion sort before being recombined. shell sort uses an increment variable called the "gap" to create sublists.

"""
import random

def shell(collection):
    sublists = len(collection) // 2
    step = 1
    while sublists > 0:
        for start in range(sublists):
            gapInsertion(collection, start, sublists)
        print("Step", step, ":", collection)
        sublists = sublists // 2
        step += 1
    return collection

def gapInsertion(collection, start, gap):
    for index in range(start + gap, len(collection), gap):
        current = collection[index]
        position = index
        while position >= gap and collection[position - gap] > current:
            collection[position] = collection[position - gap]
            position = position - gap
        collection[position] = current

if __name__=="__main__":
    test = [random.randint(1, 100) for num in range(20)]
    print("###---Shell Sort---###")
    print("Test Data:", test)
    print("Sorted Data:", shell(test))
