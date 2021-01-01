import collections
from collections import Counter

#looks like a dictionary when outputted but it is quite different
c = Counter('galland')
print(c)
c = Counter([1,2,3])
print(c)
c = Counter({"a": 1, "b": 2, "c": 3})
print(c)
d = Counter(cats = 4, dogs = 5)
d['pigs'] = 1
print(d)

print(list(c.elements()))

print(c.most_common(1))