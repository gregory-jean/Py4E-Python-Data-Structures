'''

--------------
Assignment 7.2 
--------------

Write a program that prompts for a file name, 
then opens that file and reads through the file, 
looking for lines of the form:

X-DSPAM-Confidence:    0.8475

Count these lines and extract the floating point values 
from each of the lines and compute the average of those 
values and produce an output as shown below. 

Do not use the sum() function or a variable named sum 
in your solution.

You can download the sample data at

http://www.py4e.com/code3/mbox-short.txt 

when you are testing below enter 

'mbox-short.txt' as the file name.

'''

Total = 0
Average = 0
Count = 0

# Prompt for file
fName = input('Enter a file name:')

try :
    fHandle = open(fName)
except :
    print('Invalid file name.')
    print('File \'' + fName + '\' does not exist in the curret directory.')
    quit()

# Parse for the correct lines
for line in fHandle :
    if line.startswith('X-DSPAM-Confidence:') :

        # Find amount and strip whitespace
        startPos = line.find(':')
        sAmount = line[startPos + 1 :].strip()
        iAmount = float(sAmount)

        Total = Total + iAmount
        Count= Count + 1

# Calculate average
try :
    Average = Total / Count
except :
    print('No lines in file contain phrase \'X-DSPAM-Confidence:\'')
    quit()


print('Average spam confidence:', Average)