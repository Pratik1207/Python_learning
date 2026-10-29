# 6. Count Even and Odd Numbers
# - Take 10 numbers as input from the user (using a loop)
# - Count how many numbers are **even** and how many are **odd**
# - Print both counts at the end

odd = 0
even = 0
print("Enter 10 number to check how many are even and odd")

for x in range(10):
    num = int(input(f"Enter number: "))
    if num % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1

print(f"Number of even number {even} and odd number {odd}")