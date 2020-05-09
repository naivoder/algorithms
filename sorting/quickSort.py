"""
this file implements a quick sort algorithm, a not-so-trivial approach to sorting by forming partitions around a "split point"
similar to merge sort, but instead of dividing the list equally in half, the split point is determined by setting a pointer on each side of the remaining list values and comparing each set of values as the indexes move towards a common center.
the first pair of index values that satisfy the criteria (left > right) becomes the split point and quick sort is recursively called on each new partition.
in the best case scenario quickSort works in O(nlogn) but without the space requirement demanded by mergeSort, in the worst case scenario (split points skewed heavily to left or right) run time becomes O(n^2).

"""
import random

def quick(collection, debug=False):
    helper(collection, 0, len(collection) - 1, debug=debug)
    return collection

def helper(collection, first, last, debug=False):
    if first < last:
        split_point = partition(collection, first, last, debug=debug)
        if debug:
            print("Left:", collection[first:split_point])
            print("Right:", collection[split_point:])
        helper(collection, first, split_point - 1, debug=debug)
        helper(collection, split_point + 1, last, debug=debug)

def partition(collection, first, last, debug=False):
    pivot = collection[first]
    left, right = first + 1, last
    finished = False
    while not finished:
        while left <= right and collection[left] <= pivot:
            left += 1
        while right >= left and collection[right] >= pivot:
            right -= 1
        if right < left:
            finished = True
        else:
            collection[left], collection[right] = collection[right], collection[left]
    collection[first], collection[right] = collection[right], collection[first]
    if debug:
        print("Split point: collection[%s] = %s" % (right, collection[right]))
    return right

if __name__=="__main__":
    test_data = [random.randint(1, 100) for index in range(10)]
    print("###---Quick Sort---###")
    print("Unsorted Data:", test_data)
    print("Sorted Data:", quick(test_data, debug=True))
