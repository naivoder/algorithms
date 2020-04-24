"""
this file implements an algorithm to evaluate any postfix expression

"""
from stack import Stack

operators = '*/+-'; pars = '()'

def getExpression():
    postfixExpression = input("What expression would you like to evaluate? ")
    return postFixExpression

def evaluate(postfixExpression=None, debug=False):

    if postfixExpression is None:
        postfixExpression = getExpression()

    numberStack = Stack()
    postfixExpression = [char for char in postfixExpression.split(' ')]

    postfixString = ''.join(postfixExpression)

    for char in postfixExpression:

        if char.isdigit():
            numberStack.push(int(char))
            if debug:
                print("\x1b[0;33;40m" + "\nNumber Stack:" + "\x1b[0m", numberStack.show())

        elif char in operators:

            if char is '*':
                result = numberStack.pull() * numberStack.pull()
                if debug:
                    print("\x1b[0;33;40m" + "\nNumber Stack:" + "\x1b[0m", numberStack.show())

            elif char is '/':
                result = numberStack.pull() / numberStack.pull()
                if debug:
                    print("\x1b[0;33;40m" + "\nNumber Stack:" + "\x1b[0m", numberStack.show())

            elif char is '+':
                result = numberStack.pull() + numberStack.pull()
                if debug:
                    print("\x1b[0;33;40m" + "\nNumber Stack:" + "\x1b[0m", numberStack.show())

            else:
                result = numberStack.pull() - numberStack.pull()
                if debug:
                    print("\x1b[0;33;40m" + "\nNumber Stack:" + "\x1b[0m", numberStack.show())

            numberStack.push(result)
            if debug:
                print("\x1b[0;33;40m" + "\nNumber Stack:" + "\x1b[0m", numberStack.show())

    print("\nExpression:", postfixString)

    return numberStack.pull()

if __name__=="__main__":
    print("\nSolution:", evaluate('4 5 6 * +', debug=True))
    print("\nSolution:", evaluate('3 2 + 7 8 + /'))
    print("\nSolution:", evaluate(debug=True))
