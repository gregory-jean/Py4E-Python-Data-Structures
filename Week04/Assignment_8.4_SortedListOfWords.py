'''
---------------
Assignment 8.4
---------------

Open the file romeo.txt and read it line by line. 

For each line, split the line into a list of words using the split() method. 

The program should build a list of words. 

For each word on each line check to see if the word is already in the list and if not append it to the list.

When the program completes, sort and print the resulting words in alphabetical order. 

'''

fname = input('Enter a file name: ')
words = list()

try :
    fhand = open(fname)
except :
    print('File name: ', fname, 'not found in directory.')
    quit()

for line in fhand :
    line = line.rstrip()
    # Split each line by word
    x = line.split()

    # Check if word is already in list, add word to the list if not
    for word in x :
        if word in words :
            continue
        words.append(word)
    words.sort()
    

print(words)