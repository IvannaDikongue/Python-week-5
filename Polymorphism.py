# Base class Vehicle
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses should implement this method.")

# Car class inherits from Vehicle
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

# Plane class inherits from Vehicle
class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

# Bike class inherits from Vehicle
class Bike(Vehicle):
    def move(self):
        print("Pedaling 🚴")

# Creating instances of each class
car = Car()
plane = Plane()
bike = Bike()

# Demonstrating polymorphism: each object has its own implementation of move()
car.move()   # Output: Driving 🚗
plane.move()  # Output: Flying ✈️
bike.move()   # Output: Pedaling 🚴
