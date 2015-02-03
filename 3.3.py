''' Imagine a (literal) stack of plates. If the stack gets too high, it migh t topple. Therefore,
in real life, we would likely start a new stack when the previous stack exceeds some
threshold. Implement a data structure SetOfStacks that mimics this. SetOf-
Stacks should be composed of several stacks and should create a new stack once
the previous one exceeds capacity. SetOfStacks.push() and SetOfStacks.
pop () should behave identically to a single stack (that is, pop () should return the
same values as it would if there were just a single stack).'''


class Stack():
	def __init__(self,capacity):
		self.capacity=capacity
		self.StackOfStacks=[[]]
	
	def push(self, cargo):
		if len(self.StackOfStacks[-1])>=self.capacity:
			self.StackOfStacks.append([])
		self.StackOfStacks[-1].append(cargo)

	def pop(self):
		temp=self.StackOfStacks[-1].pop()
		if len(self.StackOfStacks[-1])==0:
			self.StackOfStacks.pop()
		return temp

	def popAt(self,index):
		return self.StackOfStacks[index-1].pop()

S=Stack(8)

for i in range(24):
	S.push(i)

print S.popAt(1)
print 

for i in range(20):
	print S.pop()
