# Tuple Practice
# Create a tuple of 5 fruits
# Try to change one value (observe the error)
# Print the tuple and access elements using indexing

# tuple creation

fruits = ("Banana", "Orange", "Cherry", "Mango", "Apple")

# fruits.insert("papaya")

print(fruits)

for x in fruits:
    print(x)

# Adding element in tuple by changing tuple into list and then changing back to the tuple

y =  list(fruits)

y.append("Papaya")

fruits = tuple(y)

print("After adding item in tupel using the list: ")

print(fruits)

print(type(fruits))