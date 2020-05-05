"""
this file implements a simple sequential search algorithm. if data has linear relationship, each item can be visited in the order of their relative position.
the assumption is that the collection is unordered. this algorithm is O(n) because the worst case scenario requires a comparison against every item in the collection.
the ordered search only improves the algorithm in the case where the item is not found, and even then only slightly.

"""

def sequentialSearch(collection, item):
    index = 0; found = False
    while index < len(collection) and not found:
        if collection[index] is item:
            found = True
        else:
            index += 1
    return found

def orderedSequentialSearch(collection, item):
    index = 0; found = False;
    finished = False
    while index < len(collection) and not found and not finished:
        if collection[index] is item:
            found = True
        elif collection[index] > item:
            finished = True
        else:
            index += 1
    return found

if __name__=="__main__":
    test = [1,3,5,6,8,9,0,4,6,8,9,3,3,6]
    orderedTest = [1,1,1,2,3,4,5,7,9,9]
    print("Positive Test:")
    print(sequentialSearch(test, 5))
    print("Negative Test:")
    print(sequentialSearch(test, 2))
    print("Ordered Test:")
    print(sequentialSearch(orderedTest, 5))
