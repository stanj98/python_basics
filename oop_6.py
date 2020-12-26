#OOP 6 - property decorator

'''
With the property decorator, you can create getters, setters and deleters functionality for the Class
attributes. These can be found in other languages as well.

A property decorator allows us to define a method but access it like an attribute.
'''


class Employee():

	def __init__(self, first_name, last_name):
		self.first_name = first_name
		self.last_name = last_name


	@property
	def email(self):
		return f'{self.first_name}.{self.last_name}@company.com'

	#a method in the class but recognized and utilized as an attribute
	@property
	def full_name(self):
		return f'{self.first_name} {self.last_name}'

	#@<name_of_the_property>.setter -> create a method with the same name as the property
	@full_name.setter
	def full_name(self, name):
		first_name, last_name = name.split(' ')
		self.first_name = first_name
		self.last_name = last_name

	#@<name_of_the_property>.deleter -> create a method with the same name as the property
	@full_name.deleter
	def full_name(self):
		print("Delete name")
		self.first_name = None
		self.last_name = None



emp1 = Employee("Stanley", "John") 


emp1.full_name = "Kane Paul"

print(emp1.first_name)
print(emp1.email) #accessing the email method like an attribute.
print(emp1.full_name)


del emp1.full_name #deleter property decorator runs in the background every time the
#del keyword if used to delete an object's attribute(s).

print(emp1.full_name)