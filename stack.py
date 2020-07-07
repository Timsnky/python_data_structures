class Stack(object):

    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def get_length(self):
        return len(self.stack)

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        data = self.stack[-1]
        del self.stack[-1]
        return data

    def peek(self):
        return self.stack[-1]
