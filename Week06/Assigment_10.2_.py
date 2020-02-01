'''
Assignemnt 10.2 

Write a program to read through the mbox-short.txt 
and figure out the distribution by hour of the day 
for each of the messages. 

You can pull the hour out from the 'From ' 
line by finding the time and then splitting the string 
a second time using a colon.

From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

Once you have accumulated the counts for each hour, 
print out the counts, sorted by hour as shown below.

'''

emailCount = dict()

fname = input('Enter a file name: ')

# Attempt to open file name given
try :
    fhandle = open(fname)
except :
    print('File \''+ fname + '\' does not exist in the directory')
    quit()

# Find lines with "From" in it
for line in fhandle :
    if 'From ' in line :
        words = line.split()

        # Extract the hour timestamp and put into dict
        for word in words :
            if ':' in word :
                time = word[:2]
                emailCount[time] = emailCount.get(time, 0) + 1

# Put dict into list for sorting
lst = list()
for k, v in emailCount.items():
    newTup = (k, v)
    lst.append(newTup)

# Sort list and display results
lst = sorted(lst)
for k, v in lst:
    print(k, v)