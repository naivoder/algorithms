"""
this file uses the custom Stack class to reverse a given string

"""

from stack import Stack

def reverseString(string):

    reversed = ''
    stringStack = Stack()

    for char in string:
        stringStack.push(char)

    while not stringStack.isEmpty():
        reversed += stringStack.pull()

    return reversed

if __name__=="__main__":
    testString = "Atlanta"
    backwards = reverseString(testString)
    print("%s in reverse is: %s" % (testString, backwards))
