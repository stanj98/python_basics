#Magic/Dunder methods - OOP 5

'''
These methods allow us to emulate some built-in behavior with Python 
and also how we can implement operator overloading.

By creating our own special methods, we can change some of the built-in
behaviour and operations.

These methods are always surrounded by double underscores i.e '__' 'dunder'

In Python, special methods are a set of predefined methods you can use to enrich your classes. 
They are easy to recognize because they start and end with double underscores, 
for example __init__ or __str__ .

The goal for repr() special method is to be an unambigious representation of an object (should be
used for debugging, logging and finding out more information about the object which is predominantly
used by developers), and the goal for str() method is to be a readable representation of an object
and is meant to be used as a display to the end-user.


'return/raise NonImplemented' - returns a fallback on the other object without throwing an error.
It checks if the error is already taken care of by this object but if it does not handle the 
error, then the NonImplemented raises an error eventually.
'''

class Employee():

	raise_amount = 1.04

	def __init__(self, first_name, last_name, pay):
		self.first_name = first_name
		self.last_name = last_name
		self.email = f'{self.first_name}.{self.last_name}@company.com'
		self.pay = pay


	def full_name(self):
		return f'{self.first_name} {self.last_name}'


	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amount)


	def __repr__(self):
		return f"Employee('{self.first_name}', '{self.last_name}', '{self.pay}')"

	def __str__(self):
		return f'{self.full_name()} - {self.email}'


	def __add__(self, other):
		return self.pay + other.pay


	def __len__(self):
		return len(self.full_name())



emp1 = Employee("Stanley", "John", 32000) 
emp2 = Employee("Paul", "Bauje", 60000)

# repr(emp2)

# print(repr(emp1))
# print(str(emp1))

# print(emp1.__repr__())
# print(emp1.__str__())

#uses the special method 'dunder add' behind the scenes
# print(int.__add__(1, 2))

# print(str.__add__("hi ", "stan!"))


print(emp1 + emp2)

print("test".__len__())

print(len(emp1))