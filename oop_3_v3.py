#Decorators

'''
A decorator is just a function that:
1) Takes another function as an argument,
2) Adds some kind of functionality, 
3) And then returns another function
'''

def decorator_function(original_function):

	def wrapper_function():
		print(f'wrapper executed this before the {original_function.__name__} function')
		return original_function()

	return wrapper_function


@decorator_function
def display():
	print('display function ran')


# display = decorator_function(display) #equivalent to the decorator symbol above
display()