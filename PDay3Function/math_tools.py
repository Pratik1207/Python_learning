# Mini Math Module

# Create a file named math_tools.py and put these functions inside it:
# add(a, b)
# subtract(a, b)
# multiply(a, b)
# divide(a, b)
# factorial(n)
# Then create another file and import math_tools to use these functions.


def addition(a,b):
    return a+b

def subtraction(a,b):
    return a-b

def multiplication(a,b):
    return a*b

def division(a,b):
    return a/b

def factorialCalculator(number):
    fact = 1
    for n in range(1, number+1):
        fact = n * fact
    return fact