"""
this file combines the functionality of convert2Postfix and evaluatePostfix, returning the result of the infix Expression

"""

from stack import Stack

operators = '*/+-()'
leftParenthesis = '('; rightParenthesis = ')'

def getExpression():
    infixExpression = input("What expression would you like to convert? ")
    return infixExpression

def compare(operatorA, operatorB):
    if operators.index(operatorA) <= operators.index(operatorB):
        return False
    return True

def convertToPostfix(infixExpression=None):

    operatorStack = Stack()
    postfixExpression = []

    if infixExpression is None:
        infixExpression = getExpression()

    print("Infix Expression:", infixExpression)
    infixExpression = [char for char in infixExpression.split(' ')]
    
    for char in infixExpression:

        if char.isdigit():
            postfixExpression.append(char)

        elif char is leftParenthesis:
            operatorStack.push(char)

        elif char is rightParenthesis:

            if not operatorStack.isEmpty():
                nextOperator = operatorStack.pull()

                while nextOperator is not leftParenthesis:
                    postfixExpression.append(nextOperator)
                    nextOperator = operatorStack.pull()

        elif char in operators:

            if operatorStack.isEmpty():
                operatorStack.push(char)

            else:
                precedence = True

                while precedence:
                    if compare(char, operatorStack.peek()):
                        nextOperator = str(operatorStack.pull())
                        postfixExpression.append(nextOperator)

                        if operatorStack.isEmpty():
                            precedence = False
                            operatorStack.push(char)

                    else:
                        precedence = False
                        operatorStack.push(char)

        else:
            raise ValueError("The expression has invalid characters, please try again with a valid expression!")

    while not operatorStack.isEmpty():
        nextOperator = str(operatorStack.pull())
        postfixExpression.append(nextOperator)

    postfixString = ' '.join(postfixExpression)
    print("Postfix Expression: ", postfixString)

    return postfixString

def evaluate(postfixExpression=None):

    numberStack = Stack()
    postfixExpression = [char for char in postfixExpression.split(' ')]

    postfixString = ''.join(postfixExpression)

    for char in postfixExpression:

        if char.isdigit():
            numberStack.push(int(char))

        elif char in operators:

            if char is '*':
                result = numberStack.pull() * numberStack.pull()

            elif char is '/':
                result = numberStack.pull() / numberStack.pull()

            elif char is '+':
                result = numberStack.pull() + numberStack.pull()

            else:
                b = numberStack.pull(); a = numberStack.pull()
                result = a - b

            numberStack.push(result)

    return numberStack.pull()

if __name__=="__main__":
    eq = convertToPostfix()
    result = evaluate(eq)
    print("Result:", result)
