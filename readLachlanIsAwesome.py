# readLachlanIsAwesome.py
# written by Jason J Li 
# License see License.txt

# Import python's library for finding text with regular expressions
import re


# Read LachlanIsAwesome.txt
# Count how many times the expected text appears
counter = 0;
f = open("LachlanIsAwesome.txt", "r")
for line in f:
    if re.search("Lachlan is awesome", line) != None:
        counter+=1

if counter == 0:
    print("\"Lachlan is awesome\" did not appear.")
elif counter == 1:
    print("\"Lachlan is awesome\" appeared once.")
else:
    print("\"Lachlan is awesome\" appeared " + str(counter) + " times.")
