"""
this file implements and algorithm to convert any infix expression to postfix, optional debugging flag is included to display intermediate steps in terminal

"""
from stack import Stack

# operator tokens = '* / + - ( )'
# operand tokens = A, B, C, D ...

operators = '*/+-()'
leftParenthesis = '('; rightParenthesis = ')'

def compare(operatorA, operatorB):
    if operators.index(operatorA) <= operators.index(operatorB):
        return False
    return True

def convertPostfix(infixExpression=None, debug=False):

    operatorStack = Stack()
    postfixExpression = []

    if infixExpression is None:
        infixExpression = input("What expression would you like to convert? ")
    infixExpression = [char for char in infixExpression.split(' ')]
    if debug:
        print("\x1b[0;34;40m" + "###---DEBUGGING---###" + "\x1b[0m")
        print("\x1b[0;31;40m" + "\nInfix Expression:" + "\x1b[0m", infixExpression)


    for char in infixExpression:

        if char.isalpha():
            postfixExpression.append(char)
            if debug:
                print("\x1b[0;35;40m" + "\nPostfix:" + "\x1b[0m", postfixExpression)

        elif char is leftParenthesis:
            operatorStack.push(char)
            if debug:
                print("\x1b[0;33;40m" + "\nOpStack:" + "\x1b[0m", operatorStack.show())

        elif char is rightParenthesis:

            if not operatorStack.isEmpty():
                nextOperator = operatorStack.pull()

                while nextOperator is not leftParenthesis:
                    postfixExpression.append(nextOperator)
                    if debug:
                        print("\x1b[0;35;40m" + "\nPostfix:" + "\x1b[0m", postfixExpression)
                    nextOperator = operatorStack.pull()


        elif char in operators:

            if operatorStack.isEmpty():
                operatorStack.push(char)
                if debug:
                    print("\x1b[0;33;40m" + "\nOpStack:" + "\x1b[0m", operatorStack.show())
            else:
                precedence = True

                while precedence:
                    if compare(char, operatorStack.peek()):
                        nextOperator = str(operatorStack.pull())
                        postfixExpression.append(nextOperator)
                        if debug:
                            print("\x1b[0;35;40m" + "\nPostfix:" + "\x1b[0m", postfixExpression)
                            print("\x1b[0;33;40m" + "\nOpStack:" + "\x1b[0m", operatorStack.show())
                        if operatorStack.isEmpty():
                            precedence = False
                            operatorStack.push(char)

                    else:
                        precedence = False
                        operatorStack.push(char)
                        if debug:
                            print("\x1b[0;33;40m" + "\nOpStack:" + "\x1b[0m", operatorStack.show())

        else:
            raise ValueError("The expression has invalid characters, please try again with a valid expression!")

    while not operatorStack.isEmpty():
        nextOperator = str(operatorStack.pull())
        postfixExpression.append(nextOperator)

    postfixString = ''.join(postfixExpression)
    infixString = ''.join(infixExpression)

    print("\nThe infix expression was:", infixString)
    print("The equivalent postfix expression is:", postfixString)

if __name__=="__main__":
    convertPostfix('A + ( B * C )', debug=True)
    convertPostfix('( A + B ) * ( C + D )')
    convertPostfix('A + B / C')
    convertPostfix('( A + B ) * C')
