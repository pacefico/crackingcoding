"""
A queue is an abstract data type that maintains the order in which elements were added to it,
 allowing the oldest elements to be removed from the front and new elements to be added to the rear.
 This is called a First-In-First-Out (FIFO) data structure because the first element
 added to the queue (i.e., the one that has been waiting the longest) is always the
 first one to be removed.

A basic queue has the following operations:
Enqueue: add a new element to the end of the queue.
Dequeue: remove the element from the front of the queue and return it.

url: https://www.hackerrank.com/challenges/ctci-queue-using-two-stacks
"""

class MyQueue(object):

    def __init__(self):
        self.stack = []
        self.stack_aux = []

    def switch(self):
        if len(self.stack_aux) == 0:
            for item in range(len(self.stack)):
                self.stack_aux.append(self.stack.pop())

    def peek(self):
        self.switch()
        value = self.stack_aux.pop()
        self.stack_aux.append(value)
        return value

    def pop(self):
        self.switch()
        response = self.stack_aux.pop()

    def put(self, value):
        self.stack.append(value)

def my_tests():
    def case0():
        return "1 42:2:1 14:3:1 28:3:1 60:1 78:2:2"

    def expect0():
        return ['14','14']

    queue = MyQueue()
    val_list = case0().split(":")
    res_list = []
    for line in val_list:
        values = line.split(" ")
        if values[0] == "1":
            queue.put(values[1])
        elif values[0] == "2":
            queue.pop()
        else:
            response = queue.peek()
            res_list.append(response)
            print(response)

    assert res_list == expect0()

def original_tests():
    #original tests using inputs
    queue = MyQueue()
    t = int(input())
    for line in range(t):
        values = map(int, input().split())
        values = list(values)
        if values[0] == 1:
            queue.put(values[1])
        elif values[0] == 2:
            queue.pop()
        else:
            print(queue.peek())


#running my own test
my_tests()