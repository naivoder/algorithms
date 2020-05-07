"""
this file implements the bubble sort algorithm, which makes multiple passes through a list comparing adjacent items and exchanging when necessary
the algorithm requires n-1 passes to guarantee a sorted collection

"""

def bubble(collection):
    for loop in range(len(collection) - 1, 0, -1):
        for index in range(loop):
            if collection[index] > collection[index + 1]:
                hold = collection[index]
                collection[index] = collection[index + 1]
                collection[index + 1] = hold
    return collection
    
if __name__=="__main__":
    test = [86, 49, 13, 45, 39, 55, 94, 21, 39]
    print("###---Bubble Sort---###")
    print("Test Data:", test)
    print("Sorted Data:", bubble(test))
