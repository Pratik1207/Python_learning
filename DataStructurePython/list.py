# List Practice
# Create a list of 5 numbers
# Add a new number
# Remove one number
# Print the list, length, maximum and minimum

numberList = [23,56,35,8,44,3]

print("Numbers in List.")

for x in numberList:
    print(x)

# adding number in list

numberList.append(234)

print("Updated list: ")

for x in numberList:
    print(x)

# removing number from list

numberList.pop()

print("Removing last number from list: ")

for x in numberList:
    print(x)

print("Length of list:")

print(len(numberList))

print("Max number in List: ")

print(max(numberList))

print("Min number in List: ")

print(min(numberList))

numberList.insert(4,4556)

for x in numberList:
    print(x)

numberList.remove(3)

for x in numberList:
    print(x)

