# Alireza Mohseni
# 04/June/2022

# Python Crash Course

# Strong data

# Many of our programs will ask users to input certain kinds of information. 
# we might allow users to store preferences in a game or provide data for a visualization. 
# A simple way is (json) module

# The - Json Module - allow us to dump simple python strcutres into a file and load the data from that file the next time the program runs.
# Also we can use Json to share data between different Python programs.abs(
# )

# ===========================================================
# THE JSON is (JavaScript Object Notation) format was originally from JavaScript. However, it has since become a common format used by many languages including PYTHON.
# ===========================================================

# -----------------------------------------------------------
# Using json.dump() and json.load()

# import json
# number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# filename = "numbers.json"
# with open(filename, "w") as file_obj:
#     json.dump(number, file_obj)

# with open(filename) as file_obj:
#     number = json.load(file_obj)

# print(number)

# import json
# name = input("Enter Your Name: ")
# filename = 'users.json'
# with open(filename, "w") as file_obj:
#     json.dump(name, file_obj)
#     print(f"We'll remeber you when you come back, {name}")

# with open(filename) as file_obj:
#     name = json.load(file_obj)
#     print(f"Welcome back, {name}")

# -------------------------------------------------------------
# Refactoring
# makes our code cleaner, easier to understand, and easier to extend.

# we our code imporve code will breaking into a seriers of functions that have specific jobs. so the process called refactoring.

# ------------------------------------------------------------
# Saving and Reading User-Generated Data and Refactoring 

# def get_stored_name(filename):
#     """Get stored name if available and return string"""
#     import json
#     try:
#         with open(filename) as f:
#             name = json.load(f)
#     except FileNotFoundError:
#         print("File not found.")
#     else:
#         print(f"Wellcome Back Dear, {name}")
#         return name

# def add_new_name(filename):
#     """Get new value and store it to file name as parameter."""
#     import json
#     name = input("Enter Your Name: ")

#     try: 
#         with open(filename, 'w') as f:
#             json.dump(name, f)
#     except FileNotFoundError:
#         print("File Not Found")
#     except TypeError:
#         print("Enter valid value")
#     else:
#         print(f"We will remember you, {name}")

# filename = 'users.json'
# add_new_name(filename)
# get_stored_name(filename)