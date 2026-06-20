# Stone Paper Sciscor

import random

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissor."))

rock = '''    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

scissor = '''   _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

'''

print(f"Your Choice is: {choice}\n")

if choice == 0:
    print(rock)
elif choice == 1:
    print(paper)
else:
    print(scissor)


computerChoice = random.randint(0,1)

print(f"Computer Choice is : {computerChoice}\n")

if computerChoice == 0:
    print(rock)
elif computerChoice == 1:
    print(paper)
else:
    print(scissor)

if computerChoice == choice:
    print("You win")
else:
    print("You loose")