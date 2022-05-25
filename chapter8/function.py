#  Alireza Mohseni
# 25/May/2022
# Python Crash Course

# Function
# Block of code to perfome a particular task
# we should call function to execute the codes inside block
# Mutlipale call == multipale exceute
# Define Function
# def say_hello():
#     return f"Hello dear"
# msg = say_hello()
# print(msg)

# Passing Information to Function
# def say_hello(name):
#     return f"Hello dear, {name}"

# msg = say_hello("Alireza")
# print(msg)

# Argument and Parameters
# def get_full_name(fname, lname): # Parameters
#     return f"{fname} {lname}"

# full_name = get_full_name("Alireza", "Mohseni") # Arguments
# print(full_name)

# Passing Arguments
# Positional Arguments
# def describ_pet(animal_type, pet_name):
#     """Display information about a pet"""
#     print(f"\nI have a {animal_type}")
#     print(f"My {animal_type}'s name is {pet_name.title()}")

# describ_pet("hamster", "harry")

# Multiple Function Calls
# def describ_pet(animal_type, pet_name):
#     """Display information about a pet"""
#     print(f"\nI have a {animal_type}")
#     print(f"My {animal_type}'s name is {pet_name.title()}")

# describ_pet("hamster", "harry") # 1
# describ_pet("dog", "Willie") # 2

# NOTE:: Order Matters in Positional Arguments
# we get unexpected results if we mix up the order of the arguments

# def describ_pet(animal_type, pet_name):
#     """Display information about a pet"""
#     print(f"\nI have a {animal_type}")
#     print(f"My {animal_type}'s name is {pet_name.title()}")

# describ_pet("harry", "hamster")

# Keywor Arguments
# keyword argument is name-value - directly associate the name and the value within the argument
# no confusion in passing arrguments
# def say_hello(name, lname):
#     """return string, greeting some one"""
#     return f"your name is: {name} \nyour last name is {lname}"

# print(say_hello(lname="Mohseni", name="Alireza"))
# no confusion
# no order matters

# Default Value
# If we didn't pass argument we can use default value inside fucntion infront of inistialzion value of each parameter
# def you_name(name = "Joe"):
#     return f"Hello Dear, {name}"

# print(you_name("Alireza"))

# Equvalent function calls
# NOTE:: it doesn't realy matter which calling style we use.
# As logn our function calls produce the output you want, just the style you find easeiset to understant
# print(say_hello(name="Alireza", lname="Mohseni"))
# print(say_hello(lname="Mohseni", name="Alireza"))
# print(say_hello("Alireza", "Mohseni"))
