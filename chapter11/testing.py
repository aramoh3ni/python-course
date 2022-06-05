# Alireza Mohseni
# 05/June/2022

# Python Crash Course

# Teasing Our Code
# Every programmer makes mistakes, so every programmer must test their code often, catching problems before users encounter them.

# in this chapter we will learn how test our code using tool in Python's (unittest) Module.

# -------------------------------------------------------------
# Testing a Function
# from functions import get_formated_name

# print("Enter your information or enter (q) to quit program.")
# while True:
#     first_name = input("Enter Firstname: ")
#     if first_name == "q": break
#     middle_name = input("Enter Middle: ")
#     if middle_name == "q": break
#     last_name = input("Enter Lastname: ")
#     if last_name == "q": break

#     try:
#         full_name = get_formated_name(first_name.lower(), last_name.lower(), middle_name.lower())
#     except TypeError: 
#         print("Invalid input type.")
#     else:
#         print(f"Hey there! {full_name} welcome back.")