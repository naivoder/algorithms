"""
this file implements a merge sort algorithm, a recursive "divide and conquer" algorithm that continually splits lists in half

"""
import random

def merge(collection, debug=False):
    if debug:
        print("Splitting:", collection)
    if len(collection) > 1:
        # split and run merge sort on both halves
        midpoint = len(collection) // 2
        left, right = collection[:midpoint], collection[midpoint:]
        merge(left); merge(right)
        # take smallest item from each list (i, j) and place back into collection at position k
        i, j, k = 0, 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                collection[k] = left[i]
                # increment left index
                i += 1
            else:
                collection[k] = right[j]
                # increment right index
                j += 1
            # increment master index
            k += 1
        # if one list is empty, take the rest of the other list
        while i < len(left):
            collection[k] = left[i]
            i += 1; k += 1
        while j < len(right):
            collection[k] = right[j]
            j += 1; k += 1
    if debug:
        print("Merging:", collection)
    return collection

if __name__=="__main__":
    test_data = [random.randint(1, 100) for index in range(2000)]
    print("###---Merge Sort---###")
    merge(test_data, debug=True)
