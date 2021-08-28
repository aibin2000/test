# how to find out what methods are available from a package in python3?
# python3
# help('collections')
# it tells https://docs.python.org/3.7/library/collections
from collections import deque

# Some minor changes

queue = deque(["Eric", "John", "Michael"])
print(queue)

queue.append("Terry")
print(queue)
queue.append("Graham")
print(queue)
queue.popleft()
print(queue)
queue.popleft()
print(queue)
queue.pop()
print(queue)

#List comprehensions provide a concise way to create lists
l = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
print(l)

# list - mutable
a = [-1, 1, 66.25, 333, 333, 1234.5]
print(a)
a.append(999)
print(a)
del(a[2:4])
print(a)

# tuple - immutable
# A tuple consists of a number of values separated by commas, for instance:
t = (12345, 54321, 'hello!')
print(t[2])

# A set is an unordered collection with no duplicate elements.
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)

a = set('abracadabra')
b = set('alacazam')
print(a)
print(b)
print (a-b)
print(a|b)
print(a^b)
print(a&b)

#It is best to think of a dictionary as a set of key: value pairs, with the requirement that the keys are unique (within one dictionary).
tel = {'jack': 4098, 'sape': 4139}
print(tel)
tel['guido'] = 4127
print(tel)
x = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print(x)

# loop
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

for i in reversed(range(1, 10, 2)):
    print(i)

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)

