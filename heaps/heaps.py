class Heap(object):
    HEAP_SIZE = 10

    def __init__(self):
        self.heap = [0] * self.HEAP_SIZE
        self.heap_size = 0

    def is_full(self):
        return self.heap_size == self.HEAP_SIZE

    def get_max(self):
        return self.heap[0]

    def insert(self, data):
        if self.is_full():
            print("Heap full")
            return

        self.heap[self.heap_size] = data
        self.heap_size += 1

        self.fix_up(self.heap_size - 1)

    def fix_up(self, index):
        parent_index = (index - 1) // 2

        if parent_index >= 0 and self.heap[index] > self.heap[parent_index]:
            self.swap(index, parent_index)
            self.fix_up(parent_index)

    def swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def poll(self):
        max = self.get_max()

        self.swap(0, self.heap_size - 1)
        self.heap_size -= 1

        self.fix_down(0)

        return max

    def fix_down(self, index):

        left_index = (2 * index) + 1
        right_index = (2 * index) + 2
        largest_index = index

        if left_index < self.heap_size and self.heap[left_index] > self.heap[index]:
            largest_index = left_index

        if right_index < self.heap_size and self.heap[right_index] > self.heap[index]:
            largest_index = right_index

        if largest_index != index:
            self.swap(index, largest_index)
            self.fix_down(largest_index)

    def heap_sort(self):
        for item in range(self.heap_size):
            print(self.poll())
#
# heap = Heap()
# heap.insert(100)
# heap.insert(20)
# heap.insert(30)
# heap.insert(5)
# heap.heap_sort()

from heapq import heappop, heappush, heapify

heap1 = []
data = [13, 6, 8, 1, -4, 5, 9, 10]

for item in data:
    heappush(heap1, item)

while heap1:
    print(heappop(heap1))

heapify(data)
print(data)


