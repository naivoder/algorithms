"""
this file implements a mathmatical expression parse tree using a binary tree and the stack ADT

"""
import operator
from stacks.stack import *
from nodeReference import *

operators = "+-*/)"

def build_parser(expression, debug=False):
    pieces = expression.split()
    if debug:
        print("Pieces:", pieces)
    tree_stack = Stack()
    root_tree = BinaryTree('')
    tree_stack.push(root_tree)
    current_tree = root_tree
    for object in pieces:
        if object is "(":
            current_tree.branch_left('')
            tree_stack.push(current_tree)
            current_tree = current_tree.get_left()
        elif object not in operators:
            if debug:
                print("Setting root = %s" % object)
            current_tree.set_root(int(object))
            parent = tree_stack.pull()
            current_tree = parent
        elif object in operators[:-1]:
            current_tree.set_root(object)
            current_tree.branch_right('')
            tree_stack.push(current_tree)
            current_tree = current_tree.get_right()
        elif object is ")":
            current_tree = tree_stack.pull()
        else:
            raise ValueError("This is an invalid expression!")

    if debug:
        print("Final tree:", root_tree)
    return root_tree

def evaluate(parse_tree):
    ops = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}
    left = parse_tree.get_left()
    right = parse_tree.get_right()
    if left and right:
        function = ops[parse_tree.get_root()]
        return function(evaluate(left), evaluate(right))
    else:
        return parse_tree.get_root()

if __name__=="__main__":
    test_equation = "( 3 + ( 4 * 5 ) )"
    parse_tree = build_parser(test_equation)
    print("###---Parse Tree---###")
    print("Equation:", test_equation)
    print("Solution:", evaluate(parse_tree))
