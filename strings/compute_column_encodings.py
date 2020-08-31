"""
this file implements an algorithm to compute a given spreadsheet column encoding to its corresponding decimal form
the key to this problem is treat the the column encodings as a base 26 number where "A" = 1

"""
from functools import reduce

def convert_encoding(column_code):
    return reduce(
        lambda total, char: total * 26 + ord(char) - ord('A') + 1, column_code, 0
    )

if __name__=="__main__":
    test_cols = ['A', 'B', 'Y', 'Z', 'AA', 'AB', 'ZY', 'ZZ', 'M', 'BZ', 'CC']
    print('###---Convert Column Encodings---###')
    [print('Column Code: %s\t\tColumn Number: %s' % (col, convert_encoding(col))) for col in test_cols]