"""
this file implements a simple, one line solution to determine whether or not a given string is a palindrome
this algorithm uses O(n) time and O(1) space complexity by simultaneously traversing the string back to front
odd lengths are handled by ignoring the central term

two more versions are included, including one which performs the loops explicitely and another version of the
pythonic solution that handles more potential cases (punctuation, capitalization, etc.)

"""

def is_palindrome(word, debug=False):
    if debug:
        print('Given word:', word)
        [print('->', word[i], word[~i]) for i in range(len(word) // 2)]
    return all(word[i] == word[~i] for i in range(len(word) // 2))

def is_palindrome_naive(word):
    i, j = 0, len(word) - 1
    while i < j:
        # skip non-alphanumeric characters
        while not word[i].isalnum():
            i += 1
        while not word[j].isalnum():
            j -= 1
        if word[i].lower() != word[j].lower():
            return False
        i, j = i + 1, j - 1
    return True

def is_palindrome_pythonic(word):
    return all(
        a == b for a, b in zip(map(str.lower, filter(str.isalnum, word)),
                               map(str.lower, filter(str.isalnum, reversed(word))))
    )

if __name__=='__main__':
    print('###---Is it a Palindrome?---###')
    test_words = ['madam', 'radar', 'anna', 'pip', 'lol', 'thanks', 'infer', 'nope', 'sit', 'car', 'Pip', 'lol!']
    results = [is_palindrome(word, debug=True) for word in test_words]
    print('One Line Results:', results)
    results = [is_palindrome_naive(word) for word in test_words]
    print('Naive Results:', results)
    results = [is_palindrome_pythonic(word) for word in test_words]
    print('Pythonic Results:', results)