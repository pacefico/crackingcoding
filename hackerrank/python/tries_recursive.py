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

class RecursiveNode:
    def __init__(self, key, data=""):
        self.is_complete = False
        self.next = {}
        self.key = key
        self.count = 0

        if len(data) > 0:
            new_key = data[0]
            del data[0]
            self[new_key] = data
        elif key is not "*":
            self.is_complete = True

    def __getitem__(self, item):
        count = 0
        if len(self.next) > 0:
            for key, node in self.next.items():
                count += node[""]

        if self.is_complete:
            return count + 1

        return count

    def __setitem__(self, key, value):
        if len(key) > 0:
            exist = self.exist_next(key)
            if len(value) == 0 and key is not "*":
                if exist is None:
                    self.next[key] = RecursiveNode(key)
                else:
                    exist.is_complete = True
            else:
                if exist is None:
                    self.next[key] = RecursiveNode(key, value)
                else:
                    new_key = value[0]
                    del value[0]
                    exist[new_key] = value

    def exist_next(self, value):
        if value in self.next:
            return self.next[value]
        return None

    def __str__(self):
        for k,v in self.next.items():
            print(v)
        return ("'{}'{}={}".format(self.key, "x" if self.is_complete else "" , len(self.next)))


class TriesRecursive:

    def __init__(self):
        self.root = RecursiveNode("*")

    def add(self, item):
        data = list(item)
        key = data[0]
        del data[0]
        self.root[key] = data

    def find(self, item):
        item = list(item)
        exist = self.root.exist_next(item[0])
        while len(item) > 1 and exist is not None:
            del item[0]
            exist = exist.exist_next(item[0])

        count = 0
        if exist is not None:
            count += exist[""]

        print(count)


def my_test(cases):
    t = TriesRecursive()
    for item in cases:
        op, contact = item.split(" ")
        if op == "add":
            t.add(contact)
        elif op == "find":
            t.find(contact)

def from_file():
    t = TriesRecursive()
    import time
    all_values = []

    with open("hackerrank\\tries\\test2\\input.txt", 'r') as f:
        n = int(f.readline())
        for i in range(n):
            all_values.append(f.readline())

    start = time.clock()
    for a0 in all_values:
        op, contact = a0.strip().split(' ')
        if op == "add":
            t.add(contact)
        elif op == "find":
            t.find(contact)
    end = time.clock()
    print ("time: %.2gs" % (end - start))


def original():
    t = TriesRecursive()
    n = int(input().strip())
    for a0 in range(n):
        op, contact = input().strip().split(' ')
        if op == "add":
            t.add(contact)
        elif op == "find":
            t.find(contact)

from_file()