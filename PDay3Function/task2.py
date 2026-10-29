# Even or Odd Function

# Write a function that takes a number and returns whether it is “Even” or “Odd”.

num = int(input("Enter a number to check if it is even or odd: "))

def oddEvenChecker(a):
    if a%2 == 0:
        print(f"{a} is even number.")
    else:
        print(f"{a} is odd number.")

oddEvenChecker(num)