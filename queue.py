class Queue(object):

    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def length(self):
        return len(self.queue)

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        else:
            data = self.queue[0]
            del self.queue[0]
            return data

    def peek(self):
        if self.is_empty():
            return "Queue is empty"
        else:
            return self.queue[0]