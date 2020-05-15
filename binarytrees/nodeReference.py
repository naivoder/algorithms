"""
this file implements a binary tree using a Node & Reference representation. similar to a linked list, this class uses a root value as well as left and right branches which each become references to a new binary tree object.

"""

class BinaryTree:
    # constructor expects root argument, can be any object
    def __init__(self, root):
        self.root = root
        self.left_child = None
        self.right_child = None

    def branch_left(self, branch):
        if self.left_child == None:
            self.left_child = BinaryTree(branch)
        # if left child already exists...
        else:
            # create new node
            growth = BinaryTree(branch)
            # push old node down the branch to be left child of new node
            growth.left_child = self.left_child
            # set new node as left child of root
            self.left_child = growth

    def branch_right(self, branch):
        if self.right_child == None:
            self.right_child = BinaryTree(branch)
        else:
            growth = BinaryTree(branch)
            growth.left_child, self.left_child = self.left_child, growth

    def get_right(self):
        return self.right_child

    def get_left(self):
        return self.left_child

    def set_root(self, obj):
        self.root = obj

    def get_root(self):
        return self.root

    def __str__(self):
        content = {}
        content['root'] = str(self.root)
        if self.left_child:
            content['left'] = str(self.left_child)
        if self.right_child:
            content['right'] = str(self.right_child)
        return repr(content)

if __name__ == "__main__":
    tree = BinaryTree(1)
    print("Root:", tree.get_root())
    print("Adding left child = 2")
    tree.branch_left(2)
    left_branch = tree.get_left()
    print("Left branch:", left_branch)
    print("Adding right child = 3")
    tree.branch_right(3)
    print("Right branch:", tree.get_right())
    branch = tree.get_right()
    print("Adding right child to right branch = 4")
    branch.branch_right(4)
    print("Right branch's right child:", branch.get_right())
    print("Right branch:", tree.get_right())
    print("Right branch's root:", branch.get_root())
    print("Tree:", tree)
