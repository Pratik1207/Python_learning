# Stone Paper Sciscor

import random

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissor: "))

rock = '''   
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

scissor = ''' 
    _______
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

# ✅ Invalid input handling
if choice < 0 or choice > 2:
    print("You entered an Invalid Number.")
else:
    game_choice = [rock, paper, scissor]
    
    print("Your Choice is:")
    print(game_choice[choice])


    # if choice == 0:
    #     print(rock)
    # elif choice == 1:
    #     print(paper)
    # else:
    #     print(scissor)

    computerChoice = random.randint(0, 2)

    print("Computer Choice is:")
    print(game_choice[computerChoice])

    # if computerChoice == 0:
    #     print(rock)
    # elif computerChoice == 1:
    #     print(paper)
    # else:
    #     print(scissor)

    # if computerChoice == choice:
    #     print("It is a draw.")
    # elif choice == 0 and computerChoice == 1:
    #     print("You Lose!!!")
    # elif choice == 0 and computerChoice == 2:
    #     print("You Won!!!")

    # elif choice == 1 and computerChoice == 0:
    #     print("You Won!!!")
    # elif choice == 1 and computerChoice == 2:
    #     print("You Lose!!!")

    # elif choice == 2 and computerChoice == 0:
    #     print("You Lose!!!")
    # elif choice == 2 and computerChoice == 1:
    #     print("You Won!!!")

    if (choice == 0 and computerChoice == 2) or (choice == 1 and computerChoice == 0) or (choice == 2 and computerChoice == 1):
        print("You Win!!!")
    elif computerChoice == choice:
        print("It is a draw.")
    else:
        print("You Lose!!!")