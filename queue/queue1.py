"""
Length
Is Empty
Enqueue
Dequeue
Peek
"""


class Queue(object):

	def __init__(self):
		self.queue = []

	def get_length(self):
		return len(self.queue)

	def is_empty(self):
		return self.get_length == 0

	def enqueue(self, data):
		self.queue.append(data)

	def dequeue(self):
		if self.get_length() == 0:
			return None

		data = self.queue[0]
		del self.queue[0]

		return data

	def peek(self):
		if self.get_length() == 0:
			return None

		return self.queue[0]
