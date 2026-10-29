# 2. Sum of Digits
# - Take a number as input from the user
# - Calculate and print the sum of its digits
# - Example: Input `123` → Output `6` (1+2+3)

num = int(input("Enter a nuber to calculate its sum of digits. "))

sum = 0

while num > 0:
    sum = sum + (num % 10)
    num = num//10

print(f"Your Sum of digits are {sum}")