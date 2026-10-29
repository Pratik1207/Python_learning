# Simple Calculator using Functions

# Create a calculator where each operation (add, subtract, multiply, divide) is a separate function.

# Take two numbers and the operation choice from the user.

print("Mini Calculator!!!")

print("Enter two number to perform basic operation.")

num1 = int(input("Enter First number: "))

num2 = int(input("Enter Second number: "))

choice = input("What operations you want to perfomr: Addition, Subtraction, Multiplication or Division: ")

def addition(a,b):
    return a+b

def subtraction(a,b):
    return a-b

def multiplication(a,b):
    return a*b

def division(a,b):
    return a/b

match choice:
    case "Addition":
        res = addition(num1,num2)
        print(f"Your result is: {res}")
    case "Subtraction":
        res = subtraction(num1,num2)
        print(f"Your result is: {res}")
    case "Multiplication":
        res = multiplication(num1,num2)
        print(f"Your result is: {res}")
    case "Division":
        res = division(num1,num2)
        print(f"Your result is: {res}")