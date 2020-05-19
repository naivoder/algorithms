"""
this file implements a binary search tree using the node and reference approach, but adds an additional class to facilitate working with an empty tree via helper functions and explicit attributes
this was adapted from an exercise in Miller & Radnum

"""

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def __repr__(self):
        print(self.root)
        return self.root.__repr__()

    # method must check to see if root exists
    # --> if root exists, call private recursive function
    def put(self, key, value):
        if self.root:
            self._put(key, value, self.root)
        else:
            self.root = TreeNode(key, value)
        self.size += 1

    # if key < current --> search left tree
    # if key > current --> search right tree
    def _put(self, key, value, current_node):
        if key < current_node.key:
            if current_node.has_left_child():
                self._put(key, value, current_node.left_child)
            else:
                current_node.left_child = TreeNode(key, value, parent=current_node)
        else:
            if current_node.has_right_child():
                self._put(key, value, current_node.right_child)
            else:
                current_node.right_child = TreeNode(key, value, parent=current_node)

    def __setitem__(self, key, value):
        self.put(key, value)

class TreeNode:
    def __init__(self, key, value, left=None, right=None, parent=None):
        self.key = key
        self.payload = value
        self.left_child = left
        self.right_child = right
        self.parent = parent

    def has_left_child(self):
        return self.left_child

    def has_right_child(self):
        return self.right_child

    def is_left_child(self):
        return self.parent and self.parent.left_child == self

    def is_right_child(self):
        return self.parent and self.parent.right_child == self

    def is_root(self):
        return not self.parent

    def is_leaf(self):
        return not (self.right_child or self.left_child)

    def has_any_children(self):
        return self.right_child or self.left_child

    def has_both_children(self):
        return (self.right_child and self.left_child)

    def overwrite_node(self, key, value, left, right):
        self.key = key
        self.payload = value
        self.left_child = left
        self.right_child = right
        if self.has_left_child():
            self.left_child.parent = self
        if self.has_right_child():
            self.right_child.parent = self
