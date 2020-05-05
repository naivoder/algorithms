"""
this file implements a basic binary search algorithm, which has a runtime of O(logn)
although binary search is generally better than sequential search, it is important to note that for small values of n the addition cost of sorting is usually not worth it...

"""
def binarySearch(collection, item):
    found = False
    first = 0; last = len(collection) - 1
    while first <= last and not found:
        mid = (first + last) // 2
        if collection[mid] is item:
            found = True
        elif collection[mid] >= item:
            last = mid - 1
        else:
            first = mid + 1
    return found

def binaryRecursive(collection, item):
    if len(collection) is 0:
        return False
    else:
        mid = len(collection) // 2
    if collection[mid] is item:
        return True
    elif collection[mid] >= item:
            return binaryRecursive(collection[:mid], item)
    else:
        return binaryRecursive(collection[mid + 1:], item)

if __name__=="__main__":
    test = [0, 1, 4, 6, 7, 9, 34, 45, 76, 90]
    print("Positive Test (iterative):")
    print(binarySearch(test,  4))
    print("Negative Test (iterative):")
    print(binarySearch(test, 35))
    print("Positive Test (recursive):")
    print(binarySearch(test,  4))
    print("Negative Test (recursive):")
    print(binarySearch(test, 35))
