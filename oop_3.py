#Corey Shafer: OOP - classmethods and staticmethods - chapter3

#regular methods pass in the instance automatically as the first argument i.e self

#classmethods allow you to access the Class and not its instance thus are used
#for many Class oriented tasks in general such as building alternative constructors.
#They pass in the Class automatically as the first argument i.e cls

#staticmethods do not pass anything in automatically. They dont pass in the instance or the Class.
#So really, they behave just like REGULAR functions except, we INCLUDE them because they have some
#logical connection with the Class. A giveaway to know when to use staticmethods is when you realize
#there is no usage of 'self' or 'cls' anywhere in the function like the example below.

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


	@classmethod
	def set_raise_amount(cls, amount):
		cls.raise_amount = amount


	#Example of using classmethod as an alternative constructor to instantiate and create an object
	@classmethod
	def from_string(cls, employee_string):
		first_name, last_name, pay = employee_string.split('-')
		return cls(first_name, last_name, pay) #going to create and return a new employee so
		#that the coder can receive the new employee object created
		

	#doesnt operate on the instance or the Class so just pass in the arguments you want to work with
	@staticmethod
	def is_workday(day):
		return True if day.weekday() == 5 or day.weekday() == 6 else False 



emp1 = Employee("Stanley", "John", 32000) 
emp2 = Employee("Paul", "Bauje", 60000)


Employee.set_raise_amount(1.05)
#You can run class methods via class instances as well but its rarely used
# emp1.set_raise_amount(1.06)


#use class methods as a way to solve a common use-case problem eg:
#an incoming dataset of all employees with the particular format below.
#Need to parse them first and then add them within this Class.

emp_string_1 = "John-Doe-30000"
emp_string_2 = "Michael-Scott-45000"
emp_string_3 = "Paula-Freida-33000"

new_emp_1 = Employee.from_string(emp_string_1)
new_emp_2 = Employee.from_string(emp_string_2)
new_emp_3 = Employee.from_string(emp_string_3)

print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)

print(new_emp_1.full_name())
print(new_emp_1.email)


#testing the staticmethod
import datetime
my_date = datetime.date(2020, 12, 20)

print(Employee.is_workday(my_date))
