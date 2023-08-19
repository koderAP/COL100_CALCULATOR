class Stack:
	def __init__(self):
		self.l=[]
		# Initialise the stack's data attributes
		pass
	
	def push(self, item):
		self.l.append(item)
		# Push an item to the stack
		pass

	def peek(self):
		if self.l==[]:
			return "Error" 
		return self.l[-1]
		# Return the element at the top of the stack
		# Return a string "Error" if stack is empty
		pass
	def second_peek(self):
		return self.l[-2]
	def remove(self):
		self.l.remove(self.l[-1])
	def reverse(self):
		self.l=self.l[::-1]
	def pop(self):
		if self.l!=[]:
			self.l.pop()
		# Pop an item from the stack if non-empty
		pass
	def clear(self):
		self.l=[]

	def in_stack(self,i):
		return (i in self.l)
	def is_empty(self):
		if self.l==[]:
			return True
		return False
		# Return True if stack is empty, False otherwise
		pass

	def __str__(self):
		if self.l==[]:
			return ''
		l1=self.l[::-1]
		s=""
		for i in range(len(l1)-1):
			s+=str(l1[i])+" "
		s+=str(l1[-1])
		return s

		# Return a string containing elements of current stack in top-to-bottom order, separated by spaces
		# Example, if we push "2" and then "3" to the stack (and don't pop any elements), 
		# then the string returned should be "3 2"
		pass

	def __len__(self):
		return len(self.l)
		# Return current number of elements in the stack
		pass