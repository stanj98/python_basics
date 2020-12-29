#map function - The map() function executes a specified function for each item in an iterable. 
#The item is sent to the function as a parameter.

li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def func(x, *args):
	print(args)
	return x ** x


print(list(map(func, li, l2, l3, l4)))

