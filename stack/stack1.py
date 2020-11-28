"""
Get Length
Is Empty
Push
Pop
Peek
"""

class Stack(object):
	
	def __init__(self):
		self.stack = []
		
	
	def get_length(self):
		return len(self.stack)
		
	def is_empty(self):
		return self.get_length() == 0
		
	def push(self, data):
		self.stack.append(data)
		
	def pop(self):
		if self.get_length() == 0:
			return None
			
		data = self.stack[-1]
		del self.stack[-1]
		
		return data
		
	def peek(self):
		if self.get_length() == 0:
			return None
			
		return self.stack[-1]

st = Stack()
st.push(10)
print(st.pop())