# Simple Class and Object
# Create a class named Person
# It should have name and age
# Create two objects of this class and print their details

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def displayDetails(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

p1 = Person("Anand", 25)  #object creation
p1.displayDetails()

p2 = Person("Pratik", 23)
p2.displayDetails()
