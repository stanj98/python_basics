# A lambda function is a small anonymous function.

# A lambda function can take any number of arguments, but can only have one expression.

#use lambda when you only have one expression only

#Use lambda functions when an anonymous function is required for a short period of time.

# <name of the function> = lambda <parameter or many parameters passed in> : <one single expression> 

def func1(x):
	func = lambda x : x + 5
	return func(x) + 85

print(func1(9))

func3 = lambda x,y : x + y

print(func3(10, 10))