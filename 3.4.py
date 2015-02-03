# Towers of Hanoi

class Stack():
	def __init__(self):
		self.towers=[[],[],[]]
	
	def push(self,index,cargo):
		self.towers[index].append(cargo)

	def pop(self,index):
		return self.towers[index].pop()

def moveDisks(n,origin,destination,temp):
	
