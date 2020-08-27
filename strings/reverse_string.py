"""
this file implements a single line solution to reverse a string
python at its finest!

"""

def reverse_string(word):
    return ''.join(list(word)[::-1])

if __name__=='__main__':
    print('###---Reverse String---###')
    test_words = ['apple', 'moose', 'corvette', 'nap']
    [print(word, '-->', reverse_string(word)) for word in test_words]