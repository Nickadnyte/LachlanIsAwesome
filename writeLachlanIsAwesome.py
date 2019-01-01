# writeLachlanIsAwesome.py
# License see License.txt


# Write to LachlanIsAwesome.txt
f = open("LachlanIsAwesome.txt", "w")

# Use a while loop, write "Lachlan is awesome 10 times
counter = 0;
while counter != 1000000:
    f.write("Lachlan is awesome!\n")
    counter+=1

