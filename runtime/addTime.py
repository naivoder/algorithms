"""
this file benchmarks the recursive addition method against a traditional implementation

"""
import random
import timeit

numbers = [random.randint(0, 10000) for num in range(100)]

# non-recursive solution
def calcSum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

# recursive solution
def add(numbers=None):
    if len(numbers) == 1:
        return numbers[0]
    else:
        return numbers[0] + add(numbers[1:])

nonRecursive_Add = timeit.Timer("calcSum(numbers)","from __main__ import calcSum, numbers")
nonRecursive_Time = nonRecursive_Add.timeit()

recursive_Add = timeit.Timer("add(numbers)","from __main__ import add, numbers")
recursive_Time = recursive_Add.timeit()

print("Add method comparison:")
print("Non-Recursive = %8.5fs" % nonRecursive_Time)
print("Recursive = %8.5fs" % recursive_Time)
