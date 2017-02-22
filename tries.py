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
            # "add ac",
            # "add hackker",
            # "add rank",
            "find hac",
            "find ha",
            "find hak",
            "find h",
            "find ac"
            ]

class TrieNode:
    """
    Without recursion
    """
    def __init__(self, key):
        self.is_complete = False
        self.next = {}
        self.key = key

    def add(self, data):
        current_node = self
        while len(data) > 0 and current_node is not None:
            key = data[0]
            #print("current:{}".format(current_node.key))

            exist = current_node.exist_next(key)
            if exist is None:
                #print("Not exist: {}".format(key))
                del data[0]
                exist = Node(key)
                exist.key = key
                exist.is_complete = True if len(data) == 0 else False
                current_node.next[key] = exist
            else:
                #print("Exist: {}".format(key))
                del data[0]
                exist.is_complete = True if len(data) == 0 or exist.is_complete else False

            current_node = exist

    def __getitem__(self, item):
        # print("get:{} self.key:{}".format(item, self.key))
        count = 0

        exist = self.exist_next(item[0])
        while len(item) > 1 and exist is not None:
            del item[0]
            # item = item[1:]
            exist = exist.exist_next(item[0])
            # exist = exist.next[item[0]] if item[0] in exist.next else None

        # count = 0
        # if exist is not None:
        #     # count = 1 if exist.is_complete else 0
        #     count += exist[""]
        #
        #     while exist is not None:
        #         if len(exist.next) > 0:
        #             for key, node in self.next.items():
        #                 count += node[""]
        #
        #     if self.is_complete:
        #         return count + 1

        return count

    def exist_next(self, value):
        if value in self.next:
            return self.next[value]
        return None

    def __str__(self):
        for k, v in self.next.items():
            print(v)
        return ("'{}'{}={}".format(self.key, "x" if self.is_complete else "", len(self.next)))

class Node:
    def __init__(self, key, data=""):
        self.is_complete = False
        self.next = {}
        self.key = key

        #print("inserting key:{} data:{}".format(key, data))
        if len(data) > 0:
            new_key = data[0]
            del data[0]
            self[new_key] = data
        elif key is not "*":
            self.is_complete = True

    def __getitem__(self, item):
        #print("get:{} self.key:{}".format(item, self.key))

        count = 0
        if len(self.next) > 0:
            for key, node in self.next.items():
                count += node[""]

        if self.is_complete:
            return count + 1

        return count

    def __setitem__(self, key, value):
        #print("self.key={}".format(self.key))
        #print("set {}={}".format(key, value))
        if len(key) > 0:
            exist = self.exist_next(key)
            #exist = self.next[key] if key in self.next else None
            if len(value) == 0 and key is not "*":
                if exist is None:
                    self.next[key] = Node(key)
                else:
                    exist.is_complete = True
            else:
                if exist is None:
                    self.next[key] = Node(key, value)
                else:
                    new_key = value[0]
                    del value[0]
                    exist[new_key] = value

    def exist_next(self, value):
        if value in self.next:
            return self.next[value]
        return None
        # if value in self.next.keys():
        #     #print('exist: {}'.format(value))
        #     return self.next[value]

        #print('not exist: {}'.format(value))
        #return None

    def __str__(self):
        for k,v in self.next.items():
            print(v)
        return ("'{}'{}={}".format(self.key, "x" if self.is_complete else "" , len(self.next)))


class Tries:

    def __init__(self):
        self.root = TrieNode("*")

    def add(self, value):
        #print("### adding: {}".format(value))
        self.root.add(list(value))

        # value = list(value)
        # key = value[0]
        # del value[0]
        # self.root[key] = value
        #print(self.root)

    def find(self, item):
        #print("### finding: {}".format(item))

        item = list(item)
        exist = self.root.exist_next(item[0])
        while len(item) > 1 and exist is not None:
            del item[0]
            #item = item[1:]
            exist = exist.exist_next(item[0])
            #exist = exist.next[item[0]] if item[0] in exist.next else None

        count = 0
        if exist is not None:
            #count = 1 if exist.is_complete else 0
            count += exist[""]

        print(count)


def my_test(cases):
    t = Tries()
    for item in cases:
        op, contact = item.split(" ")
        if op == "add":
            t.add(contact)
        elif op == "find":
            t.find(contact)

def from_file():
    t = Tries()
    import time
    start = time.clock()
    with open("hackerrank\\tries\\test2\\input.txt", 'r') as f:
        n = int(f.readline())
        for a0 in range(n):
            op, contact = f.readline().strip().split(' ')
            if op == "add":
                t.add(contact)
            elif op == "find":
                t.find(contact)
    end = time.clock()
    print ("time: %.2gs" % (end - start))


def original():
    n = int(input().strip())
    for a0 in range(n):
        op, contact = input().strip().split(' ')

# 4
# add hack
# add hackerrank
# find hac
# find hak

#my_test(case0())
from_file()