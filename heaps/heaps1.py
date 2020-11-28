"""
1. Get Max
2. Insert
3. Poll
"""


class Heap(object):
    HEAP_SIZE = 10

    def __init__(self):
        self.heap = [0] * self.HEAP_SIZE
        self.heap_size = 0

    def get_max(self):
        return self.heap[0]

    def is_full(self):
        return self.heap_size == self.HEAP_SIZE

    def insert(self, data):
        if self.is_full():
            return "Heap Is Full"

        self.heap[self.heap_size] = data
        self.heap_size += 1

        self.fix_up(self.heap_size - 1)

    def fix_up(self, index):
        parent_index = (index - 1) // 2

        if parent_index > 0 and self.heap[index] > self.heap[parent_index]:
            self.swap(index, parent_index)
            self.fix_up(parent_index)

    def swap(self, index, parent_index):
        self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]

    def poll(self):
        max = self.get_max()

        self.swap(0, self.heap_size - 1)
        self.heap_size -= 1

        self.fix_down(0)

        return max

    def fix_down(self, index):
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2

        larger_index = index

        if self.heap[left_child_index] > self.heap[larger_index]:
            larger_index = left_child_index

        if self.heap[right_child_index] > self.heap[larger_index]:
            larger_index = right_child_index

        if larger_index != index:
            self.swap(index, larger_index)
            self.fix_down(larger_index)

    def heap_sort(self):
        for item in range(self.heap_size):
            print(self.poll())
