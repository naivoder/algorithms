"""
this file implements an algorithm that takes in a sorted array and returns the number of elements after removing all duplicates

this process could be completed using a hash table with O(n) additional space, but this implementation performs the operation in O(n) time and O(1) space

"""

from random import randint

def delete_dups(array:list) -> int:
    # check for empty list
    if not array:
        return 0
    count = 1
    for index in range(1, len(array)):
        # if not a duplicate increase count, else move to next index
        if array[count - 1] != array[index]:
            array[count] = array[index]
            count += 1
    return count

if __name__=="__main__":
    test_array = [1, 1, 2, 2, 2, 3, 4, 5, 6, 7, 7, 7, 8, 8, 9]
    rand_array = sorted([randint(0, 9) for int in range(15)])
    print("###--Number of Elements After Removing Duplicates---###")
    print("Test array: %s" % test_array)
    print("Number of elements after removing duplicates:", delete_dups(test_array))
    print("Randomly generated array: %s" % rand_array)
    print("Number of elements after removing duplicates:", delete_dups(rand_array))
