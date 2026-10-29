# Simple Inheritance (Bonus)
# Create a parent class Animal with a method sound()
# Create a child class Dog that inherits from Animal
# Override the sound() method in Dog

class Animal:
    def sound(self):
        print("Sound of Animal.")

class Dog(Animal):
    def sound(self):
        print("Sound of Dog.")

d1 = Dog()

d1.sound()