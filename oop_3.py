#Corey Shafer: OOP - classmethods and staticmethods - chapter3

class Employee():

	num_of_emps = 0
	raise_amount = 1.04

	def __init__(self, first_name, last_name, pay):
		self.first_name = first_name
		self.last_name = last_name
		self.email = f'{self.first_name}.{self.last_name}@company.com'
		self.pay = pay

		Employee.num_of_emps += 1


	def full_name(self):
		return f'{self.first_name} {self.last_name}'


	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amount)


	# @classmethod
	# def set_raise_amount(cls):
		



emp1 = Employee("Stanley", "John", 32000) 
emp2 = Employee("Corey", "Shafer", 60000)


print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)