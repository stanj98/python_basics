import collections
from collections import deque

#deque is exactly like a list but why choose this over a list?
#deque is more faster when it comes to appending at the beginning and at the 
#end of the list and it comes with many methods

#if you are trying to access random elements in an iterable fast, use a list

de = deque("hello", maxlen = 5) #this argument takes in an iterable
#if maxlen provided, it will only give you the specified bound and remove elements 
#to meet that bound. You cannot change the maxlen later. It is only initially defined
#and can be only accessed.
de.append("hi")

# print(de)

# de.append('4')
# de.append('5')

# print(de)

# de.appendleft([11,12])

# print(de)

# de.popleft()
# de.pop()

# de.clear()

de.extend('345') #takes in an iterable
de.extend("stanley") #adds to the end of the list
de.extendleft([1,2,3,4,4]) #adds to the beginning of the list but 
de.reverse()
#the series of left appends results in reversing the order of elements in the iterable argument.
# print(de)

# de.rotate(de.maxlen)
print(de)