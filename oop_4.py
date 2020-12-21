
#Subclasses - these are classes that inherit all the attributes and methods from the Parent class.
#You can add new and/or override functionality without affecting the Parent class. 


'''
Method resolution order - where Python walks up the chain of inheritance until it finds
what its looking for. The place where the attributes and methods are searched for in a Class.

The super() function is used to give access to methods and properties of a parent or sibling class. 
The super() function returns an object that represents the parent class.
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
	#override the raise amount here, will not affect any of the Employee instances or the Employee class
	raise_amount = 1.10

	#override the init method

	def __init__(self, first_name, last_name, pay, prog_lang):
		#pass the variables to the Employee class to avoid duplication and initiate the employee
		#object as well as add in a specific attribute for the subclass.
		super().__init__(first_name, last_name, pay)
		#or, you can initiate it like this
		# Employee.__init__(self, first_name, last_name, pay)
		self.prog_lang = prog_lang


class Manager(Employee):

	def __init__(self, first_name, last_name, pay):
		super(). __init__(first_name, last_name, pay, employees = None)
		if employees is None:
			self.employees = []
		else:
			self.employees = employees


	


dev_1 = Developer("Stanley", "John", 32000, "Python") 
dev_2 = Developer("Paul", "Bauje", 60000, "Java")

print(dev_1.email)
print(dev_2.email)

print(dev_1.prog_lang)
print(dev_2.prog_lang)


print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)