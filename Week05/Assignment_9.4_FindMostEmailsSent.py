'''
Assignment 9.4 

Write a program to read through the mbox-short.txt 
and figure out who has sent the greatest number of mail messages. 

The program looks for 'From ' lines and takes the 
second word of those lines as the person who sent the mail. 

The program creates a Python dictionary that maps 
the sender's mail address to a count of the number of 
times they appear in the file. 

After the dictionary is produced, the program reads 
through the dictionary using a maximum loop to find 
the most prolific committer.

'''
emailCount = dict()
bigCount = None
bigSender = None

fname = input('Enter a file name: ')

try :
    fhandle = open(fname)
except :
    print('File \'' + fname + '\' does not exist in the directory.')
    quit()

for line in fhandle :

    # Find all lines that begin with From
    if 'From ' in line :
        words = line.split()

        # Extrapolate the sender email
        sender = words[1]

        # Add to count of sender in dictionary, create spot for new sender if not already created
        emailCount[sender] = emailCount.get(sender, 0) + 1

        # Determine which user has sent the most emails
        for sender, amount in emailCount.items() :
            if bigCount is None or amount > bigCount :
                bigCount = amount
                bigSender = sender

print(bigSender, bigCount)