"""
this file implements an algorithm to generate a random number from a given set of n numbers and corresponding p probabilities summing to 1.
'this problem formalizes the generation of inter-arrival times for a server load test' - EPI

this is accomplished by defining the interval pairs, generating a random number, and testing for the interval pair it falls between
since the array of interval pairs is sorted, binary search finds the interval in O(logn) time

"""

import itertools
from bisect import bisect
from random import random, randint

def nonuniform_generator(array, probabilities):
    # group probabilities into intervals
    bins = list(itertools.accumulate(probabilities))
    select = bisect(bins, random())
    return array[select]

if __name__=="__main__":
    test_data = [i for i in range(10)]
    test_probs = [random() for i in range(10)]
    denom = sum(test_probs)
    test_probs = [prob/denom for prob in test_probs]
    print("###---Nonuniform Random Number Generator---###")
    print("Array:\n", test_data)
    print("Probability Distribution:\n", test_probs)
    print("Random Selection:\n", nonuniform_generator(test_data, test_probs))