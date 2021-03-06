"""
this file uses a stack to convert integer to binary.

"""
from stack import Stack

def divByTwo(integer):
    if integer % 2:
        return (integer // 2, 1)
    else:
        return (integer // 2, 0)

def convert(integer):
    binaryStack = Stack()
    while integer >= 1:
        integer, remainder = divByTwo(integer)
        binaryStack.push(remainder)
    return binaryStack.show()

if __name__=="__main__":
    print("--Binary--")
    integer = int(input("What number should be converted? "))
    binary = convert(integer)
    print("%s in binary is: %s" % (integer, binary))
