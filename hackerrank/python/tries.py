"""
We're going to make our own Contacts application! The application must
perform two types of operations:

- add name, where  is a string denoting a contact name. This must store
as a new contact in the application.
- find partial, where  is a string denoting a partial name to search
the application for. It must count the number of contacts starting with
and print the count on a new line.

Given sequential add and find operations, perform each operation in order.
url: https://www.hackerrank.com/challenges/ctci-contacts
"""

def case0():
    return ["add hack",
            "add hac",
            "add ha",
            "find hac",
            "add hackerrank",
            "add hackk",
            "add hackee",
            "find ac",
            "add ack",
            "add acki",
            "add acka",
            "add ac",
            "add hackker",
            "add rank",
            "find hac",
            "find ha",
            "find hak",
            "find h",
            "find ac"
            ]

class Node:
    """
    __slots__ makes the trick to avoid runtime error, because reserves space
    for the declared variables and prevents the automatic creation of
    __dict__ and __weakref__ for each instance

    url: https://docs.python.org/2/reference/datamodel.html#slots
    """
    __slots__ = ('next', 'count', 'is_complete', 'key')

    def __init__(self, key):
        self.is_complete = False
        self.next = {}
        self.key = key
        self.count = 0

    def add(self, data):
        current_node = self
        while len(data) > 0 and current_node is not None:
            key = data[0]
            exist = current_node.exist_next(key)
            if exist is None:
                del data[0]
                exist = Node(key)
                exist.key = key
                exist.is_complete = True if len(data) == 0 else False
                exist.count = 1
                current_node.next[key] = exist
            else:
                del data[0]
                exist.count += 1
                exist.is_complete = True if len(data) == 0 or exist.is_complete else False

            current_node = exist

    def find(self, item):
        exist = self.exist_next(item[0])
        while len(item) > 1 and exist is not None:
            del item[0]
            exist = exist.exist_next(item[0])

        count = 0
        if exist is not None:
            count = exist.count

        print(count)

    def exist_next(self, value):
        return self.next[value] if value in self.next else None

    def __str__(self):
        for k, v in self.next.items():
            print(v)
        return ("'{}'{}={}. count={}".format(self.key, "x" if self.is_complete else "", len(self.next), self.count))


class TriesNonRecursive:

    def __init__(self):
        self.root = Node("*")

    def add(self, item):
        self.root.add(list(item))

    def find(self, item):
        self.root.find(list(item))


def my_test(cases):
    t = TriesNonRecursive()
    for item in cases:
        op, contact = item.split(" ")
        if op == "add":
            t.add(contact)
        elif op == "find":
            t.find(contact)

def from_file():
    t = TriesNonRecursive()
    import time
    all_values = []

    n = 0
    with open("hackerrank\\tries\\test12\\input.txt", 'r') as f:
        n = int(f.readline())
        for i in range(n):
            all_values.append(f.readline())

    start = time.clock()
    add_count = 0
    find_count = 0
    for a0 in all_values:
        op, contact = a0.strip().split(' ')
        if op == "add":
            t.add(contact)
            add_count += 1
        elif op == "find":
            t.find(contact)
            find_count += 1

    end = time.clock()
    print ("time: %.2gs. add_count:%s, find_count:%s" % ((end - start), add_count, find_count))

def original():
    n = int(input().strip())
    for a0 in range(n):
        op, contact = input().strip().split(' ')

my_test(case0())
