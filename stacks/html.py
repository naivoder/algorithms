"""
this file uses the stack abstract data type to check that an html expression is balanced
to simplify the problem slightly I have created a list of html tags that require a "closing" partner, however this list is NOT exhaustive and this algorithm would likely not be sufficient to ensure code was production quality (I'd recommend using a staging site when doing web development anyways...)
this algorithm will check for balanced braces < > as well as ensuring that the required tags are balanced.

"""
from stack import Stack

balanced = "This HTML document is balanced!"
unbalanced = "This HTML document is unbalanced..."
requireClose = ['html', 'head', 'title', 'body', 'a', 'p', 'div']

def htmlChecker(document, debug=False):

    words = {}

    expression = ''
    try:
        with open(document) as readfile:
            for line in readfile:
                expression += line.rstrip()
    except:
        print("I couldn't find that document...")
        print("Check the file path or try another!")
        return False

    stack = Stack()
    flag = False
    word = ''

    for char in expression:
        if char is '<':
            stack.push(char)
            flag = True
            if debug:
                print(stack)

        if flag is True and char is not '<' and char is not '>' and char is not '/':
            word += char
            if debug:
                print("word", word)

        if char is '>':
            if word in words:
                words[word] += 1
            else:
                words[word] = 1
            word = ''

            flag = False
            try:
                match = stack.pull()
            except:
                print(unbalanced)
                return False

    if debug:
        print("Word dictionary:", words)

    if not stack.isEmpty:
        print(unbalanced)
        return False

    for word in words:
        if word in requireClose:
            if words[word] % 2 != 0:
                print(unbalanced)
                return False

    print(balanced)
    return True


def getDocument():
    path = input("Please enter the path to the document you want to check: ")
    return path

if __name__=="__main__":
    doc = getDocument()
    truth = htmlChecker(doc, debug=False)
