#Tech With Tim - public and private classes

'''
Use a double underscore at the beginning of a Class and then the class name to make it private.
Use a double underscore at the beginning of a method and then the method name to make it private.

By convention, you need to use a double underscore at the beginning of a Class or method to make it private.
But, Python does not create private access for these classes or methods. In fact, it's just an 
indication to other developers not to touch those classes or methods that have a single underscore
at the beginning. Which means, developers CAN still use it if needed since there are no errors raised
despite providing the underscore (not directly though, but only via a public method)

In Python, there is no existence of Private methods that cannot be accessed except inside a class.

However, private methods can be accessed by calling the private methods via public methods.
'''



class _Private:

	def __init__(self, name):
		self.name = name


	def __display_me(self):
		print("This is a private method!")




class NotPrivate:

	def __init__(self, name):
		self.name = name
		self.priv = _Private(name)

	def __display(self):
		print("Hello")

	def display(self):
		print("Hi")


	def help(self):
		self.__display()


p1 = NotPrivate("stanley")
p1.help() #cannot access __display() directly, but you can access the private method via 
#public method i.e 'help()' in this case.





'''
Name mangling: (https://www.geeksforgeeks.org/private-methods-in-python/)

Python provides a magic wand which can be used to call private methods outside the class also, 
it is known as name mangling. It means that any identifier of the form __geek 
(at least two leading underscores or at most one trailing underscore) 
is replaced with _classname__geek, where classname is the current class name with 
leading underscore(s) stripped.

'''

class A:  
    
    # Declaring public method 
    def fun(self): 
        print("Public method") 
    
    # Declaring private method 
    def __fun(self): 
        print("Private method") 
          
# Driver's code 
obj = A() 
  
# Calling the private member  
# through name mangling 
obj._A__fun() 