# Student Marks Management (Main Program)
# Create an empty dictionary
# Take names and marks of 5 students as input and store them in the dictionary
# Print the student with the highest marks
# Print the average marks of the class

# creating the empty dict named Student

student = {}

# taking name and marks from the user and making name as key and marks as its value.

for i in range(5):
    name = input("Enter the Students' Name: ")
    marks = int(input("Enter the students' Marks: "))
    student[name] = marks

print(student)

highestMarks = max(student.values())

print(f"The highest marks among the Student is: {highestMarks}")

averageMarks = sum(student.values())/5

print(f"The average marks of the class is: {averageMarks}")