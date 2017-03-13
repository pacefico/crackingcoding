import heapq


class Heap(object):

    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def get_parent_idx(self, idx):
        return int((idx - 1) / 2)

    def get_left_idx(self, idx):
        return (2 * idx) + 1

    def get_right_idx(self, idx):
        return (2 * idx) + 2

    def has_left(self, idx):
        return self.get_left_idx(idx) < self.size()

    def has_right(self, idx):
        return self.get_right_idx(idx) < self.size()

    def has_parent(self, idx):
        return self.get_parent_idx(idx) >= 0

    def left_child(self, idx):
        return self.items[self.get_left_idx(idx)]

    def right_child(self, idx):
        return self.items[self.get_right_idx(idx)]

    def parent(self, idx):
        return self.items[self.get_parent_idx(idx)]

    def swap(self, first_idx, second_idx):
        temp = self.items[first_idx]
        self.items[first_idx] = self.items[second_idx]
        self.items[second_idx] = temp

    def is_empty(self):
        return self.size() == 0

    def peek(self):
        if not self.is_empty():
            return self.items[0]

    def poll(self):
        if not self.is_empty():
            item = self.items[0]
            self.items[0] = self.items[self.size()-1];
            self.heapifyDown()
            del self.items[self.size()-1]
            return item

    def add(self, item):
        self.items.append(item)
        self.heapifyUp()

    def heapifyDown(self):
        pass

    def heapifyUp(self):
        pass

    def __str__(self):
        return "{}".format(self.items)

class MinHeap1(Heap):

    def heapifyDown(self):
        idx = 0
        while (self.has_left(idx)):
            smaller_idx = self.get_left_idx(idx)

            if self.has_right(idx) and self.right_child(idx) < self.left_child(idx):
                smaller_idx = self.get_right_idx(idx)

            if self.items[idx] < self.items[smaller_idx]:
                break
            else:
                self.swap(idx, smaller_idx)

            idx = smaller_idx

    def heapifyUp(self):
        idx = self.size() - 1
        while self.has_parent(idx) and self.parent(idx) > self.items[idx]:
            self.swap(self.get_parent_idx(idx), idx)
            idx = self.get_parent_idx(idx)

class MaxHeap1(Heap):

    def heapifyDown(self):
        idx = 0
        while (self.has_left(idx)):
            smaller_idx = self.get_left_idx(idx)

            if self.has_right(idx) and self.right_child(idx) > self.left_child(idx):
                smaller_idx = self.get_right_idx(idx)

            if self.items[idx] > self.items[smaller_idx]:
                break
            else:
                self.swap(idx, smaller_idx)

            idx = smaller_idx

    def heapifyUp(self):
        idx = self.size() - 1
        while self.has_parent(idx) and self.parent(idx) < self.items[idx]:
            self.swap(self.get_parent_idx(idx), idx)
            idx = self.get_parent_idx(idx)


class MinHeap(object):

    def __init__(self):
        self.values = []

    def add(self, item):
        heapq.heappush(self.values, item)

    def peek(self):
        return heapq.nsmallest(1, self.values)[0] if self.size() > 0 else None

    def poll(self):
        return heapq.heappop(self.values)

    def size(self):
        return len(self.values)

    def __str__(self):
        return "{}".format(self.values)

class MaxHeap(object):

    def __init__(self):
        self.values = []

    def add(self, item):
        heapq.heappush(self.values, -item)

    def peek(self):
        return -heapq.nsmallest(1, self.values)[0] if self.size() > 0 else None

    def poll(self):
        return -heapq.heappop(self.values)

    def size(self):
        return len(self.values)

    def __str__(self):
        return "{}".format([-val for val in self.values])


class MedianHeap():

    def __init__(self):
        self.lowers = MinHeap1()
        self.highers = MaxHeap1()

    def add(self, item):
        print("adding:{}".format(item))
        if self.lowers.size() == 0 or item < self.lowers.peek():
            self.lowers.add(item)
        else:
            self.highers.add(item)

        self.rebalance()

        print("h:{}".format(self.highers))
        print("l:{}".format(self.lowers))

    def rebalance(self):
        if self.highers.size() - self.lowers.size() >= 2:
            print("rebalancing...")
            self.lowers.add(self.highers.poll())

    def get_median(self):
        response = 0
        if self.lowers.size() == 0 and self.highers.size() == 0:
            response = -99999999999999999999

        if self.lowers.size() == self.highers.size():
            response = float((self.highers.peek() + self.lowers.peek()) / 2)

        if self.lowers.size() > self.highers.size():
            response = self.lowers.peek()

        if self.highers.size() > self.lowers.size():
            response = self.highers.peek()

        return "{0:.1f}".format(response)


def case0():
    values = [3,1,2,5,4]
    heap = MinHeap()

    for val in values:
        heap.add(val)

    print(heap)

    for iter in range(len(values)):
        print(heap.poll())
        print(heap)

def case1():
    values = [12,4,5,3,8,7]
    heap = MaxHeap()

    for val in values:
        heap.add(val)

    print(heap)

    for iter in range(len(values)):
        print(heap.poll())

def case2():
    values = [12, 4, 5, 3, 8, 7]

    heap = MaxHeap()

    for item in values:
        heap.add(item)

    for item in values:
        print(heap)
        print(heap.peek())
        print(heap.poll())

def case3():
    values = [12, 4, 5, 3, 8, 7]
    median = MedianHeap()

    results = []
    for val in values:
        median.add(val)
        results.append(median.get_median())
        print(median.get_median())

def case4():
    values = [1,2,3,4,5,6,7,8,9,10]
    median = MedianHeap()
    results = []

    for val in values:
        median.add(val)
        results.append(median.get_median())
        print(median.get_median())

    valid_results = [1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5]
    assert valid_results == results

case4()

