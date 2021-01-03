import collections
from collections import Counter

#looks like a dictionary when outputted but it is quite different
# c = Counter('galland')
# print(c)
# c = Counter([1,2,3])
# print(c)
# c = Counter({"a": 1, "b": 2, "c": 3})
# print(c)
# d = Counter(cats = 4, dogs = 5)
# d['pigs'] = 1
# print(d)

#You can subtract counter elements' count using other iterables
c = Counter(a = 4, b = 6, c = 2, d = 0)

d = ['a', 'b', 'b', 'd'] #should be an iterable or a mapping.

# c.subtract(d)

print(c)

#same like above but adds instead of subtracting
#c.update(d) #or you can do: c+d (but you should only use Counter for this operation)
e = Counter(['a', 'b', 'b', 'd', 'd'])
print(c+e)
print(c-e) #wont show elements that have a count less than or equal to 0

#intersection - min elements for each counter
print(c & e) #wont show elements that have a count less than or equal to 0

#union - max elements shown for each counter
print(c | e)

# c.clear()

# print(c)

print(list(c.elements())) #returns an itertor of elements repeating as many times as its count

print(c.most_common(3)) #Returns a list of the n most common elements and their counts from the most common to the least