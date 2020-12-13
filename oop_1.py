#Corey Shafer: OOP - classes and instances - chapter1

#Main reason for using Classes:
	#1) Reusability
	#2) Extensibility
	#3) Organization of code and data

class Employee:
	# pass

	'''
	This is equivalent to a Constructor in other langguages. 
	When we create methods for a class, they receive the instance as the first argument automatically. 
	By convention, we call the instance 'self'. 
	You can call this whatever you want, but it's best to stick with the convention.
	self == <name of the instance> i.e emp1, emp2 etc...'''
	def __init__(self, first_name, last_name, pay):
		self.first_name = first_name
		self.last_name = last_name
		self.email = f'{self.first_name}.{self.last_name}@company.com'
		self.pay = pay


	#need to include 'self' here since this method receives the instance argument automatically when calling the method.
	#it expects the instance argument to be here hence need to include it.
	def full_name(self):
		return f'{self.first_name} {self.last_name}'



#each object has a different location in memory. These variables are known as instance variables.
#Instance variables contain data that is unique to each instance.
emp1 = Employee("Stanley", "John", 32000) #no need to pass in the self argument here since the emp1 is created as self and the instance is passed automatically
emp2 = Employee("Corey", "Shafer", 60000)

#manual addition of data to a unique instance of the Employee class. This is prone to errors.
# emp1.first_name = "Stanley"
# emp1.last_name = "John"
# emp1.email = "Stanley.John@company.com"
# emp1.pay = 32000


# emp2.first_name = "Corey"
# emp2.last_name = "Shafer"
# emp2.email = "Corey.Shafer@company.com"
# emp2.pay = 60000

print(emp1.email)
print(emp2.email)

#manually printing the full name of a patricular employee. Again, this is prone to errors
# print(f'{emp1.first_name} {emp1.last_name}')

print(emp1.full_name()) #we need parantheses here since this is a method...not an attribute
print(emp2.full_name())

#we can use the Class to access its method directly BUT we need to pass in the instance 
#manually as the argument. This way, you can see what's going on more in the background
#but prefer to use the above style above.
print(Employee.full_name(emp1))