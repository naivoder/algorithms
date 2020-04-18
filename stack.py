"""
this file contains an implementation of a Stack class, adapted from M&R

"""

class Stack:

    def __init__(self):
        self.content = []

    def isEmpty(self):
        return len(self.content) == 0

    def push(self, item):
        self.content.append(item)

    def pull(self):
        return self.content.pop()

    def peek(self):
        return self.content[-1]

    def count(self):
        return len(self.content)

    def show(self):
        reverse = ''
        while self.content:
            reverse += str(self.pull())
        return reverse


class BadStack(Stack):

    def push(self, item):
        self.content.insert(0, item)

    def pull(self):
        return self.content.pop(0)

    def peek(self):
        return self.content[0]

if __name__=="__main__":

    print("--GOOD STACK--")
    stack = Stack()

    if stack.isEmpty():
        print("The stack is empty!")

    stack.push(3261990)
    stack.push('puppy dog')
    print("The top item in the stack is '%s'" % stack.peek())

    stack.push(False)
    print("The stack has %d items" % stack.count())

    stack.pull(); stack.pull()
    print("The top item in the stack is '%s'" % stack.peek())

    print("\n--BAD STACK--")
    stack = BadStack()

    if stack.isEmpty():
        print("The stack is empty!")

    stack.push(3261990)
    stack.push('puppy dog')
    print("The top item in the stack is '%s'" % stack.peek())

    stack.push(False)
    print("The stack has %d items" % stack.count())

    stack.pull(); stack.pull()
    print("The top item in the stack is '%s'" % stack.peek())
