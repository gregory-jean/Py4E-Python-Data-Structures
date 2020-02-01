# --------------------------------
#       Video 6.1 - Strings
# --------------------------------

'''
We cab get at any single character in a string
using an index specified in square brackets []

The index value must be an integer and starts at
zero

The index value can be an expression that is 
computed

'''
'''
fruit = 'banana'
letter = fruit[1]
print(letter)
# >>> a

x = 3
w = fruit[x - 1]
print(w)
# >>> n

y = len(fruit2)
print(y)
# >>> 6
'''

# Looping Through Strings

''' 

While Loop

fruit = 'banana'
index = 0
while index < len(fruit) :
    x = fruit[index]
    print(index, x)
    index = index + 1



For loop

fruit = 'banana'
for letter in fruit :
    print(letter)

'''

# Looping and counting
'''
This is a simple loop that loops
through each letter in a string
and counts the number of times
the loop encounters the 'a'
character
'''
'''
word = 'banana'
count = 0
for letter in word :
    if letter == 'a' :
        count = count + 1
print(count)
'''

# Slicing Strings
'''
We can also look at any contiuous section 
of a string using a color operator.

The second number is one beyond the 
end of the slice - "up to but not including"

If the second number is beyond the end of the 
string, it stops at the end.

If we leave off the first number or the last 
number of the3 slice, it is assumed to be the 
beginning or end of the string respectively.

'''
'''
s = 'Monty Python'
print(s[0:4])
# >>> Mont

print(s[6:7])
# >>> P

print(s[6:20])
# >>> Python

print(s[:2])
# >>> Mo

print(s[8:])
# >>> thon

print(s[:])
# >>> Monty Python

'''


# ------------------------------------------------------
#       Video 6.1 - Manipulating Strings
# ------------------------------------------------------


# Using in as a Logical Operator
'''
The 'in' keyword can also be
used to check to see if one string
is 'in' another string

The in expression is a 
logical expression that returns
True or False and can be used 
in an if statement

'''
'''
fruit = 'banana'
'n' in fruit
# >>> True

'm' in fruit
# >>> False

'nan' in fruit
# >>> True

if 'a' in fruit :
    print('Found it!')
# >>> Found it!
'''

# String Comparison
'''
word = input('Type a phrase: ')

if word == 'banana' :
    print('All right, bananas.')

if word < 'banana' :
    print('Your word,' + word + ',  comes before banana')
elif word > 'banana' :
    print('Your word, ' + word + ', comes after banana')
else :
    print('All right, bananas')

'''

# String Library
'''
Python has a number of string functions which are in the 
string library.

These functions are already built into every string - we
invoke them by apphending the function to the string variable

These functions do not modify the original string, instead they
return a new string that has been altered.

'''

# Changing a strings characters to all lowercase / uppercase
'''
greet = 'Hello Greg'

zap = greet.lower()
print(zap)
# >>> hello greg

print(greet)
# >>> Hello Greg

print('Hi There'.lower())
# >>> hi there
'''

# Searching a string
'''
We use the find() function to search for a substring within
another string

find() finds the first occurrence oif the substring

If the substring is not found, find() reutrns -1

Remember that string position starts a zero

'''
'''
fruit = 'pineapple'
pos = fruit.find('ea')
print(pos)
# >>> 3

aa = fruit.find('z')
print(aa)
# -1

'''

# Search and Replace
'''
The replace() function is a 'search and replace' 
opeation in a word processor.

It replaces ALL OCCURANCES of the search string with
the replacement string

'''
'''
greet = 'Hello Gregory'
nstr = greet.replace('Gregory','Nora')
print(nstr)
# >>> Hello Nora

nstr = greet.replace('o','X')
print(nstr)
# >>> HellX GregXry

'''

# Stripping Whitespace
'''
Sometimes we want to take a string and remove
whitespace at the beginning and/or end

lstrip() and rstrip() remove whitespace at the 
left or right

strip() removes both beginning and ending whitespace

'''
'''
greet = '   Hello Gregory   '
print(greet.lstrip())
# >>> 'Hello Gregory    '

print(greet.rstrip())
# >>> '    Hello Gregory'

print(greet.strip())
# >>> 'Hello Gregory'
'''

# Prefixes

'''
line = 'Please have a nice day'
print(line.startswith('Please'))
# >>> True

print(line.startswith('p'))
# >>> False

'''

# Parsing and Extracting

data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'

atops = data.find('@')
print(atops)
# >>> 21

sppos = data.find(' ',atops)
print(sppos)
# >>> 31

host = data[atops+1 : sppos]
print(host)
# >>> uct.ac.za

x = 'From marquard@uct.ac.za'