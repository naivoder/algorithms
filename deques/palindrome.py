"""
this file uses the deque datatype from deque.py to check for palidromes

"""
from deque import Deque

def palindrome(string):

    letterDeque = Deque()

    for char in string:
        letterDeque.pushFront(char)
    print("Deque:", letterDeque)

    equal = True

    while equal and not letterDeque.isEmpty():
        first = letterDeque.pullFront()

        try:
            last = letterDeque.pullRear()
        except:
            break

        if first != last:
            equal = False

    return equal

if __name__=="__main__":
    print("Checking for palindromes!")
    test = input("What word should be checked? ")
    result = palindrome(test)
    if result:
        print("%s is a palindrome!" % (test))
    else:
        print("Sorry, %s is not a palindrome!" % (test))
