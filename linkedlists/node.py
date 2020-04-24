"""
this file implements a Node datatype, which holds two pieces of information relevant to the implemenation of a linked list: the list item itself, and a reference to the next node

note: pointer initialized with None indicates that there is no "next" node

"""
class Node:

    def __init__(self, data):
        self.object = data
        self.pointer = None

    def __str__(self):
        return str((self.object, self.pointer))

    def content(self):
        return self.object

    def reference(self):
        return self.pointer

    def store(self, data):
        self.object = data

    def point(self, next):
        self.pointer = next

if __name__=="__main__":
    print("##---Testing Node Class---##")
    node = Node(0)
    node2 = Node(1)
    node.point(node2)
    print(node)
    node.store(1)
    print(node)
