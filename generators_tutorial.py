#generators - simple way of creating iterators. A generator is a function that returns an object
#(iterator) which we can iterate over (one value at a time). This solves the problem of storing 
#and iterating over the entire sequence and exhausting the RAM. It does not store the entire sequence
#of iterables.

#A generator pattern

# class Gen:
# 	def __init__(self, n):
# 		self.n = n
# 		self.last = 0


# 	def __next__(self):
# 		return self.next()


# 	def next(self):
# 		if self.last == self.n:
# 			raise StopIteration()

# 		rv = self.last ** 2
# 		self.last += 1
# 		return rv


# g  = Gen(100)

# while True:
# 	try:
# 		print(next(g))
# 	except StopIteration:
# 		break

import sys

def gen(n):
	for i in range(n):
		yield i ** 2 #yield just pauses the execution rather than stopping it. It has 
		#memory of the last iterable and will generate the next value when the execution
		#is presumed/the last time it was left off

x = [i ** 2 for i in range(10000)]
g = gen(10000)

print(sys.getsizeof(x))
print(sys.getsizeof(g))
# for i in g:
# 	print(i)

