"""
this file implements a binary tree structure using a "list of lists" technique

"""

def binaryTree(root):
    return [root, [], []]

def growLeft(root, branch):
    # check if value already exists in position
    child = root.pop(1)
    # if sublist exists, move it down branch as child of new node
    if len(child) > 1:
        root.insert(1, [branch, child, []])
    else:
        root.insert(1, [branch, [], []])
    return root

def growRight(root, branch):
    child = root.pop(2)
    if len(child) > 1:
        root.insert(2, [branch, child, []])
    else:
        root.insert(2, [branch, [], []])
    return root

def getRoot(root):
    return root[0]

def setRoot(root, value):
    root[0] = value

def leftChild(root):
    return root[1]

def rightChild(root):
    return root[2]

if __name__=="__main__":
    tree = binaryTree(3)
    growLeft(tree, 4)
    growLeft(tree, 5)
    growRight(tree, 6)
    growRight(tree, 7)
    print("Tree:", tree)
    branch = leftChild(tree)
    print("Left Child:", branch)
    setRoot(branch, 9)
    print("Tree:", tree)
    growLeft(branch, 11)
    print("Tree:", tree)
    print(rightChild(rightChild(tree)))
