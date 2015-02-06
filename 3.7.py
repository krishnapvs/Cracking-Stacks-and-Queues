''' An animal shelter holds only dogs and cats, and operates on a strictly "first in,
first out" basis. People must adopt either the "oldest" (based on arrival time) of
all animals at the shelter, or they can select whether they would prefer a dog or
a cat (and will receive the oldest animal of that type). They cannot select which
specificanimal they would like. Create the data structures to maintain this system
and implement operations such as enqueue, dequeueAny, dequeueDog and
dequeueCat.You may use the built-in LinkedList data structure'''

class Animal():
	def __init__(self,name,kind):
		self.name=name
		self.kind=kind
		self.next=None

	def enqueue(self,name,kind):
		while(self.next):
			self=self.next
		self.next=Animal(name,kind)

	def dequeueAny(self):
		temp_name=self.name
		temp_kind=self.kind
		self.name=self.next.name
		self.kind=self.next.kind
		self.next=self.next.next
		


def  Shelter(name):
	



class Animal:
	def __init__(self,name=None,kind=None):
		self.name=name
		self.kind=kind
		self.next=next

	def enqueue(self,name,kind):
		head=self
		while head.next:
			head=head.next
		head.next=Animal(name,kind)

	def dequeueAny(self):
		temp=self
		self=self.next
		return temp.name

a=Animal('cas','cat')

print a

print a.dequeueAny()

print a.dequeueAny()
print a 


