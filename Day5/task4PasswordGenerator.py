# password Generator

import random

lower_case_alphabets = [
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z']

upper_case_alphabets = [
    'A','B','C','D','E','F','G','H','I','J','K','L','M',
    'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

numbers = ['0','1','2','3','4','5','6','7','8','9']

symbols = [
    '!','@','#','$','%','^','&','*','(',')',
    '-','_','=','+','[',']','{','}','|',
    ';',':',"'",',','.','<','>','?']

print("Welcome to the pyPassword Generator!!!")

nr_small_letter = int(input("How many small letters you would like in your password?\n"))

nr_capital_letter = int(input("How many capital letter you would like in your password?\n"))

nr_Symbols = int(input("How many symbols you would like?\n"))

nr_numbers = int(input("How many numbers would you like?\n"))

# weak password

password = ""

for char in range(0,nr_small_letter):
    password += (random.choice(lower_case_alphabets))

for char in range(0,nr_capital_letter):
    password += (random.choice(upper_case_alphabets))

for char in range (0,nr_Symbols):
    password += (random.choice(symbols))

for char in range(0, nr_numbers):
    password += (random.choice(numbers))

print(f"your password is:{password}")

# hard password

Strong_password = []

for char in range(0,nr_small_letter):
    Strong_password.append(random.choice(lower_case_alphabets))

for char in range(0,nr_capital_letter):
    Strong_password.append(random.choice(upper_case_alphabets))

for char in range (0,nr_Symbols):
    Strong_password.append(random.choice(symbols))

for char in range(0, nr_numbers):
    Strong_password.append(random.choice(numbers))

print(Strong_password)

strongPassword = ""

random.shuffle(Strong_password)

for char in Strong_password:
    strongPassword += char

print(strongPassword)