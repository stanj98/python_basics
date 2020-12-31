import collections
from collections import Counter


c = Counter('galland')
print(c)
c = Counter([1,2,3])
print(c)
c = Counter({1: "a", 1: "b", 3: "c"})
print(c)