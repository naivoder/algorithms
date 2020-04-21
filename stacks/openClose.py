"""
this file extends the parenthesis balance checker from parenthesis.py to work with all nesting symbols

"""

from stack import Stack

nesting = ['(', '[', '{', ')', ']', '}']

def isBalanced(expression):
    eStack = Stack()
    for char in expression:
        if char in '([{':
            eStack.push(char)
        if char in ')]}':
            open = eStack.peek()
            if nesting[nesting.index(open) + 3] is char:
                eStack.pull()
            else:
                print("This expression is unbalanced!")
                return False
    if eStack.isEmpty():
        print("This expression is perfectly balanced!")
        return True
    else:
        print("This expression is unbalanced!")
        return False

if __name__=="__main__":
    goodEquation = '{{([][])}()}'
    print("Test:", goodEquation)
    isBalanced(goodEquation)

    goodEquation = '[][][](){}'
    print("Test:", goodEquation)
    isBalanced(goodEquation)

    badEquation = '[{()]'
    print("Test:", badEquation)
    isBalanced(badEquation)

    badEquation = '((()]))'
    print("Test:", badEquation)
    isBalanced(badEquation)
