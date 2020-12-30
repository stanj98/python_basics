#The filter() function returns an iterator where the items are filtered through a 
#function to test if the item is accepted or not.


def add7(x):
	return x + 7


def isOdd(x):
	return x%2 != 0


x = [1,2,3,4,5,6,7,8,9,10]

#returns back the same iterable passed in the filter function, ideally, it
#returns the item in the iterable is its True.
data = list(filter(isOdd, x))

print(data)

c = list(map(add7, data))

print(c)