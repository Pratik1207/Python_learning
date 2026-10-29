# Who will pay the bill

import random

friends = ["Navneet", "Pawan", "Tannu", "Lavi", "Vishnu"]

payBill = random.choice(friends) # choice is used to provide us the random name from seq

print(payBill)

# Second method

index = random.randint(0,4)

print(friends[index])

