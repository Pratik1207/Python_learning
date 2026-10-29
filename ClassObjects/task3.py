# Student Class
# Create a class Student
# Attributes: name, roll_no, marks
# Method: display_info() that prints student details
# Create 3 student objects and display their information

class Student:
    def __init__(self,name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def displayDetails(self):
        print(f"Name: {self.name}")
        print(f"Roll number: {self.roll_no}")
        print(f"Marks: {self.marks}")

s1 = Student("Anand" , 1, 100)
s1.displayDetails()

s2 = Student("Pratik", 102, 23)
s2.displayDetails()

s3 = Student("Raj", 23, 67)
s3.displayDetails()
