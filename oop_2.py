#Corey Shafer: OOP - class varibles - chapter2

#Class variables are variables that are shared among all instances of a Class.
#While instance variables are the unique for each instance, class variables will be the same
#for all instances.

class Employee():

	#class variable - can be used throughout all the methods and code. This avoids manual
	#manipulation for each occurence of the variable if used throughout
	raise_amount = 1.04

	num_of_emps = 0 #each time we create an employee, we can increment this variable by 1.

	def __init__(self, first_name, last_name, pay):
		self.first_name = first_name
		self.last_name = last_name
		self.email = f'{self.first_name}.{self.last_name}@company.com'
		self.pay = pay

		#using the Class here and not self (specific instance) since its the overall Employee count.
		#It would not make sense to have the ability to change this count value for each instance,
		#it should remain the same incremented value for all employees. It would not make sense
		#to change the total number of Employees for each instance.
		Employee.num_of_emps += 1


	def full_name(self):
		return f'{self.first_name} {self.last_name}'

	#when we access the class variable, we can't just apply them here directly. We can only
	#access the variable via the Class or the instance of the Class.

	'''Be careful and decide to use self or Class here. If self is used, then that instance will only 
	be affected. If Employee was used, then the new raise_amount class variable will be implemented
	throughout all instances. We are using self here since we may want the ability to change the 
	raise amount for each employee/ single instance of the Class.

	Also, any subclass can override the specific instance constant if they wanted to.
	'''
	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amount)





print(Employee.num_of_emps)

emp1 = Employee("Stanley", "John", 32000) 
emp2 = Employee("Corey", "Shafer", 60000)


#test the apply_raise method
# print(emp1.pay)
# emp1.apply_raise()
# print(emp1.pay)

#printing the namespace of emp1
# print(emp1.__dict__)

#changes raise_amount attribute for a specific instance of the Class. 
# emp1.raise_amount = 1.05

#If you want to change the value for all instances, you need to access the attribute via the
#Class and change it.
# Employee.raise_amount = 1.05

# print(emp1.__dict__)

# print(Employee.__dict__)

#We can access the class variable via the Class or the instance of the Class. When we access
#the class variable via the instance, it checks first whether if the variable exists for that 
#particular instance. Meaning, whether if the instance contains that attribute.

#If it does not, then it will check whether if the Class or any Class that the instance inherits
#from contains that attribute (class variable).
# print(Employee.raise_amount)
# print(emp1.raise_amount) #this does not particularly have the raise amount attribute until we specify it like above. Then, it will create the attribute for emp1 (that particular instance) only.
# print(emp2.raise_amount)


print(Employee.num_of_emps)