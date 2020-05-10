"""
this file implements a deque abstract datatype
rear-------------------------------------front

"""

class Deque():

    def __init__(self):
        self.content = []

    def __str__(self):
        return ''.join(str(self.content))

    def __len__(self):
        return len(self.content)

    def __contains__(self, item):
        return True if item in self.content else False

    def isEmpty(self):
        return len(self.content) == 0

    def pushFront(self, item):
        self.content.append(item)

    def pushRear(self, item):
        self.content.insert(0, item)

    def pullFront(self):
        return self.content.pop()

    def pullRear(self):
        return self.content.pop(0)

    def peekFront(self):
        return self.content[-1]

    def peekRear(self):
        return self.content[0]

    def count(self):
        return len(self.content)


if __name__=="__main__":
    print("--DEQUE--")
    deque = Deque()
    deque.pushFront(999)
    deque.pushRear('blue')
    print("Deque:",deque)
    if 'blue' in deque:
        print("'Blue' is in the deque.")
    deque.pullFront()
    print("After pulling, the deque has length = %s" % len(deque))
    deque.pushRear(37)
    print("Items in deck:", deque.count())
    print("Deque:", deque)
    deque.pullRear()
    print("Items in deck:", deque.count())
    print("Deque:", deque)
