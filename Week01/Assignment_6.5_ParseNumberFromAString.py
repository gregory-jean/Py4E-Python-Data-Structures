'''
Assigment 6.5 

Write code using find() and string slicing (see section 6.10) to extract 
the number at the end of the line below. 

text = "X-DSPAM-Confidence:    0.8475";

Convert the extracted value to a floating point number and print it out.

'''

text = "X-DSPAM-Confidence:    0.8475"

# Find where the number starts
startpos = text.find(':')

# Assign number to a variable
number = text[startpos + 1 :]

# Remove whitespace and print number
cleanNumber = number.strip()

# Change number to a float
inumber = float(cleanNumber)
print(inumber)
