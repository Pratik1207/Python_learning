# Set Practice
# Create a set of numbers (with some duplicates)
# Add a new element
# Remove an element
# Print the set (notice duplicates are removed)

# creating set

thisSet = {11,22,12,23,11,5,34,22}

print(thisSet)

for x in thisSet:
    print(x)

# adding elemetn in set

thisSet.add("Apple")

print(thisSet)

thisSet.remove(22)

print(thisSet)