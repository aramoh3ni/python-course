# NOTE:: Excercise 1
# filename = "learning_python.txt"
# with open(filename) as file_obj:
#     lines = file_obj.readlines()

# for line in lines:
#     print(line.strip())

# with open(filename) as file_obj:
#     for line in file_obj:
#         line.replace("Python", "C#")
#         print(line.rstrip())

# NOTE:: Excercise 2

# msg = "Hello Dear, {} Welcome to our course."
# filename = "guest.txt"

# print("------------------------------------------")
# print("Enter (s) or (show) to display data.")
# print("Enter (e) or (entry) to add new data.")
# print("Enter (q) or (quit) to quit the program.")
# print("------------------------------------------")
# while True:
#     code = input("Please enter the code: ")
    
#     if code == "s" or code == "show":
#         with open(filename) as file_obj:
#             lines = file_obj.readlines()

#         for name in lines:
#             print(msg.format(name.title().strip()))

#     elif code == "e" or code == "entry":
#         users_name = input("Please Enter Your Name: ")
#         with open(filename, 'a') as file_obj:
#             file_obj.write(f"{users_name.lower()} \n")
        
#         print(f"{users_name.title()} add successfuly.")
#         print("Enter (s) or (show) to display data.")

#     elif code == "q" or code == "quit":
#         print("You are loged out!!!")
#         break


# NOTE::  Excercise 3
# print("Enter 2 number i will adding them.")
# try:
#     first_num = int(input("First Number: "))
#     second_num = int(input("Second Number: "))
#     answer = first_num + second_num
# except ValueError:
#     print("Please Enter integar value (numric)")
# else:
#     print(f"{first_num} + {second_num} = {answer}")

# print("=============================================")
# print("Enter (a) for Adding Operation.")
# print("Enter (d) for Divition Operation.")
# print("Enter (q) to quit the program.")
# print("=============================================")
# while True:
#     code = input("Enter the code: ")
#     if code == 'q':
#         break
#     first_num = input("Enter First Number: ")
#     if first_num == "q":
#         break
#     second_num = input("Enter Second Number: ")
#     if second_num == 'q':
#         break
    
#     try:
#         if code == 'd':
#             answer = int(first_num) / int(second_num)
#         if code == "a":
#             answer = int(first_num) +  int(second_num)
#     except ZeroDivisionError:
#         print("You can't divide by ziro")
#     except ValueError:
#         print("Please Enter Valid Number")
#     except NameError:
#         print("Name Error")
#     else:
#         print(f"Answer is: \t{answer}")


# try:
#     filename = "/files/user_info.txt"
#     with open(filename) as fo:
#         c = fo.read()

#     print(c)
# except FileNotFoundError:
#     print("file Not Found")

# NOTE::     Excercise 4
# def set_favorite_number(filename):
#     """set number if file available"""
#     import json
#     numbers = []
#     try:
#        while True:
#             num = input("Enter a number: ")
#             if num == "q": break

#             if num == "e" and len(numbers) <= 0:
#                 print("you did not enter a number yet.")
#                 continue
#             elif num == "e" and len(numbers) > 0:
                
#                 with open(filename, "w") as f:
#                     json.dump(numbers, f)
#                 print("data saved successfully".title())
#                 break;
#             else:
#                 numbers.append(int(num))

#     except FileNotFoundError:
#         print("file not found")
#     except TypeError:
#         print("Enter value integar number")
    

# def get_favorite_numer(filename):
#     """Get stored number if avilibale"""
#     import json
#     try:
#         with open(filename) as f:
#             numbers = json.load(f)
#     except FileNotFoundError:
#         print("file not found")
#     else: 
#         print("All favorite Number")
#         for num in numbers:
#             print(f"- {num}")

# print(set_favorite_number("numbers.json"))
# print(get_favorite_numer('numbers.json'))

# import json

# def user_greeting(username):
#     """print greeting message"""
#     print(f"Dear {username}, welcome back ❤️‍🔥")

# def add_new_username():
#     """Add New Username if not existed yet."""
#     username = input("Enter your new username: ")
#     try:
#         with open('users.json', 'w') as file_obj:
#             json.dump(username, file_obj)
#     except FileNotFoundError:
#         print("File Not Found")
#     else:
#         print(f"{username.title()} we will remember you at next login: 🙂")

# def get_username():
#     """Get single store username in json file"""

#     try:
#         with open("users.json") as file_obj:
#             username = json.load(file_obj)
#         operation = input(f"is @{username} user last username? (y/n)")
#         if operation == 'y': 
#             user_greeting(username)
#         else:
#             add_new_username()
#     except FileNotFoundError:
#         print("file Not Found")


# get_username()