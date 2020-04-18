"""
this file uses a Stack to determine whether parenthesis in an expression are balanced

"""
from stack import Stack

def pChecker(expression):
    pStack = Stack()
    for char in expression:
        if char == "(":
            pStack.push(char)
        if char == ")":
            try:
                pStack.pull()
            except:
                print("This expression has unbalanced parenthesis!")
                return False
    if pStack.isEmpty():
        print("This expression is perfectly balanced!")
        return True
    else:
        print("This expression has unbalanced parenthesis!")
        return False

if __name__=="__main__":
    goodEquation = '(()(()()))'
    print("Test:", goodEquation)
    pChecker(goodEquation)

    badEquation = '(()()(()()'
    print("Test:", badEquation)
    pChecker(badEquation)

    reallyBadEquation = ')'
    print("Test:", reallyBadEquation)
    pChecker(reallyBadEquation)
