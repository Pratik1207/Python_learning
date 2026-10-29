import math_tools

print("Enter numbers to calculate addition, sub,multiplication, division and factorial")

num1 = int(input("Enter first number: "))

num2 = int(input("Enter second number: "))

res = math_tools.addition(num1,num2)

print(f"Addition is: {res}")