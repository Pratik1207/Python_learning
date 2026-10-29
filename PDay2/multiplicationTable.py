# #### 4. Multiplication Table
# - Take a number from the user
# - Print its multiplication table from 1 to 10
# - Example:  
#   5 x 1 = 5  
#   5 x 2 = 10  
#   ...  
#   5 x 10 = 50

num = int(input("Enter number to calculate its Multiplication Tabel: "))

for x in range(1,11):
    res = num * x
    print(f"{num} * {x} = {res}")