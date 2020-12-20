
#Subclasses - these are classes that inherit all the attributes and methods from the Parent class.
#You can add new and/or override functionality without affecting the Parent class. 


'''
Method resolution order - where Python walks up the chain of inheritance until it finds
what its looking for. The place where the attributes and methods are searched for in a Class.
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


class Developer(Employee):
	#override the raise amount here
	raise_amount = 1.10



dev_1 = Developer("Stanley", "John", 32000) 
dev_2 = Developer("Paul", "Bauje", 60000)

print(dev_1.email)
print(dev_2.email)


print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)