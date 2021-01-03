import collections
from collections import namedtuple

# Point = namedtuple('Point', 'x y z')
# Point = namedtuple('Point', ['x', 'y', 'o', 'd'])
Point = namedtuple('Point', {'x': 'hi', 'b': "whatsup", 'c': 'hello', 'd': 'hai'}) #takes the key names, but ignores the values and is added to the Point

# print(Point.__dict__)
#treat the Point variable above like a Class
newP = Point(3,4,5,3)

print(newP)

print(newP.x, newP.b, newP.c, newP.d)
print(newP[0]) #you can use basic operations of a tuple in a namedtuple as well
print(newP._asdict())
print(newP._fields)

#to replace the element value in a namedtuple, you need to assign it to a new object
newP = newP._replace(c = 20)
print(newP)


# Class method that makes a new instance from an existing sequence or iterable.
somellist = [1 ,3, 4, 5]
p2 = Point._make(somellist) #assign all the elements in iterable to the namedtuple's defined variables

print(p2)