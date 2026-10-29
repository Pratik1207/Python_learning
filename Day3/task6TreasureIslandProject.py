# Trasure Island

print("Welcome to Treasure Island")

print("Your Mission is to find the treasure.")

print("Your are at cross road. Where do you want to go?")

turn = input("You\'re at cross road. Where do you want to go \"left\" or \"right\"?")

if turn == "right" or turn == "Right" or turn == "RIGHT":
    print("Game Over!!!")
else:
    whatToDo = input("You\'re are at Ocean. You want to \"Swim\" or \"Wait\"?")
    if whatToDo == "swim" or whatToDo == "Swim" or whatToDo == "SWIM":
        print("Game Over!!!")
    else:
        door = input("You\"re at three colored door. Which color door you want to choose: \"Red\", \"Green\" or \"Blue\"?").lower()
        if door == "red":
            print("Game Over!!!")
        elif door == "blue":
            print("Game Over!!!")
        else:
            print("You Win!")