# for using range

# syntax: for number in range (a, b, c): including a and excluding b: c = increased by
            # print(number)

# range function is used in conjuction of another 

for number in range(1,10):
    print(f"{number}\n")

print("\n")

for number in range(1, 10, 3):
    print(number)

# sum number from 1 to 100 using range and for loop

total = 0

for num in range(1, 101):
    total += num

print(total)