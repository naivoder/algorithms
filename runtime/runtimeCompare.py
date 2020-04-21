"""
Author: Cameron Redovian

This program consists of two algorithms to identify the minimum value in a list (presumably of numbers), to demonstrate runtime difference between O(n) and O(n^2).

"""

import time

def findMin_n(numberList):
  start = time.time()
  minimum = numberList[0]
  for number in numberList:
    if number < minimum:
      minimum = number
  end = time.time()
  return minimum, end-start

def findMin_n2(numberList):
  start = time.time()
  for i in range(len(numberList)):
    for j in range(1, len(numberList)):
      if numberList[j] < numberList[i]:
        hold = numberList[i]
        numberList[i] = numberList[j]
        numberList[j] = hold
  minimum = numberList[0]
  end = time.time()
  return minimum, end-start

if __name__=="__main__":
  print("O(n): Min = %d, Time = %.7fs" % (findMin_n([4, 2, 6, 8, 3])))
  print("O(n2): Min = %d, Time = %.7f" % (findMin_n2([4, 2, 6, 8, 3])))

 
