"""
this file implements an algorithm that returns a random subset of size 'k' from a given array of distinct elements
all subsets should be equally likely, and the result should be returned in the input array itself

a brute force approach would be to enumerate every possible combination of 'k' elements from the array and choose one at random

a more elegant approach is to generate a random number % size(array) and swap with array[i] for i in range(k)
in this way the random subset is collected at the beginning of the array with O(1) additional space and O(k) time, where k = number of randomly generated numbers

"""
import random

def random_sample(array: list, size: int) -> list:
    for i in range(size):
        # generate random index in [i, len(array) - 1]
        rand = random.randint(i, len(array) - 1)
        array[i], array[rand] = array[rand], array[i]
    return array[:size]

if __name__=="__main__":
    print("###---Random Subset---###")
    test_data = [random.randint(1, 30) for i in range(10)]
    print("Array:", test_data)
    print("Subset:", random_sample(test_data, size=4))
