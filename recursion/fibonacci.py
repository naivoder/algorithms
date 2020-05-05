"""
this file implements a recursive algorithm to compute the nth number of the fibonacci sequence
M&R start this algorithm from 0, however most implementations start the sequence from 1. I have chosen the latter, so that the resulting solutions match what would most commonly be expected.

"""
def getInt():
    print("Incorrect input, please enter a positive integer...")
    n = input("Which number in the fibonacci sequence should be calculated? ")
    try:
        n = int(n)
    except:
        n = getInt()
    if n < 0 or n.isfloat() or n.isalpha():
        getInt()
    return n

def fibonacci(n=None):
    try:
        n = int(n)
    except:
        n = getInt()
    if n is 1:
        return 1
    elif n is 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

if __name__=="__main__":
    print("Fibonacci Sequencer")
    print("___________________")
    n = input("Which number in the fibonacci sequence should be calculated? ")
    try:
        int(n)
    except:
        n = getInt()
    nth = fibonacci(n)
    print("The number at position %s is: %s" % (n, nth))
