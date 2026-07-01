# sum

student_scores = [78, 85, 92, 67, 88, 73, 95, 81, 69, 90]

# print sum by using sum function 

total = sum(student_scores)

print(total)

# max

maximum = max(student_scores)

print(maximum)

# print sum by using loop

total_score = 0

for score in student_scores:
    total_score += score

print(total_score)

# max using for loop

highest_number = 0

for num in student_scores:
    if highest_number < num:
        highest_number = num

print(highest_number)