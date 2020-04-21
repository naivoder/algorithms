"""
this file implements a "queue" abstract data type

"""

class Queue:

    def __init__(self):
        self.content = []

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

    def show(self):
        qString = ''.join(self.content)
        return qString

class ReverseQueue(Queue):

    def push(self, item):
        self.content.append(item)

    def pull(self):
        return self.content.pop(0)

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
