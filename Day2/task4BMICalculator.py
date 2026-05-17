# BMI Calculator

print("Welcome to the BMI Calculator")


weight = float(input("Enter your weight: ")) # input returns string and type casted to int

height = float(input("Enter your Height: "))

bmi = (weight/(height*height))

# rounding the number by using the round function: it takes two arguments one that I want to round the 

# and second the up to what decimal place they want to round 

# before rounding the BMI

print(bmi)

rounded_BMI = round(bmi, 3)

print(f"Your BMI is {rounded_BMI}")


# An f-string (formatted string literal) in Python is a string prefixed with f that allows 

# you to embed variables, expressions, and function calls directly inside the string using {}.

# name = "Pratik"
# print(f"Hello, {name}")

# f-string is a way to format strings by inserting values directly inside {} in a string using the f prefix.