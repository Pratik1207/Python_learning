# Randomisation 

# first import the random module

import random

randomInteger = random.randint(1,10)

# print(randomInteger)


randomFloatingNumber = random.random()  # included 0 excluded 1

# print(randomFloatingNumber)

random_float = random.uniform(1, 10)  # generates florating number including 1 and 10

# print(random_float)

# head and tail program 

Number = random.randint(0,1)

if Number == 0:
    print("Head")
else:
    print("Tail")

