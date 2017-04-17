# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"
from threading import Lock

class Operation(object):
    """
        This class is used to store operations in the stack of operations to assure correct rollback
    """

    __slots__ = ('name', 'value')

    def __init__(self, name, value):
        """
            Constructor for class Operation
        :param name: Operation´s name. ex. push | pop
        :param value: value of the operation
        """
        self.name = name
        self.value = value

    def __str__(self):
        return "op: {}, val:{}".format(self.name, self.value)

class SimpleStack():
    """
        Class created to simplify the management of thread safe operations
        All operations append, pop and len are protected by a lock
    """
    __transaction_lock = Lock()

    def __init__(self):
        # write your code in Python 2.7
        self.items = []

    def append(self, value):
        self.__transaction_lock.acquire()
        try:
            self.items.append(value)
        finally:
            self.__transaction_lock.release()

    def pop(self):
        self.__transaction_lock.acquire()
        try:
            return self.items.pop() if len(self.items) > 0 else None
        finally:
            self.__transaction_lock.release()

    def __len__(self):
        self.__transaction_lock.acquire()
        try:
            return len(self.items)
        finally:
            self.__transaction_lock.release()

    def __str__(self):
        return "{}".format(self.items)

class Solution(object):
    """
        Its necessary to create the main Stack that will store all values
        then to control the transactions will be necessary to create another stack os transactions
        the third stack is to control the operations in the main stack allowing rollback of each transactions
    """

    """
    __slots__ makes the trick to avoid runtime error, because reserves space
    for the declared variables and prevents the automatic creation of
    __dict__ and __weakref__ for each instance

    url: https://docs.python.org/2/reference/datamodel.html#slots
    """
    __slots__ = ('items', 'transactions', 'committed')

    # using lock to assure atomic operations in the transactions
    __transaction_lock = Lock()

    def __init__(self):
        # write your code in Python 2.7
        self.items = SimpleStack()
        self.transactions = None
        self.committed = False

    def push(self, value):
        """
            For each push, the item is appended to items list that represents the main stack of this instance
            after appending, is verified if we have an instance os a transaction and then update the
            operation on the open transaction
        :param value: value that will be stored
        :return: None
        """

        self.items.append(value)

        if self.transactions is not None:
            current = self.transactions.top()
            if current != 0:
                current.push(Operation("push", value))


    def top(self):
        """
            Show the top value stored in the stack
        :return: The top value of the stack
        """

        if len(self.items) == 0:
            return 0

        response = self.items.pop()
        self.items.append(response)
        return response

    def pop(self):
        """
            For each pop operation, the item is removed from the items list that represents the main stack of this instance
            after appending, is verified if we have an instance os a transaction and then update the operation on the open transaction
        :param value: value that will be stored
        :return: None
        """

        if len(self.items) > 0:
            response = self.items.pop()
            if self.transactions is not None:
                current = self.transactions.top()
                if current != 0:
                    current.push(Operation("pop", response))
            return response

        return None

    def begin(self):
        """
            Make new instance of transaction
        :return: None
        """
        if self.transactions is None:
            self.transactions = Solution()

        # create new instances of Solution representing transactions
        self.transactions.push(Solution())

    def rollback(self):
        if self.__transaction_lock.locked():
            return False

        self.__transaction_lock.acquire()

        def perform_rollback(current):
            # performs the rollback
            operation = current.pop()
            while operation is not None:
                # print("rolling back: {}:{}".format(operation.name, operation.value))
                if operation.name == "push":
                    popped = self.items.pop()
                    if popped != operation.value:
                        self.items.append(popped)
                elif operation.name == "pop":
                    self.items.append(operation.value)
                operation = current.pop()
        # try to assure that even something got wrong the lock will be released
        try:
            if self.transactions is not None:
                # get current transaction
                current = self.transactions.pop()
                committed = []
                while current is not None:
                    # if there is open transactions committed, remove from list until find one valid transaction
                    if current.committed:
                        committed.append(current)
                        current = self.transactions.pop()
                        continue
                    else:
                        # having one transaction valid and once have items committed without rollback,
                        # then perform rollbacks first
                        while len(committed) > 0:
                            item = committed[0]
                            del committed[0]
                            perform_rollback(item)
                        perform_rollback(current)
                        break
                # print("committed:{}".format(len(committed)))
        finally:
            self.__transaction_lock.release()
            return True

    def commit(self):
        """
            Commit the current pending transaction
        :return:
            True - Commit has completed succesfully
            False - The operations is in progress
        """
        if self.__transaction_lock.locked():
            return False

        self.__transaction_lock.acquire()

        if self.transactions.top() == 0:
            self.__transaction_lock.release()
            return False
        try:
            if self.transactions is not None:
                #remove the actual transaction from transactions stack and mark as committed
                current = self.transactions.pop()
                if current.top() != 0:
                    current.committed = True
                    self.transactions.push(current)
        finally:
            self.__transaction_lock.release()
            return True

    def __str__(self):
        print("open: {}".format(len(self.transactions.items)))
        if isinstance(self.transactions, list):
            for item in self.transactions:
                print(item)
        return "i: {}".format(self.items)



