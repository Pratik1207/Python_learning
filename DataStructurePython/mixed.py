# Mixed Practice
# Take 10 numbers from the user and store them in a list
# Convert the list into a set (to remove duplicates)
# Convert the set back into a list and sort it
# Print the final sorted list without duplicates


numbers = []

for i in range(9):
    numbers.append(int(input("Enter numbers: ")))

print("The number in list is: ")


for i in range(len(numbers)):
    print(numbers[i])


thisSet = set(numbers)

print("The set is: ")

for i in thisSet:
    print(i)

numbers = list(thisSet)

accendingList = sorted(numbers)

print("The sorted list is: ", accendingList)

