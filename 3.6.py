'''Write a program to sort a stack in ascending order (with biggest items on top).
You may use at most one additional stack to hold items, but you may not copy the
elements into any other data structure (such as an array). The stack supports the
following operations: push, pop, peek, and isEmpty.'''

class Stack:
	def __init__(self):
		self.items=[]

	def pop(self):
		return self.items.pop()

	def push(self,cargo):
		self.items.append(cargo)

	def isEmpty(self):
		return len(self.items)==0

	def peek(self):
		if len(self.items)==0:
			return None
		return self.items[-1]


def stackSort(S1):
	S2=Stack()
	while (not S1.isEmpty()):
		if (S2.isEmpty()):
			S2.push(S1.pop())			
		else:
			temp = S1.pop()			
			while (temp < S2.peek()):
				S1.push(S2.pop())
			S2.push(temp)
	print S2.items
	while (not S2.isEmpty()):
		S1.push(S2.pop())

# testing
S1=Stack()

for i in range(10):
	S1.push(i)

for i in range(10):
	S1.push(i)

print S1.items
stackSort(S1)

print S1.items

