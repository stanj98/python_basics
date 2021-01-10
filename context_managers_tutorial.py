'''
Context managers allow you to allocate and release resources precisely when you want to. 
The most widely used example of context managers is the 'with' statement.
A common use case of context managers is locking and unlocking resources/shared memory and closing opened files.
You can use a try/finally statement but Python implemented the 'with' statement which does the
exact same thing and provides more functionality
'''

# with open("file.txt", "w") as file:
# 	file.write("hello")

#implementation of the Context Manager with a Class
# class File:
# 	def __init__(self, filename, method):
# 		self.file = open(filename, method)

# 	def __enter__(self):
# 		print("Enter")
# 		return self.file

	#Any exception raised will be handled by the exit function
	# def __exit__(self, type, value, traceback):
	# 	print(type)
	# 	print(value)
	# 	print(traceback)
	# 	print("Exit")
	# 	self.file.close()
		#return True #tells Python that we have gracefully handled the exception (if available)
		#and there is no need to crash the program. You should return True only after handling
		#the exception


#can use the File() class here since the enter and exit methods are defined above
# with File("file.txt", "w") as f:
# 	print("Middle content")
# 	f.write('hello')
# 	raise Exception()


#Use generator and decorator to use context managers

import contextlib

@contextlib.contextmanager
#this function is a generator
def file(filename, method):
	file = open(filename, method)
	yield file
	file.close()


with file("file.txt", "w") as f:
	f.write("hello world")
