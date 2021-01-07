#A Class is an object which is created by a higher level Class in Python. It gets created when we 
#return a class or create a class. Essentially, we can treat this Class (which we defined) as a object.
#A Metaclass defines the rules of a class. When a class gets created, the Metaclass creates it for us
#automatically and it defines how the class (which we created) is made. It defines the rules
#and creates the class, which we defined, for us.

# class Test:
# 	pass


# print(type(Test))
# print(type.__dict__)

#equivalent to the class definition above. All of the code in class we defined gets sent to the
#type class which then creates the class representation for us like the syntax below.

class Foo:
	def show(self):
		print("hello")


#to define a method is quite different, we need to do the following in a Metaclass

def add_attribute(self):
	self.z = 9


Test = type('Test', (Foo,), {"x":5, "add_attribute": add_attribute}) 
#this function takes the name of the class (which is the internal repr.)
#the inheritance (if available) and the third argument will contain the properties and methods and other
#stuff which we usually define in a normal class.

print(type(Test))
t = Test()

t.show()

t.add_attribute()
print(t.z)


class Meta(type):

	def __new__(self, class_name, bases, attrs):

		a = {}

		for name, value in attrs.items():
			if name.startswith("__"):
				a[name] = value
			else:
				a[name.upper()] = value

		return type(class_name, bases, a)


class Dog(metaclass = Meta):

	x = 5
	y = 8

	def hello(self):
		print("hello")


dog = Dog()
dog.HELLO()
print(dog.X)
