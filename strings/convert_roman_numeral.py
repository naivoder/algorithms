"""
this file implements an algorithm to convert a valid roman numeral string to its corresponding integer representation
the elegant solution is to traverse the string in reverse, subtracting if a numeral is found to be less than the next, else add

"""
from functools import reduce

def convert_numeral(numeral):
    convert = {'I' : 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    return reduce(
        lambda val, i: val + (-convert[numeral[i]] if convert[numeral[i]] < convert[numeral[i + 1]] else convert[numeral[i]]),
        reversed(range(len(numeral) - 1)),
        convert[numeral[-1]]
    )

if __name__=="__main__":
    print('###---Convert Roman Numeral to Integer---###')
    roman_numerals = ['LIX', 'XVI', 'IV']
    for rn in roman_numerals:
        print(rn, '->', convert_numeral(rn))