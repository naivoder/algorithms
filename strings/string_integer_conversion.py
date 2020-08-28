"""
this file implements algorithms that convert a given string to an integer or vice versa
the string_to_int method (taken from EPI - Aziz, Lee, Prakash) makes use of the 'functools' library for an especially pythonic solution

"""

from functools import reduce

def int_to_string(number, debug=False):
    # set flag for negative, will combine with final result
    is_negative = True if number < 0 else False
    # take abs value for calculation
    if is_negative:
        number = -number

    word = []
    while True:
        # build string in reverse to save computation time
        # inserting obj at front of list is slow...
        # appending obj to end of list is fast
        word.append(chr(ord('0') + number % 10))
        number //= 10
        if debug:
            print('Word:', ''.join(word))
            print('Number:', number)
        if number == 0:
            break

    # add negative sign if required, reverse string for result
    return ('-' if is_negative else '') + ''.join(reversed(word))

def string_to_int(word):
    # word[word[0] in '-+':] === "for letter in word"
    return (-1 if word[0] == '-' else 1) * reduce(
        lambda run_sum, letter: run_sum * 10 + int(letter), word[word[0] in '-+':], 0
    )

def convert(obj):
    if isinstance(obj, int):
        return int_to_string(obj)
    elif isinstance(obj, str):
       return string_to_int(obj)
    else:
        print('Sorry, not a valid object type!')
        print('Try again with an integer or string...')

if __name__=='__main__':
    print('###---Converting Between Strings and Integers---###')
    test_number = -12345
    test_word = '-12345'
    print('As string: "%s"' % convert(test_number))
    print('As number:', convert(test_word))