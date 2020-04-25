"""
this file implements a "queue" abstract data type

"""

class Queue:

    def __init__(self):
        self.content = []

    def __str__(self):
        return str(self.content)

    def isEmpty(self):
        return len(self.content) == 0

    def push(self, item):
        self.content.insert(0, item)

    def pull(self):
        return self.content.pop()

    def peek(self):
        return self.content[-1]

    def count(self):
        return len(self.content)

    def print(self):
        print("The queue: ", end="")
        for item in self.content:
            print(item, end=" ")
        print("")

    def show(self):
        try:
            qString = ' '.join(self.content)
            print(qString)
        except:
            print("\nThis command is for string queues only!")
            yes = input("Try self.print()? (y/n) ")
            if yes is 'y':
                self.print()
            else:
                print("")

class ReverseQueue(Queue):

    def push(self, item):
        self.content.append(item)

    def pull(self):
        return self.content.pop(0)

    def peek(self):
        return self.content[0]

class StackQueue(Queue):

    def push(self, item):
        self.content.append(item)

    def pull(self):
        return self.content.pop()

    def peek(self):
        return self.content[0]

if __name__=="__main__":

    print("--FORWARD QUEUE--")
    queue = Queue()

    if queue.isEmpty():
        print("The queue is empty!")

    queue.push(3261990)
    queue.push('puppy dog')
    print("The next item in the queue is '%s'" % queue.peek())

    queue.push(False)
    print("The queue has %d items" % queue.count())
    queue.print()
    queue.show()

    queue.pull(); queue.pull()
    print("The next item in the queue is '%s'" % queue.peek())

    print("\n--REVERSE QUEUE--")
    queue = ReverseQueue()

    if queue.isEmpty():
        print("The queue is empty!")

    queue.push(3261990)
    queue.push('puppy dog')
    print("The next item in the queue is '%s'" % queue.peek())

    queue.push(False)
    print("The queue has %d items" % queue.count())

    queue.pull(); queue.pull()
    print("The next item in the queue is '%s'" % queue.peek())
