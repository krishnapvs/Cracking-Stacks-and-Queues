# Towers of Hanoi

class Stack():
	def __init__(self):
		self.towers=[[],[],[]]
	
	def push(self,index,cargo):
		self.towers[index].append(cargo)

	def pop(self,index):
		return self.towers[index].pop()

	def moveDisks(self,n,origin,destination,temp):
		# base case 
		if(n <= 0):
			return
		self.moveDisks(n-1,origin,temp,destination)
		dummy=self.towers[origin].pop()
		self.towers[destination].append(dummy)
		self.moveDisks(n-1, temp,destination,origin)


#Code to test

S=Stack()

for i in range(10,0,-1):
	S.push(0,i)

print S.towers

S.moveDisks(10,0,2,1)

print S.towers