def example2():
    sol = Solution()
    sol.push(4)
    print(sol.items)
    sol.begin()  # start transaction 1
    sol.push(7)  # stack: [4,7]
    print(sol.items)
    sol.begin()  # start transaction 2
    sol.push(2)  # stack: [4,7,2]
    print(sol.items)
    assert sol.rollback() == True  # rollback transaction 2
    assert sol.top() == 7  # stack: [4,7]
    print(sol.items)
    sol.begin()  # start transaction 3
    sol.push(10)  # stack: [4,7,10]
    print(sol.items)
    assert sol.commit() == True  # transaction 3 is committed
    print(sol.items)
    assert sol.top() == 10
    assert sol.rollback() == True  # rollback transaction 1
    print(sol)
    assert sol.top() == 4  # stack: [4]
    print(sol)
    assert sol.commit() == False  # there is no open transaction

def test1():
    # Define your tests here
    sol = Solution()
    sol.push(42)
    assert sol.top() == 42, "top() should be 42"

def test2():
    sol = Solution()
    sol.push(5)
    sol.push(2)  # stack: [5,2]
    assert sol.top() == 2
    sol.pop()  # stack: [5]
    assert sol.top() == 5

    sol2 = Solution()
    assert sol2.top() == 0  # top of an empty stack is 0
    sol2.pop()  # pop should do nothin

def test3():
    sol = Solution()
    sol.begin()
    sol.push(1)
    print(sol)
    sol.begin()
    sol.push(2)
    sol.push(3)
    sol.pop()
    print(sol)
    print("####")
    assert sol.rollback() == True
    print(sol)
    assert sol.rollback() == True
    print(sol)
    # sol.begin()
    # print(sol)
    # sol.push(3)
    # print(sol)

def test4():
    sol = Solution()
    sol.push(4)
    print(sol.items)
    sol.begin()  # start transaction 1
    sol.push(7)  # stack: [4,7]
    print(sol.items)
    sol.begin()  # start transaction 2
    sol.push(2)  # stack: [4,7,2]
    print(sol.items)
    assert sol.rollback() == True  # rollback transaction 2
    assert sol.top() == 7  # stack: [4,7]
    print(sol.items)
    sol.begin()  # start transaction 3
    sol.push(10)  # stack: [4,7,10]
    print(sol.items)
    assert sol.commit() == True  # transaction 3 is committed
    print(sol.items)
    assert sol.top() == 10
    assert sol.rollback() == True  # rollback transaction 1
    print(sol)
    assert sol.top() == 4  # stack: [4]
    print(sol)
    assert sol.commit() == False  # there is no open transaction
    print(sol)
    sol.push(2)
    assert sol.top() == 2
    sol.begin()
    sol.commit()
    sol.commit()
    sol.begin()
    sol.commit()
    sol.begin()
    sol.push(3)
    sol.push(5)
    sol.push(6)
    sol.begin()
    sol.commit()
    sol.begin()
    sol.push(7)
    assert sol.top() == 7
    sol.rollback()
    assert sol.top() == 6
    sol.commit()
    print(sol)
    sol.begin()
    sol.begin()
    sol.begin()
    sol.begin()
    sol.rollback()
    sol.rollback()
    sol.push(7)
    sol.push(8)
    print(sol)
    sol.rollback()
    assert sol.top() == 6
    sol.rollback()
    sol.rollback()
    sol.rollback()
    print(sol)

