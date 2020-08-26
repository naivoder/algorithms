"""
this file implements a simple, one line solution to determine whether or not a given string is a palindrome
this algorithm uses O(n) time and O(1) space complexity by simultaneously traversing the string back to front
odd lengths are handled by ignoring the central term

"""

def is_palindrome(word, debug=False):
    if debug:
        print('Given word:', word)
        [print('->', word[i], word[~i]) for i in range(len(word) // 2)]
    return all(word[i] == word[~i] for i in range(len(word) // 2))

if __name__=='__main__':
    print('###---Is it a Palindrome?---###')
    test_words = ['madam', 'radar', 'anna', 'pip', 'lol', 'thanks', 'infer', 'nope', 'sit', 'car']
    results = [is_palindrome(word, debug=True) for word in test_words]
    print('Results:', results)