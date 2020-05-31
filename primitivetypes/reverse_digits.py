"""
this file implements an algorithm to reverse the digits of a given integer

the brute force approach would be to convert the number to a string and traverse it in reverse
a more elegant solution is to realize that for any input 'k', if k > 0:
-> the first digit of the result = 'k' % 10, and the remaining digits are reverse('k'/10) recursively

"""
import random

def reverse(word):
    reversed, absolute = 0, abs(word)
    while absolute:
        reversed = (reversed * 10) + (absolute %  10)
        absolute //= 10
    return reversed if word > 0 else -(reversed)

if __name__=="__main__":
    test_inputs = [random.randint(100, 10000) for num in range(10)]
    print("###---Reverse Number---###")
    for input in test_inputs:
        print("%5s reversed = %5s" % (input, reverse(input)))
        
