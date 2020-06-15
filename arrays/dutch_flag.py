"""
this file implements an algorithm to solve the 'dutch national flag' problem, in essence a modification of the quick sort algorithm that reduces runtimes and call stacks in cases where there are large numbers of duplicates

the algorithm works by creating three partitions, instead of the usual two, around a 'pivot' to account for values equal to the pivot

this file does not finish the sort, it is for comprehension only, and returns the given array sorted into groups of smaller, equal to, and larger than the stated pivot value

"""

red, white, blue = range(3)

# this version uses O(1) additional space, but time complexity of O(n^2)
def dutch_flag_naive(pivot_index:int, array:list) -> list:
    pivot = array[pivot_index]
    # first pass collects values smaller than pivot
    for i in range(len(array)):
        # find a smaller element
        for j in range(i+1, len(array)):
            if array[j] < pivot:
                array[i], array[j] = array[j], array[i]
                break
    # second pass collects values larger than pivot
    for i in reversed(range(len(array))):
        # find larger element
        # stop when element < pivot
        for j in reversed(range(i)):
            if array[j] > pivot:
                array[i], array[j] = array[j], array[i]
                break
    return array

# this version improves upon the time complexity by performing only one pass
def dutch_flag_improved(pivot_index:int, array:list) -> list:
    pivot = array[pivot_index]
    pointer = 0
    # collect all elements smaller than pivot
    for i in range(len(array)):
        if array[i] < pivot:
            array[i], array[pointer] = array[pointer], array[i]
            pointer += 1
    pointer = len(array) - 1
    # collect all elements larger than pivot
    for i in reversed(range(len(array))):
        if array[i] > pivot:
            array[i], array[pointer] = array[pointer], array[i]
            pointer -= 1
    return array

# this version improves upon the runtime
# keeps track of four collections via three indexes:
# smaller than, equal to, unclassified (items not yet sorted), larger than
def dutch_flag(pivot_index:int, array:list) -> list:
    pivot = array[pivot_index]
    smaller, equal, larger = 0, 0, len(array) - 1
    while equal < larger:
        # array[equal] = next element to be sorted
        if array[equal] < pivot:
            array[smaller], array[equal] = array[equal], array[smaller]
            smaller, equal = smaller + 1, equal + 1
        elif array[equal] == pivot:
            equal += 1
        else:
            array[equal], array[larger] = array[larger], array[equal]
            larger -= 1
    return array


if __name__=="__main__":
    test_data = [1, 8, 5, 3, 8, 3, 6, 4, 9, 3]
    # pivot = 3
    # print("Naive:", dutch_flag_naive(3, test_data))
    # print("Improved:", dutch_flag_improved(3, test_data))
    print("Dutch Flag:", dutch_flag(3, test_data))
