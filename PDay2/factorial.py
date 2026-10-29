# 3. Factorial of a Number
# - Take a number from the user
# - Calculate its factorial using a loop
# - Example: Input `5` → Output `120` (5×4×3×2×1)

num = int(input("Enter a number to calculate its factorial: "))

fact = 1

print("Using While loop:")


if num > 0:
    while num > 0:
        fact = fact * num
        num = num - 1
    print(f"Your Factorial is {fact}")
else:
    print("Factorial is 0")


# print("Using For loop:")

# num1 = int(input("Enter a number to calculate its factorial: "))


# if num1 > 0:
#     for x in range(num1,0):
#         fact = fact * x
#     print(f"Your Factorial is {fact}")
# else:
#     print("Factorial is 0")
