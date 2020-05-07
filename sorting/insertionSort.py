"""
this file implements a simple insertion sort algorithm, which maintains a sorted sublist in the lower positions of the collection, each new item is inserted back into the proper position within the sublist. this algorithm still has a runtime of O(n^2).

"""
import random

def insertion(collection):
    for index in range(1, len(collection)):
        value = collection[index]
        position = index
        while position > 0 and collection[position - 1] > value:
            collection[position] = collection[position - 1]
            position -= 1
        collection[position] = value
    return collection

if __name__=="__main__":
    test = [random.randint(0, 100) for num in range(10)]
    print("###---Insertion Sort----###")
    print("Test Data:", test)
    print("Sorted Data:", insertion(test))
