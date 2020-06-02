"""
this file implements an algorithm to determine whether a given integer is in fact a palindrome.

the brute force method would be to convert the input to a string and compare the first and last positions iteratively
this results in time and space complexity O(n)
an implementation of this approach can be found in the 'deques' directory, where a deque ADT is used to solve this problem

a more elegant method is to directly extract the LSB and MSB from an input, resulting in space complexity O(1)
the LSD of an integer 'x' is always = x % 10

the number of digits in an integer is equivalent to the log10(input), or n = (log10x) + 1
therefore MSD is = x / (10 ** n-1)

"""
import math

def palindrome(number:int, debug:bool=False) -> bool:
    # if the number is negative, it cannot be a palindrome (only one '-')
    if number < 0:
        return False
    if debug:
        print("Input:", number)
        print("Input type:", type(number))
    try:
        # this does not work due to single digit inputs...
        # number_of_digits = math.ceil(math.log10(number))
        number_of_digits = math.floor(math.log10(number)) + 1
    except ValueError:
        return True
    msd_mask = 10 ** (number_of_digits - 1)
    if debug:
        print("Number of digits in input:", number_of_digits)
        print("MSD Mask:", msd_mask)
    for i in range(number_of_digits // 2):
        if number // msd_mask != number % 10:
            return False
        # remove MSD
        number %= msd_mask
        # remove LSD
        number //= 10
        # reduce mask by 2 decimal places
        msd_mask //= 100
    return True

if __name__=="__main__":
    pos_test_data = [0, 1, 111, 2222, 3443, 555565555, 9000110009]
    neg_test_data = [10, 123, 938465, 5555555555556, 93817353480]
    print("###---Test for palindrome---###")
    for num in pos_test_data:
        print("%s = %s" % (num, palindrome(num, debug=True)))
    for num in neg_test_data:
        print("%s = %s" % (num, palindrome(num)))
