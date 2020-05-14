"""
this file implements a (min) binary heap ADT, used to implement a priority queue, in which enqueing and dequeing items is completed in O(logn) time. to guarantee logarithmic performance the binary tree is kept balanced (roughly same number of nodes on left and right subtrees) with the exception of the bottom level which is filled from left to right
heap order property: for every node (x) with parent (p) the key in (p) is smaller than or equal to the key in (x)
compute the parent of any node with floor division // 2 (parent of node 5 is node 2...)

"""

class BinaryHeap:

    def __init__(self):
        self.content = [0]
        self.size = 0

    # smallest value rises up to the top of heap
    def percolate(self, index):
        while index // 2 > 0:
            if self.content[index] < self.content[index // 2]:
                self.content[index], self.content[index // 2] = self.content[index // 2], self.content[index]
            index //= 2

    def push(self, obj):
        self.content.append(obj)
        self.size += 1
        self.percolate(self.size)

    def get_min(self, index):
        # if there is only one child no need to compare
        if index * 2 + 1 > self.size:
            return index * 2
        # return smallest of child nodes
        return (index * 2) if self.content[index * 2] < self.content[index * 2 + 1] else (index * 2 + 1)

    # largest value sinks to the bottom of heap
    def distill(self, index):
        while (index * 2) <= self.size:
            min_child = self.get_min(index)
            if self.content[index] > self.content[min_child]:
                self.content[index], self.content[min_child] = self.content[min_child], self.content[index]
            index = min_child

    def del_min(self):
        trash = self.content[1]
        # place largest value in root position
        self.content[1] = self.content[self.size]
        self.size -= 1
        # remove largest value from bottom of heap (duplicate)
        self.content.pop()
        # filter item (large value) back to bottom of heap
        self.distill(1)

    def build_heap(self, collection):
        index = len(collection) // 2
        self.size = len(collection)
        self.content = [0] + collection[:]
        while (index > 0):
            self.distill(index)
            index -= 1

    def __str__(self):
        string = "Heap: "
        return string + str(self.content)

if __name__=="__main__":
    heap = BinaryHeap()
    heap.build_heap([9, 5, 7, 3, 1, 5])
    print(heap)
    print("Deleting minimum value...")
    heap.del_min()
    print(heap)
    print("Adding new value...")
    heap.push(12)
    print(heap)
