'''
--------------
Assignment 8.5
--------------

Open the file mbox-short.txt and read it line by line. 
When you find a line that starts with 'From ' like 
the following line:

From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

You will parse the From line using split() and print 
out the second word in the line (i.e. the entire 
address of the person who sent the message). 

Then print out a count at the end.

Hint: make sure not to include the 
lines that start with 'From:'.

You can download the sample data at 
http://www.py4e.com/code3/mbox-short.txt

'''
count = None

# Open file handle

inp = input('Enter a file name: ')
try :
    fhand = open(inp)
except :
    print('File \'' + inp + '\' not found in directory.')

for line in fhand :

    # Remove lines starting with 'From:'
    if line.startswith('From:') :
        continue

    # Find remaining lines and print email addresses
    if line.startswith('From') :
        if count == None :
            count = 0
        count = count + 1
        words = line.split()
        print(words[1])

print('There were', count ,'lines in the file with From as the first word')