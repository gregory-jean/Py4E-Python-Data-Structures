# -----------------
# Video 10 - Tuples
# -----------------

'''
Tuples are another kind of sequence that functions much like a list.
    - They have elements which are indexed starting at 0

Tuples are NOT mutable

Cannot Sort, append, reverse

Tuples are more efficent than lists

'''
'''
x = ('Gregory', 'Michele', 'Nora')
print(x[2])
# >>> Nora

y = (1, 9, 2)
print(y)
# >>> (1, 9, 2)

print(max(y))
# >>> 9

for iter in y:
    print(iter)
# >>> 1
# >>> 9
# >>> 2

'''

# Tuples and Assignment
'''
We can also put a tuple on the left-hand side of 
an assignment statement

We can even omit the parentheses
'''
'''
(x, y) = (4, 'Evan')
print(y)
# >>> Evan

(a, b) = (99, 98)
print(a)
# >>> 99
'''

# Tuples and Dictionaries
'''
The items() method in dictionaries returns
a list of (key, value) tuples

'''
'''
d = dict()
d['Gregory'] = 2
d['Michele'] = 4

for (k, v) in d.items() :
    print(k, v)
# >>> Gregory 2
# >>> Michele 4

tups = d.items()
print(tups)
# >>> dict_items([('Gregory', 2), ('Michele, 4')])
'''

# Tuples are comparable
'''
The comparison operators work with tuples and other 
sequences. If the first item is equal, Python goes on
to the next element, and so on, until it finds 
elements that differ.

'''
'''
(0, 1, 2) < (5, 1, 2)
# >>> True
(0, 1, 2000000) < (0, 3, 4)
# >>> True
('Jones', 'Sallly') < ('Jones', 'Sam')
# >>> True
('Jones', 'Sally') > ('Adams', 'Sam')
# >>> True
'''

# Sorting Lists of Tuples
'''
We can take advantage of the ability to sort a list of tuples
to get a sorted version of a dictionary

First we sort the dictionary by the key using the items() method
and sorted() function

'''
'''
d = {'a': 10, 'b': 1, 'c': 22}
d.items()
# >>> dict_items([('a', 10), ('c', 22), ('b', 1)])

sorted(d.items())
# >>> [('a', 10), ('b', 1), ('c', 22)]
'''

# Using sorted()

'''

Sorting by Key

We can do this even more directly using the built-in
function sorted that takes a sequence as a parameter
and returns a sorted sequence.

'''
'''
d = {'a': 10, 'b': 1, 'c': 22}
t = sorted(d.items())
print(t)
# >>> [('a', 10), ('b', 1), ('c', 22)]

for k, v in sorted(d.items()) :
    print(k, v)
# >>> a 10
# >>> b 1
# >>> c 22
'''

# Sort by values instead of key
'''
If we could construct a list of tuples of the form (value, key)
we could sort by value

We do this with a for loop that creates a list of tuples

'''

c = {'a': 10, 'b': 1, 'c': 22}
tmp = list()
for k, v in c.items() :
    tmp.append((v, k))

print(tmp)
# >>> [(10, 'a'), (22, 'c'), (1, 'b')]

tmp = sorted(tmp, reverse=True)
print(tmp)
# >>> [(22, 'c'), (10, 'a'), (1, 'b')]
