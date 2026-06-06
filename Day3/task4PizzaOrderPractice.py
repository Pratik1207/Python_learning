# Pizza order 

print("Welcome to Python Pizza Deliveries!!")

size = input("What size pizza do you want? S,M or L: ")

pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")

extra_cheese = input("Do you want extra cheese? Y or N: ")

# small ; 15

# M : 20

# L ; 25


# add pepporoni for S + 2

# add pepperoni for M or L +3 

# extra cheese +1

# calculate final bill

# if size == "S":
#     if pepperoni == "Y":
#         if extra_cheese == "Y":
#             print(f"Your final bill is: ${18}")
#         else:
#             print(f"You final bill is: ${17}")
#     else:
#         if extra_cheese == "N":
#             print(f"Your final bill is: ${15}")
# elif size == "M":
#     if pepperoni == "Y":
#         if extra_cheese == "Y":
#             print(f"Your final bill is: ${24}")
#         else:
#             print(f"You final bill is: ${23}")
#     else:
#         if extra_cheese == "N":
#             print(f"Your final bill is: ${20}")
# else:
#     if pepperoni == "Y":
#         if extra_cheese == "Y":
#             print(f"Your final bill is: ${29}")
#         else:
#             print(f"You final bill is: ${28}") 
#     else:
#         if extra_cheese == "N":
#             print(f"Your final bill is: ${25}")


# cleaner code

bill = 0

if size == "S":
    bill = bill + 15
elif size == "M":
    bill = bill + 20
elif size:
    bill = bill + 25
else:
    print("Wrong Input")

if pepperoni == "Y":
    if size =="S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}")
