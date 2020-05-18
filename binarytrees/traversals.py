"""
this file implements external versions of three traversal methods for binary trees. these functions are included as internal methods with the nodeReference implementation of the BinaryTree class. the benefit to external methods is that actions can be defined and performed while traversing the tree, rather than just viewing the data itself.

"""

import operator
from parseTree import *

def preorder(tree):
    if tree:
        print(tree.get_root())
        preorder(tree.get_left())
        preorder(tree.get_right())

def postorder(tree):
    if tree is not None:
        postorder(tree.get_left())
        postorder(tree.get_right())
        print(tree.get_root())

def evaluate_postorder(tree):
    ops = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}
    left, right = None, None
    if tree:
        left = evaluate_postorder(tree.get_left())
        right = evaluate_postorder(tree.get_right())
        if left and right:
            return ops[tree.get_root()](left, right)
        else:
            return tree.get_root()

def inorder(tree):
    if tree is not None:
        inorder(tree.get_left())
        print(tree.get_root())
        inorder(tree.get_right())

def print_inorder(tree):
    expression = ""
    if tree:
        expression += '(' + print_inorder(tree.get_left())
        expression += str(tree.get_root())
        expression += print_inorder(tree.get_right()) + ')'
    return expression

if __name__=="__main__":
    test_equation = "( 3 + ( 4 * 5 ) )"
    tree = build_parser(test_equation)
    print("Preorder:")
    preorder(tree)
    print("Postorder:")
    postorder(tree)
    print("Evaluate Postorder:", evaluate_postorder(tree))
    print("Inorder:")
    inorder(tree)
    print("Print Inorder:", print_inorder(tree))
