"""
this file implements an algorithm by which one array is taken as input, and sorted so that a[0] <= a[1] >=  a[2] <= a[3] ...

simply sorting the array and interweaving the top and bottom halves would solve the problem in O(nlogn) time

sorting is not required to achieve the desired results, iterate through the array and swap:
---> a[i] > a[i+1] when i is even
---> a[i] < a[i+1] when i is odd
this method solves the problem in O(n) time

"""

from random import randint

def alternate(array:list) -> list:
    for i in range(len(array)):
        array[i:i+2] = sorted(array[i:i+2], reverse=bool(i%2))
    return array

if __name__=="__main__":
    test_data = [randint(0, 100) for num in range(10)]
    print("###---Alternate Array---###")
    print(alternate(test_data))
