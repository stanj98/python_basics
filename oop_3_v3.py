#Decorators

'''
A decorator is just a function that:
1) Takes another function as an argument,
2) Adds some kind of functionality, 
3) And then returns another function
'''

def decorator_function(original_function):

	#need to accept positional and keyword arguments => use *args and **kwargs
	def wrapper_function(*args, **kwargs):
		print(f'wrapper executed this before the {original_function.__name__} function')
		return original_function(*args, **kwargs)

	return wrapper_function


#Class decorator (using decorator with class as an alternative to the function based decorator)
# class DecoratorClass(object):

	#pass the function in this class
	# def __init__(self, original_function):
		#tie the function with the instance of this class
		# self.original_function = original_function

	#mimic the functionality with the wrapper that adds functionality to the original function
	'''Note: The __init__ method is used when the class is called to initialize the instance, 
	while the __call__ method is called when the instance is called'''
	# def __call__(self, *args, **kwargs):
		# print(f'call method executed this before the {self.original_function.__name__} function')
		# return self.original_function(*args, **kwargs)


@decorator_function
# @DecoratorClass
def display():
	print('display function ran')

@decorator_function
# @DecoratorClass
def display_info(name, age):
	print(f'display_info ran with arguments: {name} and {age}')


# display = decorator_function(display) #equivalent to the decorator symbol above
# display_info = decorator_function(display_info)
display()
display_info("Stanley", 22)