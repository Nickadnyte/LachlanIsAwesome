# writeLachlanIsAwesome.py
# License see License.txt

# Import python's library for finding text with regular expressions
import re

# Write to LachlanIsAwesome.txt
f = open("LachlanIsAwesome.txt", "w")

# Use a while loop, write "Lachlan is awesome 10 times
counter = 0;
while counter != 10:
    f.write("Lachlan is awesome!\n")
    counter+=1
    print ("Wrote \"Lachlan is awesome!\" " + str(counter) + " times.")

