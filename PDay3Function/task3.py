# Factorial Function

# Write a function that takes a number and returns its factorial.

num = int(input("Enter a number to calculates its factorial: "))

def factorialCalculator(number):
    fact = 1
    for n in range(1, number+1):
        fact = n * fact
    print(f"Factorial of number is: {fact}")

factorialCalculator(num)