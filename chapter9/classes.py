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

# ==============================================================
# Inheritance
# When on class inherits fro another, it takes on the attributes and methods of the first class.
# Orginal Class = Parent Class
# New Class = Child Class
# when we inherit parent attributes and methods child class is free to have owen methods and properties

# -------------------------------------------------------------
# The __init__() Method for child class
# Main Class
# class Car: 
#     def __init__(self, name, model, year):
#         self.name = name
#         self.model = model
#         self.year = year

#     def set_car(self, name, model, year):
#         self.name = name
#         self.model = model
#         self.year = year

#     def get_car(self):
#         car_info = f"{self.name} {self.model} {self.year}"
#         return car_info.title()

# ------------------------------------------------
# Creating Supret class to define more effictively
# Instances as Attributes
# class Battery:
#     def __init__(self, battery_size = 75):
#         self.battery_size = battery_size

#     def describe_battery(self):
#         print(f"This car has a {self.battery_size}-kWH battery.")

#     def get_range(self):
#         if self.battery_size == 75:
#             range = 260
#         elif self.battery_size == 100:
#             range = 315
        
#         print(f"This car can got about {range} miles on a full charge")

# ------------------------------------------------
# Inherite class
# class ElectricCar(Car):
#     """Represent aspects of a car, specific to electric vehicles"""

#     def __init__(self, name, model, year, price):
#         super().__init__(name, model, year)
#         self.battery = Battery() # Define Attribute for child class and creating object of a class (Battery)
#         self.price = price # Define Attribue for Child class

#     def fill_gas_tank(self):
#         print("This car doesn't need a gas tank")

# my_tesla = ElectricCar("Tesla", "GTR2600", 2022, price=90000)

# print(my_tesla.get_car())
# my_tesla.battery.describe_battery()
# my_tesla.fill_gas_tank()
# my_tesla.battery.get_range()

# --------------------------------------------------
# Instances as Attributes
# When modeling something from the real world in code. we may find that we are adding more and more details to a class. 
# we will find that we have a growing list of attributes and methods and that our files are becoming lengthy. 
# ? Solution
#  we might recognize that part of one class can be written as a separate class.
# we can break our large class into samller classes that work together.
# Example to inside car, battery and electronic class

# ---------------------------------------------------
# Importing Classes
# Python allow us to supreate our class, module in such external files to manage easly our project.
# ---------------------------------------------------
# Import Single Class
# from car import Car

# new_car = Car("Toyota", "GTR", 2019)
# print(new_car.get_descriptive_name())
# new_car.odometer_reading = 24
# new_car.read_odometer()

# ---------------------------------------------------
# Storing Multiple Classes in a module

# from car import ElectricCar

# new_electric_car = ElectricCar("Tesla", "GTR", 2022)
# print(new_electric_car.get_descriptive_name())
# new_electric_car.battery.battery_size = 75
# new_electric_car.battery.get_range()

# --------------------------------------------------
# Import Multiple classes from a module
# from car import Car, ElectricCar

# --------------------------------------------------
# Import an Entire Module
# import car
# new_car = car.ElectricCar("Tesla", "GTR", 2019)
# print(new_car.get_descriptive_name())

# --------------------------------------------------
# Import All Classes from a Module
# from car import *

# NOTE:: from <module_name> import *, is good and helpfull for smal project but it's not recommented for big project because it will lead to confusion with names in the files.

# <module_name>.<class_name> is recommented for this type of importing

# it's recomment to use saperate file to store multiple modules and import in nessasity files.

# --------------------------------------------------
# Using Aliases
# from car import Car as myCar

# --------------------------------------------------
# Thy Python Standard Library
# Python standard library is a set of modules included with every python installation
# We can import them sample by (import) statement
# import random

# int_number = random.randint(10, 100)
# print(int_number)


# --------------------------------------------------
# Styling Classes
# 1- Class name should be in CamelCase.
# 2- Don't use underscore between words.
# 3- every class should have docstring imediately follwing the class definition.
# 4- docstring ("""some text""") should be a bried description of what the class does.
