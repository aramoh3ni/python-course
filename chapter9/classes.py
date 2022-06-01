# Alireza Mohseni
# 31/May/2022
# Python Crash Course

# NOTE:: CLASSES
# Object-oriented programming is one of the mose effective approaches to writing soft-ware. 
# in OOP we write (classes) that represent real-world things and situations, and we create (objects) based on the classes.

# Making an object from a class is called instantioation
# and we work with instnaces in class.

# we store our classes as module and import them every where we need them.

# Creating And Using Class
# from dog import Dog

# x = Dog("Afghan",3)
# x.sit()
# x.roll_over()

# the __init__() Method
# called constructor
# python runs automatically whenever we create a new instance of class

# Createing Instace from a class
# from dog import Dog
# dog = Dog("tom", 1.5) # Creating Instance of a class or creating object of a class

# Accessing Attributes
# new_dog = Dog("tom", 2)
# print(new_dog.name) # Access class attributies.

# Calling Methods
# new_dog = Dog("tom", 2)
# new_dog.sit() # call functions inside class

# Creating Multiple Instances
# first_dog = Dog("tom", 2)
# second_dog = Dog("petee", 1)

# print(first_dog.name)
# print(second_dog.name)


# Working with classes and instances
# class Car:
#     """A simple attempt to represent a car."""

#     def __init__(self, make, model, year):
#         """Initialize attributes to describe a car."""
#         self.make = make
#         self.year = year
#         self.model = model
    
#     def get_descriptive_name(self):
#         """Return a neatly formatted descriptive name."""
#         long_name = f"{self.year} {self.make} {self.model}"
#         return long_name.title()


# new_car = Car("Toyota", "GTR", "2021")

# print(new_car.get_descriptive_name())
# --------------------------------------------------------------
# Setting a default Value for an Attribute
# class Car:
#     """A simple attempt to represent a car."""

#     def __init__(self, make, model, year):
#         """Initialize attributes to describe a car."""
#         self.make = make
#         self.year = year
#         self.model = model
#         self.odometer_reading = 0 # Default value 
    
#     def get_descriptive_name(self):
#         """Return a neatly formatted descriptive name."""
#         long_name = f"{self.year} {self.make} {self.model}"
#         return long_name.title()

#     def read_odometer(self):
#         """Print a statement showing the car's mileage."""
#         print(f"This car has {self.odometer_reading} miles on it.")

#     def set_odometer(self, mileage): # Modifying an attribute's value through a method
#         """Set the odometer reading to the given value."""
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You can't roll back an odometer!")

#     def increment_odometer(self, miles): # Increment an attribut's value through a method
#         """Add the given amount to the odometer reading."""
#         self.odometer_reading += miles


# new_car = Car("Toyota", "GTR", "2021")

# print(new_car.get_descriptive_name())
# new_car.read_odometer()

# --------------------------------------------------------------
# Modifying Attributes values
# We can change and attribute's value in three ways:
# 1. Directly through an instance
# 2. Set the value through a method
# 3. Increment the value (add a certain amount to it)

# --------------------------------------------------------------
# Modifing an attributs Value Directly

# new_car = Car("audi", "a4", 2019)
# print(new_car.get_descriptive_name())
# new_car.read_odometer() # 0

# new_car.odometer_reading = 102
# new_car.read_odometer() # 10
# --------------------------------------------------------------
# Modifing and attribute's value through a method
# Example inside class
# new_car.set_odometer(1)
# new_car.read_odometer()

# --------------------------------------------------------------
# Increamnting an Attribute's value through a method
# Example inside Car Class
# new_car.increment_odometer(100)
# new_car.read_odometer()