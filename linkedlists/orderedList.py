"""
this file implements an ordered linked list abstract data type
assume that data has predefined comparable relationship
modified from M&R

"""
from node import Node

ground = None

class OrderedList:

    def __init__(self):
        self.head = [ground, 0]

    def __str__(self):
        stuff = []
        step = self.head[0]
        while step != ground:
            stuff.append(step.content())
            step = step.reference()
        return str(stuff)

    def search(self, item):
        step = self.head[0]
        found = False
        finished = False
        while step != ground and not found and not finished:
            if step.content() == item:
                found = True
            else:
                if step.content() > item:
                    finished = True
                else:
                    step = step.reference()
        return found

    def add(self, item):
        hold = Node(item)
        step = self.head[0]
        last = ground
        finished = False
        while step != ground and not finished:
            if step.content() > item:
                finished = True
            else:
                last = step
                step = step.reference()
        if last == ground:
            hold.point(ground)
            self.head[0] = hold
        else:
            hold.point(step)
            last.point(hold)
        self.head[1] += 1

    def remove(self, item):
        step = self.head[0]
        last = None
        found = False
        while not found:
            if step.content() == item:
                found = True
            else:
                last = step
                step = step.reference()
        if last == ground:
            self.head[0] = step.reference()
        else:
            last.point(step.reference())
        self.head[1] -= 1

    def isEmpty(self):
        return self.head[0] == ground

    def size(self):
        step = self.head[0]
        count = 0
        while step != ground:
            count += 1
            step = step.reference()
        return count

    def index(self, item):
        step = self.head[0]
        found = False
        count = 0
        while not found:
            if step.content() == item:
                found = True
            else:
                count += 1
                step = step.reference()
        return count

    def pop(self, pos=None):
        step = self.head[0]
        last = None
        if pos is None:
            while step.reference() != ground:
                last = step
                step = step.reference()
            if last == None:
                self.head[0] = step.reference()
            else:
                last.point(step.reference())
        else:
            count = 0
            while count < pos:
                last = step
                step = step.reference()
            if last == None:
                self.head[0] = step.reference()
            else:
                last.point(step.reference())
        self.head[1] -= 1

    def length(self):
        return self.head[1]

if __name__=="__main__":
    print("##---ORDERED LINKED LIST---##")
    list = OrderedList();
    list.add(1); list.add(9); list.add(16)
    print("Linked List:", list)
    list.add(4)
    print("Adding 4")
    print("Linked List:", list)
    list.add(32)
    print("Adding 32")
    print("Linked List:", list)
    print("Index of 9? ", list.index(9))
    print("Number of items in list:", list.size())
    print("Linked List:", list)
    list.remove(4)
    print("Removing 4")
    print("Linked List:", list)
    list.add(3)
    print("Adding 3")
    print("Linked List:", list)
    list.add(12)
    print("Adding 12")
    print("Linked List:", list)
    print("Number of items in list:", list.size())
    print("Linked List:", list)
    print("Item '1' in list? ", list.search(1))
    list.pop()
    print("Pop from end...")
    print("Linked List:", list)
    list.pop(0)
    print("Pop from 0...")
    print("Linked List:", list)
    print("Length of list:", list.length())
