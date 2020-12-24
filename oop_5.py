#Magic/Dunder methods - OOP 5

'''
These methods allow us to emulate some built-in behavior with Python 
and also how we can implement operator overloading.

By creating our own special methods, we can change some of the built-in
behaviour and operations.

These methods are always surrounded by double underscores i.e '__' 'dunder'
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
		pass



emp1 = Employee("Stanley", "John", 32000) 
emp2 = Employee("Paul", "Bauje", 60000)

repr(emp2)