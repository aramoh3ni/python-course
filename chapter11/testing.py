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

# -------------------------------------------------------------
# Testing a Class
# we can be confident that improvements we make to the class won't accidentaly break its current behavior.

# -------------------------------------------------------------
# A Variety of Assert Methods

# Python provides a number of assert methods in the (unittest.testCase) Class as mentioned earlier, assert methods test whether a condition we believe is true at a specific point in our code is indeed True.

# if condition is true = we can be confident that no error exists
# if condition is not true = we condident that error accurate.

# ----------------------------------------------------------
# Methods                   Use
# ----------------------------------------------------------
# assertEqual(a, b)         Verify that a == b
# assertNotEqual(a, b)      Verify that a != b
# assertTrue(x)             Verify that x is True
# assertFalse(x)            Verify that x in False
# assertIn(Item, list)      Verify that item is in list
# assertNotIn(Item, list)   Verify that item is not in list

# -----------------------------------------------------------
# A Class Test
# from survey import AnonymousSurvey

# print("Please follow the instraction bellow.")
# print("Enter [show -q] to show question.")
# print("Enter [add] to add your response.")
# print("Enter [show -r] to show all responses.")
# while True:
#     code = input("Enter the code: ")
#     new_survery = AnonymousSurvey("How to become programmer?")
#     if code == "q": break

#     if code == "add": 
#         response = input("Enter you response: ")
#         new_survery.set_responses(response)
#         print("Thank Your for your Response. 💙")
#         new_survery.show_result()

#     if code == "show -r":
#         new_survery.show_result()

#     if code == "show -q":
#         print(new_survery.show_question())
