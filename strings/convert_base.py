"""
this file implements an algorithm to that converts a given number and base into the desired base

"""

from string import hexdigits
from functools import reduce

def as_decimal(number, base, debug=False):
    num_list = list(number)[::-1]
    if debug:
        print('Number list:', num_list)
        print('Given base:', base)
    decimal = 0
    for i in range(len(num_list)):
        decimal += int(num_list[i]) * base ** i
    return decimal

def convert_base(number, from_base, to_base, debug=False):
    def construct_from_base(as_integer, to_base):
        return ('' if as_integer == 0 else construct_from_base(as_integer // to_base, to_base) + hexdigits[as_integer % to_base].upper())
    if debug:
        print(as_decimal, number, from_base)
    is_negative = number[0] == '-'
    as_integer = reduce(lambda x, c: x * from_base + hexdigits.index(c.lower()), number[is_negative:], 0)
    return ('-' if is_negative else '') + ('0' if as_integer == 0 else construct_from_base(as_integer, to_base))

if __name__=='__main__':
    print('###---Base-to-Base Conversion---###')
    test_data = ('615', 7)
    target_bases = list(range(2, 11))
    for base in target_bases:
        print('Given base: %s\tGiven Number: %s' % (test_data[1], test_data[0]))
        print('Target base: %s\tSolution: %s' % (base, convert_base(*test_data, base)))