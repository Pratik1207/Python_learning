# list starts with square brackets and between them the items separated by coma

# Syntax: fruits = [item1, item2]  - order is maintained in the list

State_of_India = ["Delhi", "Rajasthan", "Bihar"]

print(State_of_India[1])

# can change the list 

State_of_India[0] = "Goa"

print(State_of_India)

# can add the item in the end of the list

# We use append - add the single item at the end  of the list

State_of_India.append("Sikkim")

print(State_of_India)

# we use the extend function to extend the list

State_of_India.extend(["Himachal Pradesh","J and K", "MP"])

print(State_of_India)

