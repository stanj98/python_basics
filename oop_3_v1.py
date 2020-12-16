'''

"A programming language is said to have first-class functions if it treats functions as first-class
citizens."

First-Class Citizen (Programming):
"A first-class citizen (sometimes called first-time objects) in a programming language is an entity
that supports all the operations generally available to other entities. These operations typically
include being passed as an argument, returned from a function, and assigned to a variable".

TL:DR; We are able to treat functions just like any other object or variable.

Higher-order function: a function that accepts other functions as arguments or returns a function
as a result of a function.

'''

#Example of an aspect of a first-class function: assign to a variable

#Assign a function to a variable (this does not mean assigning the result of a function to a variable)
def square(x):
	return x * x

# f = square(5)
f = square #assign the function to a variable (not invoking/executing the function here)


print(square)
print(f)

#now, we can use 'f' as a normal function
print(f(5))



#Example of an aspect of a first-class function: pass a function as an argument to another function

def map_list(func, arg_list):
	new_list = [func(i) for i in arg_list]
	return new_list


initial_list = [1, 2, 3, 4, 5]
print(map_list(square, initial_list))


#Example of an aspect of a first-class function: return a function

def logger(msg):

	#dont need to pass in the msg parameter again into the below function since first-class functions
	#remeber the initial parameters sent from the initial functions
	def print_msg(user):
		print(f'{user} says: {msg} ')

	return print_msg

msg1 = logger("Call me")
msg1("Stan") 