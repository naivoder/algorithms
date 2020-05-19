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
    def _put(self, key, value, current):
        if key < current.key:
            if current.has_left_child():
                self._put(key, value, current.left_child)
            else:
                current.left_child = TreeNode(key, value, parent=current)
        else:
            if current.has_right_child():
                self._put(key, value, current.right_child)
            else:
                current.right_child = TreeNode(key, value, parent=current)

    # overload dict 'write' method
    def __setitem__(self, key, value):
        self.put(key, value)

    # call private recursive function until leaf or match
    def get(self, key):
        if self.root:
            node = self._get(key, self.root)
            # match
            if node:
                return node.payload
            # leaf
            else:
                return None
        # empty tree
        else:
            return None

    def _get(self, key, current):
        # leaf (dead end)
        if not current:
            return None
        # match found
        elif current.key == key:
            return current
        # search left or right branches
        elif current.key < key:
            return self._get(key, current.left_child)
        else:
            return self._get(key, current.right_child)

    # overload dict 'read' method
    def __getitem__(self, key):
        return self.get(key)

    # overload 'in' method
    def __contains__(self, key):
        return True if self._get(key, self.root) else False

    # find node to be deleted using private _get
    # --> if root must still perform value check
    def delete(self, key):
        if self.size > 1:
            dead_node = self._get(key, self.root)
            if dead_node:
                # call method to prune node from branch
                # must reattach any children!
                self.remove(dead_node)
                self.size -= 1
            else:
                raise KeyError('%s not found in search tree...' % key)
        # remember to confirm correct key...
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size -= 1
        else:
            raise KeyError('%s not found in search tree' % key)

    # overload 'del' method
    def __delitem__(self, key):
        self.delete(key)

    # handle three potential delete cases
    # 1) no children
    # 2) 1 child
    # 3) 2 children

    # reattach branch at removed node
    def splice_branch(self):
        # case 1
        if self.is_leaf():
            if self.is_left_child():
                self.parent.left_child = None
            else:
                self.parent.right_child = None
        # case 2
        elif self.has_any_children():
            if self.has_left_child():
                if self.is_left_child():
                    self.parent.left_child = self.left_child
                else:
                    self.parent.right_child = self.left_child
                self.left_child.parent = self.parent
            else:
                if self.is_left_child():
                    self.parent.left_child = self.right_child
                else:
                    self.parent.right_child = self.right_child

    # case 3
    def find_successor(self):
        chosen = None
        if self.has_right_child():
            chosen = self.right_child.find_minimum()
        else:
            if self.parent:
                if self.is_left_child():
                    chosen = self.parent
                else:
                    self.parent.right_child = None
                    chosen = self.parent.find_successor()
                    self.parent.right_child = self
        return chosen

    # find smallest value in branch
    def find_minimum(self):
        minimum = self
        while minimum.has_left_child():
            minimum = minimum.is_left_child
        return minimum

    # prune node from tree
    def remove(self, current):
        if current.is_leaf():
            # remove references from parent node
            if current == current.parent.left_child:
                current.parent.left_child = None
            else:
                current.parent.right_child = None
        elif current.has_both_children():
            successor = current.find_successor()
            successor.splice_branch()
            current.key = successor.key
            current.payload = successor.payload
        else:
            if current.has_left_child():
                # shift leaf up branch
                if current.is_left_child():
                    current.left_child.parent = current.parent
                    current.parent.left_child = current.left_child
                elif current.is_right_child():
                    current.left_child.parent = current.parent
                    current.parent.right_child = current.left_child
                else:
                    current.overwrite(current.left_child.key, current.left_child.payload, current.left_child.left_child, current.left_child.right_child)
            else:
                if current.is_left_child():
                    current.right_child.parent = current.parent
                    current.parent.left_child = current.right_child
                elif current.is_right_child():
                    current.right_child.parent = current.parent
                    current.parent.right_child = current.right_child
                else:
                    current.overwrite(current.right_child.key, current.right_child.payload, current.right_child.left_child, current.right_child.right_child)
    def inorder(self):
        if self.root.left_child:
            left = self.root.left_child
            left.inorder()
        print(self.root.payload)
        if self.root.right_child:
            right = self.root.right_child
            right.inorder()

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

    def overwrite(self, key, value, left, right):
        self.key = key
        self.payload = value
        self.left_child = left
        self.right_child = right
        if self.has_left_child():
            self.left_child.parent = self
        if self.has_right_child():
            self.right_child.parent = self

    def inorder(self):
        if self.left_child:
            left = self.left_child
            left.inorder()
        print(self.payload)
        if self.right_child:
            right = self.right_child
            right.inorder()


if __name__=="__main__":
    tree = BinarySearchTree()
    tree[3] = "could"
    tree[6] = "worse"
    tree[5] = "be"
    tree[4] = "always"
    tree[2] = "it"
    tree.inorder()
