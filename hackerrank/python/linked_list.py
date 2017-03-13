"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as:

    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node

url: https://www.hackerrank.com/challenges/ctci-linked-list-cycle
"""

import random

class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

def has_cycle(head):
    if head is not None:
        node = head
        while node is not None:
            node = node.next
            print(node.data)
            if head.next is not None and node == head.next and node.data == head.next.data:
                return True
        return False
    return True

def case0():
    n = random.randint(1, 100)
    head = Node(0)
    node = Node(1,head)
    for x in range(n):
        node = Node(random.randint(100,200), node)
    head.next = node
    return head.next

def case1():
    n1 = Node(1)
    n2 = Node(2,n1)
    n3 = Node(3,n2)
    n4 = Node(4,n3)
    n5 = Node(5,n4)

    n1.next = n5
    return n1

def case2():
    return None

def case3():
    n1 = Node(1)
    n2 = Node(2,n1)
    n3 = Node(3,n2)
    n4 = Node(4,n3)
    n5 = Node(5,n4)

    return n5

def case4():
    n1 = Node(1)
    n2 = Node(2,n1)
    n3 = Node(3, n2)
    n4 = Node(4, n3)
    n5 = Node(5,n4)
    n1.next = n4
    return n5

def case5():
    return Node(1)

assert has_cycle(case0()) == True
assert has_cycle(case1()) == True
assert has_cycle(case2()) == True
assert has_cycle(case3()) == False
assert has_cycle(case4()) == True
assert has_cycle(case5()) == False
