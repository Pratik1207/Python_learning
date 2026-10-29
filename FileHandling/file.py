# File Writing
# Create a new text file
# Write 5 lines of text into that file
# Close the file properly (preferably using with)

import os

count  = 0


sum = 0

f = open("demo.txt", "x")
f.write("Anyway\nFocus")
f.close()

with open("demo.txt") as f:
    for x in f:
        print(x, end="")

with open("demo.txt", "a") as f:
    f.write("Adding extra sentence:")

with open("demo.txt") as f:
    for x in f:
        print(x)
        sum = len(x.split()) + sum
        count = count + 1

f.close()

print(f"Total word count is: {sum}")
with open("demo.txt") as f:
    print(f.read())

# deleting file

os.remove("demo.txt")