# ---------------------------------
#       Video 7.1 - Files
# ---------------------------------

# Opening a File

'''
Before we can read the content of the file, we must tell Python
which file we are goingr to work with and what we will be doing 
with the file.

This is done with the open() function

open() returns a 'file handle' - a variable used to perform
operations on the file

Similar to 'File -> Open' in a Word Processor

'''

count = 0

xfile = open('mbox-short.txt')
for cheese in xfile :
    count = count + 1
    cheese = cheese.rstrip()
    if cheese.startswith('From: ') :
        print(cheese)


print('Line count:', count)
