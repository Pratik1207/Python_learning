print("Enter two numbers to Calculate their addtion, subtraction, multiplication and division")

num1 = float(input("Enter first number: "))

num2 = float(input("Enter second number: "))

def myFunction(a, b):
    print("Addition: ", a+b)
    print("Subtraction: ", a-b)
    print("Multiplication: ", a*b)
    print("Division: ", a/b)



myFunction(num1,num2)