def test5():
    import time
    sol = Solution()

    commands = []
    with open("stack.txt", 'r') as f:
        n = 100000
        for i in range(n):
            commands.append(f.readline())

    start = time.clock()
    for a0 in commands:
        op, value = a0.strip().split(' ')
        op.replace("\n", "")
        if op == "push":
            sol.push(int(value))
        if op == "pop":
            sol.pop()
        if op == "rollback":
            sol.rollback()
        if op == "begin":
            sol.begin()
        if op == "top":
            sol.top()
    end = time.clock()
    print("time: %.2gs" % (end - start))

def test6():
    import time
    import threading
    sol = Solution()

    commands = []
    with open("stack.txt", 'r') as f:
        n = 100000
        for i in range(n):
            commands.append(f.readline())

    start = time.clock()
    for a0 in commands:
        op, value = a0.strip().split(' ')
        op.replace("\n", "")
        if op == "push":
            sol.push(int(value))
        if op == "pop":
            sol.pop()
        if op == "rollback":
            sol.rollback()
        if op == "begin":
            sol.begin()
        if op == "top":
            sol.top()
    end = time.clock()
    print("time: %.2gs" % (end - start))

def test7():
    """
        Create to perform test
        1 - Generate operations and values randomly (ex. push 12922, pop, begin, etc) and puts in a Stack (Stack Simple)
        2 - Create N threads to be executed together, remove an operation from the stack and perform the test
        3 - Measure the total amount of time spent
    :return: None
    """
    import random
    import time
    import threading

    def generate_input(operations):
        """
            Generates random operations with random values
        :param operations:
        :return:
        """
        def get_operation(code):
            if code == 0:
                return "push"
            if code == 1:
                return "pop"
            if code == 2:
                return "rollback"
            if code == 3:
                return "begin"
            if code == 4:
                return "top"
            return "push"

        items = SimpleStack()
        for i in range(operations):
            op = get_operation(random.randint(0, 4))
            randA = random.randint(1, 1000000000)
            if op == "push":
                items.append("{} {}\n".format(op, randA))
            else:
                items.append("{} {}\n".format(op, 0))
        return items

    # total operation s ammount to be performed
    operations = 100000
    n_threads = 10

    # declared as global to be accessed by different threads
    global commands
    global sol

    # generates random imputs and values to perform the test
    commands = generate_input(operations)
    sol = Solution()

    start = time.clock()

    def process_thread():
        """
            Thread will process the operation removed from the stack generate previously
        :return: None
        """
        global commands
        global sol

        while len(commands) > 0:
            command = commands.pop()
            if command:
                op, value = command.strip().split(' ')
                if op == "push":
                    sol.push(int(value))
                if op == "pop":
                    sol.pop()
                if op == "rollback":
                    sol.rollback()
                if op == "begin":
                    sol.begin()
                if op == "top":
                    sol.top()
        end = time.clock()

    try:
        threads = []
        # create threads to perform operations
        for _ in range(n_threads):
            t = threading.Thread(target=process_thread)
            t.start()
            threads.append(t)
        # wait for all threads to finish
        for t in threads:
            t.join()
    except:
        process_thread()

    end = time.clock()
    # calculate total amount of time
    print("time: %.2gs" % (end - start))


test1()
test2()
test3()
test4()
test5()
test6()
test7()