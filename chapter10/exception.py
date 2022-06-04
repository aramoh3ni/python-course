# Alireza Mohseni
# 04/June/2022

# Python Crash Course

# Exceptions
# Python uses special object called exception to manage errors that arise during a program's execution.

# it creates an exception object. 
# if you write code that handles the exception, the program will continue running.
# if not handle the exception, the program will halt and show a traceback, which include a report of the exception that was raised.

# try-exception blocks. asks Pythonto do something, but it also tells Python what to do if an exceptin is raised.

# ------------------------------------------------------------
# Handling the ZeroDivisionError Exception
# print(5/0) # ZeroDivisionError: division by zero

# ------------------------------------------------------------
# Using Try-except Blocks 
# try: 
#     print(5/0)
# except ZeroDivisionError:
#     print("You Can't divide by Zero (0)")

# ------------------------------------------------------------
# Using Exceptions to prevent Crashes.
# Handling errors correctly is especially important when the program has more work to do after the error occurs. 

# print("Give me two numbers, and I'll divide them.")
# print('Enter q to quit program.')

# while True:
#     first_num = input("\n Enter First Number: ")
#     if first_num == 'q':
#         break
#     second_num = input("\n Enter Second Number: ")
#     if second_num == 'q':
#         break
#     try:
#         answer = int(first_num) / int(second_num)
#     except ZeroDivisionError:
#         print("You can't divide by ziro")
#     else:
#         print(f"Answer is: \t{answer}")

# -------------------------------------------------------------
# The Else Block
# if in try-except block code handle successfully, then program will automaticlly run the else: block. it alwaye can be the result of programe.

# try:
# except <error_type>:
# else:

# -------------------------------------------------------------
# Handln the FileNotFoundError Exception

# filename = "something.txt"
# try:
#     with open(filename) as f:
#         contents = f.read()
# except FileNotFoundError:
#     print("File Not Found")
# except FileExistsError:
#     print("File Exists Before")
# else:
#     print(contents)

# def count_words(filename):
#     try:
#         with open(filename) as file_obj:
#             contents = file_obj.read()
#     except FileNotFoundError:
#         pass
#     else:
#         num_chars = len(contents.strip())
#         words = contents.split()
#         num_words = len(words)
#         print(f"This File contains {num_words} words and {num_chars} Character.")

# count_words("learning_python.txt")