# -----------------
# Video 8.1 - Lists
# -----------------

'''
Most of our variables have one value in them - when we put a new
value in the variable, the old value is overwritten.

x = 2
x = 4
print(x)

# >>> 4

A Collection allows us to put many values in a single 'variable'

A collection is nice because we can carry many values
around in one convenient package.

friends = ['John,', 'Evan', 'Rocky']
carryOn = ['socks', 'shirt', 'perfume']

List constants are surrounded by square brackets
and the elements in the list are seperated by commas

A list element can be any Python object - even another list

A list can be empty

'''
'''
print([1, 24, 76])
# >>> [1, 24, 76]

print(['red', 'yellow', 'blue'])
# >>> ['red', 'yellow', 'blue']


friends = ['John', 'Evan', 'Donnie']

for friend in friends :
    print('Happy New Year:', friend)
print('done!')
'''



# Looking Inside Lists
'''
Just like strings, we can get at any single element in a 
list using an index specified in square brackets []

'''
'''
friends = ['John', 'Evan', 'Donnie']
print(friends[1])
# >>> Evan
'''

# Lists are Mutable
'''
Strings are 'immutable' - we cannot change the contents
of a string - we must make a new string to make any change

fruit = 'Pineapple'
fruit[0] = 'p'
# Traceback

Lists are 'mutable' - We can change an element of a list
using the index operator

'''
'''
lotto = [2, 14, 26, 41, 63]
print(lotto)
# >>> [2, 14, 26, 41, 63]

lotto[2] = 28
print(lotto)
# >>> [2, 14, 28, 41, 63]
'''

# Length of a list

'''
x = [1, 2, 'greg', 99]
print(len(x))
# >>> 4

'''

# Using the Range Function

'''
The range function returns a list of numbers that range
from zero to one less than the parameter

We can construct an index loop using for and an integer interator

'''
'''
print(range(4))

friends = ['John', 'Evan', 'Donnie']
print(len(friends))
# >>> 3

print(range(len(friends)))
# >>> [0, 1, 2]
'''

# Knowing the index number of a list in a loop (Counted Loop)
'''
Sometimes you want to know the location of an item in a list. 

Using the second for loop to know the location of an item in a list.
'''
'''
friends = ['John', 'Evan', 'Donnie']

for friend in friends :
    print('Happy New Year:', friend)

for i in range(len(friends)) :
    friend = friends[i]
    print('Happy New Year:', friend)
'''

# ----------------------------------
# Video 8.2 - Manipulating Lists
# ----------------------------------

# Building a List from Scratch

'''
We can create an empty list and then add elements using the 
append method

The list stays in order and new elements are added at the end
of the list

'''
'''
stuff = list()
stuff.append('book')
stuff.append(99)
print(stuff)
# >>>  ['book', 99]

stuff.append('cookie')
print(stuff)
# >>>  ['book', 99, 'cookie']
'''

# Is something in a List?

'''
Searching a list

Python provides two operators that let you check if an item
is in a list

These are logical operators that return True or False

They do not modify the list

'''
'''
some = [1, 9, 21, 10, 16]
9 in some
# >>> True

15 in some
# >>> False

20 not in some
# >>> True

'''

# Lists are in Order

'''
A list can hold many items and keeps those items in the order
unitl we do something to change the order

A list can be sorted (i.e., change its order)

The sort method (unlike in strings) means 'sort yourself'

'''
'''
friends = ['John', 'Donald', 'Evan']
friends.sort()
print(friends)
# >>> ['Donald', 'Evan', 'John']

print(friends[1])
# >>> ['Evan']

'''

# ----------------------------------
# Video 8.3 - Lists and Strings
# ----------------------------------


# Using the Split method

'''
Split breaks a string into parts and produces a list of strings.

We think of these as words. We can access a particular word or
loop through all the words.

'''
'''
abc = 'With three words'
stuff = abc.split()
print(stuff)
# >>> ['With', 'three', 'words']

print(len(stuff))
# >>> 3

print(stuff[0])
# >>> With

for w in stuff :
    print(w)
# >>> With
# >>> three
# >>> words

'''

'''
When you do not specify a dilimiter, multiple spaces are
treated like one delimiter

You can specify what delimiter character to use in the splitting.
'''
'''
line = 'A lot                     of spaces'
etc = line.split()
print(etc)
# >>> ['A','lot', 'of', 'spaces']

line = 'first;second;third'
thing = line.split()
print(thing)
# >>> ['first;second;third']

print(len(thing))
# >>> 1

thing = line.split(';')
print(thing)
# >>> ['first', 'second', 'third']

print(len(thing))
# >>> 3


line = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
words = line.split()
print(words)

fhand = open('mbox-short.txt')
for line in fhand :
    line = line.rstrip()
    if not line.startswith('From ') : continue
    words = line.split()
    print(words[2])
'''

# The Double Split Pattern

'''
Sometimes we split a line one way, and then grab one of the
pieces of the line and plit that piece again

'''

line = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
words = line.split()
email = words[1]
# >>> stephen.marquard@uct.ac.za

pieces = email.split('@')
# >>> ['stephen.marquard', 'uct.ac.za']

print(pieces[1])
# >>> 'uct.ac.za'


