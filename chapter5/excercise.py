# Conditions in Python
# NOTE:: Excercise 1

# name = "hamid"
# print(car == "hamid") # True
# print(car == "jawid") # False

# names = ["Alireza", "Karim", "Ahmad"]
# for name in names:
#     input_value = input("enter a name: ").lower()

#     if input_value == name.lower():
#         print("your chess match!!! 😮‍💨")
#         break
#     else: 
#         print("Not Match Sorry!!!")
#         input_value = ""

# def error_message(line_number: int, message: str) -> str:
#     line = line_number + 1
#     return f'(L{line:03d}) {message}'

# print(error_message(21, "confirm the vlaue"))

# NOTE:: Excercise 2

# alien_color = input("Shoot to color point [red], [yellow], [green]: ")
# point = 0
# if alien_color == 'green':
#     print("You have Earned {} points. 🥳".format(point + 5))
# elif alien_color == 'yellow': 
#     print("You have Earned {} points. 🥳".format(point + 10))
# elif alien_color == 'red':
#     print("You have Earned {} points. 🥳".format(point + 15))

# person_age = int(input("enter your age: "))

# if person_age <= 2:
#     print(f"Person in {person_age} year is baby \n")
# elif person_age >= 4 and person_age <= 13:
#     print(f"Person in {person_age} year is Kid \n")
# elif person_age >= 13 and person_age <= 20:
#     print(f"Person in {person_age} year is teenager \n")
# elif person_age >= 20 and person_age <= 65:
#     print(f"Person in {person_age} year is adult \n")
# elif person_age >= 65:
#     print(f"Person in {person_age} year is an elder \n")

# fevorite_fruits = ['apple', 'orange', 'pinapple', 'banana']

# if 'apple' in fevorite_fruits:
#     print("You really like apple")
# if 'banana' in fevorite_fruits:
#     print('You really like banana')

# NOTE:: Excercise 3
usernames = ['admin', 'aramohseni', 'karimi@', 'homayon_22']
# usernames.clear() # make a list empty
# if usernames:
#     for username in usernames:
#         if username == 'admin':
#             print(f"Hello {username}, would you like to see a status reports?")
#         else:
#             print(f'Hello {username}', "thank you for logging in again.")
# else:
#     print("Please Signup before login, no user!")

# current_users = usernames
# new_users = usernames[0:3]
# new_users.append("hamidi".lower())
# new_users.append("Javadi".lower())

# for user in new_users:
#     if user in current_users:
#         print(f"this {user} have been taken. ✂️")
#         continue
#     else: 
#         print(f"adding {user} in to database ... ✔️")

# print("process finished. 🤠")

# for position in range(1, 10):
#     if position == 1:
#         print(f"You got {position}st Position")
#         continue
#     elif position == 2:
#         print(f"You got {position}nd Position")
#         continue
#     elif position == 3:
#         print(f"You got {position}rd Position")
#         continue
#     print(f"You got {position}th Position")