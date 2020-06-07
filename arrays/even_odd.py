"""
this file implements an algorithm that takens in an array of integer numbers and outputs an array in which all even numbers are presented before all odd numbers
the method is to divide the array into "even", "unsorted" and "odd" partitions, with the even and odd partitions initially being empty

the time complexity is O(n), where n = size of the array
the space complexity used here is O(1)

"""
import random

def even_odd(array):
    # initial position of even/odd
    even_pointer, odd_pointer = 0, len(array) - 1
    while even_pointer < odd_pointer:
        # if first number is even, move even pointer to next index
        if array[even_pointer] % 2 == 0:
            even_pointer += 1
        # swap first and last positions, move odd pointer to next index
        else:
            array[even_pointer], array[odd_pointer] = array[odd_pointer], array[even_pointer]
            odd_pointer -= 1
    return array

if __name__=="__main__":
    test_array = [random.randint(1, 1000) for num in range(10)]
    print("###---Even/Odd Sort---###")
    print("Unsorted:", test_array)
    print("Sorted:", even_odd(test_array))
