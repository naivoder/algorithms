"""
this file implements an Unordered List class, built as a collection of Nodes (defined in node.py)
the class must keep track of the first node, and the final node should always be "grounded"
my implementation of linked lists is based heavily on Miller & Radnum's excellent discussion in "Problem Solving with Algorithms and Data Structures"

"""
from node import Node

class UnorderedList:

    def __init__(self):
        self.head = [None, 0]

    def __str__(self):
        stuff = []
        step = self.head[0]
        while step != None:
            stuff.append(step.content())
            step = step.reference()
        return str(stuff)

    def empty(self):
        return self.head[0] == None

    def add(self, item):
        hold = Node(item)
        hold.point(self.head[0])
        self.head[0] = hold
        self.head[1] += 1

    def size(self):
        step = self.head[0]
        count = 0
        while step != None:
            count += 1
            step = step.reference()
        return count

    def length(self):
        count = self.head[1]
        return count

    def search(self, item):
        step = self.head[0]
        found = False
        while step != None and not found:
            if step.content() == item:
                found = True
            else:
                step = step.reference()
        return found

    # to remove a node, we assign the pointer from the preceding node to the reference of the node we wish to skip
    def delete(self, item):
        step = self.head[0]
        last = None
        found = False
        while not found:
            if step.content() == item:
                found = True
            else:
                last = step
                step = step.reference()

        if last == None:
            self.head[0] = step.reference()
        else:
            last.point(step.reference())
        self.head[1] -= 1

    def append(self, item):
        step = self.head[0]
        hold = Node(item)
        while step.reference() != None:
            step = step.reference()
        step.point(hold)
        self.head[1] += 1

if __name__=="__main__":
    print("##---UNORDERED LINKED LIST---###")
    list = UnorderedList()
    print("Linked List:", list)
    list.add(4)
    print("Adding 4")
    print("Linked List:", list)
    list.add(32)
    print("Adding 32")
    print("Linked List:", list)
    list.add(3)
    print("Adding 3")
    print("Linked List:", list)
    list.add(12)
    print("Adding 12")
    print("Linked List:", list)
    print("Number of items in list:", list.size())
    list.delete(4)
    print("Removing 4")
    print("Number of items in list:", list.size())
    print("Linked List:", list)
    list.append(15)
    print("Appending 15")
    print("Item '15' in list? ", list.search(15))
    print("Linked List:", list)
    print("Length of list:", list.length())
