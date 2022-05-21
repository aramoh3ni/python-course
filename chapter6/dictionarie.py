# Alireza Mohseni
# 21/May/2022
# Python Crash Course

# DICTIONARIES
# it look like an object syntax in javascrpt or other plangs
# in python dictionary is a collecion of key-value pairs. each is connected to a value, and you can use a key to access the value associated with that key.

# Describtion
# -> ordered
# -> changable
# -> no duplicate

# alien_0 = {'color': 'red', 'points': 3, 'speed': ''}

# access to each element by key
# print(alien_0['color'])

# Adding new value to dic
# alien_0['x'] = 34
# alien_0['y'] = 10
# alien_0['status'] = True
# print(alien_0)

# Modifying values in a Dic
# if alien_0['speed'] == 'slow':
#     x_increment = 1
# elif alien_0['speed'] == 'medium':
#     x_increment = 2
# else: 
#     x_increment = 3
# alien_0['x'] = alien_0['x'] + x_increment
# print(alien_0['x'])

# Removing Key-Value pairs
# completely remove the key with value
# NOTE:: be aware that the deleted key-value pair is removed permanently
# del alien_0['color']
# print(alien_0)

# A Dictionary i Similar Objects
# simple Login system
# users = [
#     {
#         "id": "xyqttssxq23,.8e",
#         "username": "admin",
#         "password": "abc@123",
#         "first_name": "alireza",
#         "last_name": "mohseni",
#         "position": "software developer",
#         'email': "alireza.mohseni.se@gmail.com",
#         "roll": "admin",
#     },
#     {
#         "id": "tssxq2sdf3,.2e",
#         "username": "homayon.afghan",
#         "password": "123@123",
#         "first_name": "homayon",
#         "last_name": "afghan",
#         "position": "correspondent",
#         'email': "homayon.afghan@gmail.com",
#         "roll": "normal"
#     }
# ]

# print("-----Login System------")

# usr = input("Username 🤵: ")
# pwd = input("Password #️⃣ : ")

# for user in users:
#     if usr == user['username'] and pwd == user['password']:
#         print('login Success')
#         print(user)
#     else:
#         print("not success")

# Using Get() method to retrieve the value
# dic = {'name': "alireza", "lname": "mohseni"}
# name = dic.get('name')
# print(name)

# if key is not exists in dic
# name = dic.get('point', 'Empty Faild')
# print(name)

# if we leave out second argument in get() method it will return None you no value exits
# name = dic.get('pint')
# print(name) 