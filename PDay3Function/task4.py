# Maximum of Three Numbers

# Write a function that takes three numbers and returns the maximum among them.

print("Enter three number to check the  max.")

num1 = int(input("First Number: "))

num2 = int(input("Second Number: "))

num3 = int(input("Third Number: "))

def maxChecker(a,b,c):
    if a > b and a > c:
        print(f"{a} is max number.")
    elif b > c:
        print(f"{b} is max number.")
    else:
        print(f"{c} is max number.")

maxChecker(num1,num2,num3)