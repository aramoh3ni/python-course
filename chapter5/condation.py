# Alireza Mohseni 
# 22/May/2022
# Python Crash Course

# Chapter 5 - If Statements
# for example chage correctness of programm
computers = ['dell', 'mac', 'toshiba', 'samsung']
# for pc in computers:
#     if 'dell' in pc:
#         print(pc.upper())
#         continue

#     print(pc)

# Condition Check
# car = "bmw"
# print(car == "bmw")
# print("bmw" in car)

# Ignoring case whem checking for equality
# python is casesensitive then if "ali" AND "Ali" or different
# if we check those are not equal so the solution is when user enter
# the input we must to make it uppercase or lower case and it will 
# #improve our code

# Checking to inequality (!=) or (not in)
# for pc in computers:
#     if input("enter Value") != computers: # not in 
#         print("Value not Match!!!")
#         print("Try Agin \n")
#     else:
#         print("Value Match 🤭")
#         break

# Numerical Coparisons
# age = 18
# print(age == 18)

# Checking multiple conditions
# age_0 = 22
# age_1 = 20
# print(age_0 >= 21 and age_1 >= 21)
# print(age_0 >= 21 or age_1 >= 21)

# Using Multiple elif Blocks
# user_submit_type = "pro"
# if user_submit_type == "student":
#     university_email = input("Enter Your University Email Address: ")
# elif user_submit_type == "teacher":
#     university_email = input("Please Enter Your University Email: ")
# elif user_submit_type == "community":
#     print('Some rolls may be disbale for you !!! 😭')
# elif user_submit_type == "pro":
#     email = input("Enter Your Email Address: ")
#     first_name = input("Enter Your First Name: ")
#     last_name = input("Enter Your Last Name: ")
#     print("😎 Link to download your software have been sent to your email address")
#     print(f"💗 Thank you Dear, {first_name} {last_name}. have nice day")

# Omitting the else Block
# Python does not require an else block at the end of an if-elif chain
# for value in range(1, 11):
#     """Not require for else"""
#     if value == 10:
#         print("Maximam values of 10")
#         continue
#     elif value == 5:
#         print("Middle of values")
#         continue
#     elif value == 1:
#         print("Minimam of values 1")
#         continue
    
#     print(value)

# Testing Multiple Conditions
# if-elif-else is powerfull but it just only for one test to pass
# we use if statment for testing multiple conditions
# require_topices = ['mushrooms', 'extra cheese']

# if 'mushrooms' in require_topices:
#     print("Adding myshrooms.")
# if 'pepperoni' in require_topices:
#     print("Adding pepperoni.")
# if 'extra cheese' in require_topices:
#     print("Adding Extra cheese")

# print('\nFinised making you pizza')

# Checking for special items
# requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

# for value in requested_toppings:
#     if value == 'green peppers':
#         print("Sorry, we care out of geen peppers right now")
#         continue

#     print(f"Adding {value.title()}.")

# print('\nFinised making you pizza')

# Checking that a list is not empty
# requested_toppings = []
# if requested_toppings:
#     for value in requested_toppings:
#         if value == 'green peppers':
#             print("Sorry, we care out of geen peppers right now")
#             continue
#         print(f"Adding {value.title()}.")
#     print('\nFinised making you pizza')
# else:
#     print('Are you sure you want a pain pizza?')

# Using Multiple lists
# available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
# requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
# for requested_topping in requested_toppings:
#     if requested_topping in available_toppings:
#         print(f"Adding {requested_topping}")
#     else:
#         print(f"Sorry, we don't have {requested_topping}")
# print('\nFinished making your pizza')

# 