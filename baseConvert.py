"""
this file uses a stack to convert integer to any number base.

"""
from stack import Stack

digits = "0123456789ABCDEF"

def divByBase(integer, base):
    remainder = integer % base
    if remainder:
        return (integer // base, remainder)
    else:
        return (integer // base, 0)

def convertBase(integer, base):
    baseStack = Stack()
    while integer >= 1:
        integer, remainder = divByBase(integer, base)
        baseStack.push(remainder)
    decoded = ""
    while not baseStack.isEmpty():
        decoded += digits[baseStack.pull()]
    return decoded

if __name__=="__main__":
    print("--Any Base --")
    integer = int(input("What number should be converted? "))
    base = int(input("What base do you want to convert to? "))
    result = convertBase(integer, base)
    print("%s in base %s is: %s" % (integer, base, result))
