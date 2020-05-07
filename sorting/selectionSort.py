"""
this file implements a basic selection sort algorithm, which improves upon bubble sort by only making one swap per pass through the collection. While the algorithm still requires n-1 passes and thus O(n^2) runtime, it performs fewer swaps and so generally completes faster than the bubble sort algorithm.

"""
import random

def selection(collection):
    for slot in range(len(collection) - 1, 0, -1):
        max = 0
        for index in range(1, slot + 1):
            if collection[index] > collection[max]:
                max = index
        collection[slot], collection[max] = collection[max], collection[slot]
    return collection
    
if __name__=="__main__":
    test = [random.randint(0, 100) for num in range(10)]
    print("###---Selection Sort---###")
    print("Test Data:", test)
    print("Sorted Data:", selection(test))
