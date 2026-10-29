# 5. Star Pattern
# Print the following pattern using loops:

num = int(input("Enter a number to print star patter: "))

for x in range(num):
    for j in range(x+1):
        print("*", end=" ")
    print()