# Tip calculator

print("Welcome to the Tip Calculator!")

bill = float(input("what was the total bill? $"))

tip = int(input("How much tip would you like to give? 10, 12 or 15? "))

no_of_person = int(input("How many person to split the bill?"))

total_bill = (bill + ((tip/100) * bill))

each_person_amount = (total_bill/no_of_person)

print(f"Each person should pay: ${round(each_person_amount, 2)}")
