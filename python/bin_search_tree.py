"""
For the purposes of this challenge, we define a binary search tree to be
a binary tree with the following ordering properties:

The  value of every node in a node's left subtree is less than the data value of that node.
The  value of every node in a node's right subtree is greater than the data value of that node.
Given the root node of a binary tree, can you determine if it's also a binary search tree?

Complete the function in your editor below, which has  parameter: a pointer to the root
of a binary tree. It must return a boolean denoting whether or not the binary tree is a
binary search tree. You may have to write one or more helper functions to complete this challenge.

Note: We do not consider a binary tree to be a binary search tree if it contains duplicate values.
url: https://www.hackerrank.com/challenges/ctci-is-binary-search-tree
"""

class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def set_right(self, right):
        self.right = right

    def set_left(self, left):
        self.left = left

def case1():
    n8 = node(8)
    n6 = node(6)
    n8.set_left(n6)
    n6.set_left(node(4))
    return n8

def case2():
    n10 = node(10)
    n5 = node(5)
    n10.set_left(n5)
    n4 = node(4)
    n1 = node(1)
    n5.set_left(n4)
    n4.set_left(n1)

    n7 = node(7)
    n5.set_right(n7)
    n11 = node(11)
    n5.set_right(n11)

    n16 = node(16)
    n10.set_right(n16)
    return n10

def case3():
    n7 = node(7)
    n9 = node(9)
    n7.set_right(n9)

    n4 = node(4)
    n7.set_left(n4)
    n1 = node(1)
    n4.set_left(n1)
    n6 = node(6)
    n4.set_right(n6)
    return n7

def case4():
    n5 = node(5)
    n1 = node(1)
    n8 = node(8)
    n5.set_left(n1)
    n5.set_right(n8)

    n9 = node(9)
    n12 = node(12)
    n8.set_left(n9)
    n8.set_right(n12)
    return n5


def case5():
    n10 = node(10)
    n5 = node(5)
    n16 = node(16)

    n10.set_left(n5)
    n10.set_right(n16)

    n4 = node(4)
    n5.set_left(n4)

    n1 = node(1)
    n4.set_left(n1)

    n7 = node(7)
    n5.set_right(n7)

    new4 = node(4)
    n7.set_left(new4)


    return n10

def check_greater(node, value):
    """
        check all nodes in the right side of the root and check if it´s value is greater,
        doing it for all child nodes value recursively
    :param node: node to be checked
    :param value: value from root node to be compared
    :return: true: if all nodes values are greater than root
    """
    if node is None: return True
    response = False
    if node.data > value and \
        check_greater(node.left, value) and \
        check_greater(node.right, value):
        response = True
    return response

def check_less(node, value):
    """
        check all nodes in the left side of the root and check if it´s value is lesser,
        doing it for all child nodes value recursively
    :param node: node to be checked
    :param value: value from root node to be compared
    :return: true: if all nodes values are lesser than root
    """
    if node is None: return True

    response = False
    if node.data < value and \
            check_less(node.left, value) and \
            check_less(node.right, value):
        response = True
    return response

def check_binary_search_tree_(root):
    """
        check if its a binary tree
        1 - checking first left nodes recursively if they have its value LESSER than the root value
        2 - checking right nodes if they have its value GREATER than the root value
        3 - pass the left and right nodes to this function again to test the other nodes recursively
    :param root: root node of a binary tree
    :return: true: is a binary search tree
        false: is not a binary search tree
    """
    if root is None:
        return True
    if check_less(root.left, root.data) and \
        check_greater(root.right, root.data) and \
        check_binary_search_tree_(root.left) and \
        check_binary_search_tree_(root.right):
        return True
    else:
        return False

assert check_binary_search_tree_(case1()) == True
assert check_binary_search_tree_(case2()) == False
assert check_binary_search_tree_(case3()) == True
assert check_binary_search_tree_(case4()) == False
assert check_binary_search_tree_(case5()) == False

