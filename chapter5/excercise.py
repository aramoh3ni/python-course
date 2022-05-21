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

fevorite_fruits = ['apple', 'orange', 'pinapple', 'banana']

if 'apple' in fevorite_fruits:
    print("You really like apple")
if 'banana' in fevorite_fruits:
    print('You really like banana')


