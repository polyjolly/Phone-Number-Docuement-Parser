#John Greim, CT206, 3/18/19, Assignment 6
#Parse file for phone numbers

import re
#Opens the file and stores text inside as data
with open("file.txt") as file:
    data = file.read()
#Stores the found numbers formated using ., -, or spaces between the blocks 
numbers = re.findall("\d{3}[-\.\s]\d{3}[-\.\s]\d{4}", data)
#Finds numbers using parenthesis on area code similar to above
parennumbers = re.findall(".\d{3}.[-\.\s]\d{3}[-\.\s]\d{4}", data)
#Prints numbers
print(numbers, parennumbers)
