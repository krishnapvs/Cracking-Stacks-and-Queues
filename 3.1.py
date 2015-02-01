# Describe how you could use a single array to implement three stacks

class Stack_Array:
	def __init__(self):
		self.array=[None]*300
		self.index={1:0,2:1,3:2}

	def push(self,cargo,stack):
		if (self.index[stack] > 300):
			print "Stack overflow"
		else:
			self.array[self.index[stack]]=cargo
			self.index[stack]=self.index[stack]+3

	def pop(self,stack):
		if (self.index[stack] in (0,1,2)):
			print "stack empty"
		else:
			self.index[stack]=self.index[stack]-3
			temp = self.array[self.index[stack]]
			self.array[self.index[stack]] = None
			print temp

	def peek(self,stack):
		if (self.index[stack] in (0,1,2)):
			print "stack empty"
		else:
			print self.array[self.index[stack]-3]

S=Stack_Array()			
for i in range(0,10):
	S.push(i,1)

for i in range(10,20):
	S.push(i,3)
for i in range(20,30):
	S.push(i,2)

S.peek(3)
S.peek(1)
S.peek(2)
'''
for i in range(10):
	S.pop(1)
	S.pop(2)
	S.pop(3)

S.pop(1)'''