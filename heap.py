
class MinHeap(object):

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
        idx = self.size() -1
        while self.has_parent(idx) and self.parent(idx) > self.items[idx]:
            self.swap(self.get_parent_idx(idx), idx)
            idx = self.get_parent_idx(idx)

    def add(self, item):
        self.items.append(item)
        self.heapifyUp()

    def __str__(self):
        return "{}".format(self.items)


def case0():
    values = [3,1,2,5,4]
    heap = MinHeap()

    for val in values:
        heap.add(val)

    print(heap)

    for iter in range(len(values)):
        print(heap.poll())
        print(heap)

case0()

