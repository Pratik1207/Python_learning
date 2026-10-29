# 1. Number Guessing Game
# - Create a secret number (you can hardcode it, e.g. 7)
# - Keep asking the user to guess the number
# - Tell the user if their guess is **too high** or **too low**
# - Stop only when the user guesses correctly
# - (Optional) Count the number of attempts

seceretNumber = 6

print("Guess the number between 0 to 10")

guess = 0

count = 0

while guess != seceretNumber:
    guess = int(input("Enter your Number"))
    count += 1
    if guess < seceretNumber:
        print("Too Low")
    elif guess > seceretNumber:
        print("Too High")
    elif guess == seceretNumber:
        print(f"Your Guessed Correct!!! and your guess count is {count}")