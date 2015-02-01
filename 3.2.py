# How would you design a stack which, in addition to push and pop, also has a
#function min which returns the minimum element? Push, pop and min should
#all operate in O(1) time

class Stack:
	def __init__(self):
		self.items=[]
		self.min=[None]

	def push(self,cargo):
		self.items.append(cargo)
		if(self.min[0] == None):
			self.min[0]=cargo
			
		elif self.min[-1] > cargo:
			self.min.append(cargo)
			
		else:
			self.min.append(self.min[-1])
			

	def pop(self):
		if len(self.min)>1:
			self.min.pop()
		else:
			self.min[0]=None
		return self.items.pop()

	def minimum(self):
		return self.min[-1]

S=Stack()		
	
for i in range(10,1,-1):
	S.push(i)

for i in range(9):
	print S.pop()
	print
	print S.minimum()
