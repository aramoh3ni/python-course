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

# Looping Through a Dictionary
# Python Allow us to loop to get items of dictionary 
# users = {
#     "usrname": "efermi",
#     "first": "enrico",
#     "last": "fermi"
# }
# get value and key of a dic
# item() method return both key and value
# for key, value in users.items():
    # print(f"The key is: {key} and value is: {value}")
# Get only value of a dic
# key() method is useful when you don't need to work with all of
# the values in a dictionary
# key() method allow us to find out if a articular person was polled for example
# for name in users.keys():
    # print(name.title())

# Looing through a dictionary's key in a particular order
# for value in sorted(users.keys()):
    # print(value)

# Looping through all values in dictionary
# return all values of each key
# for value in users.values():
#     print(value)

# NOTE:: we can build a set dicrectly using braces and seprating the elements with cammas,
# languages = {"python", "ruby", "java", "c#", "c++"}
# for lang in languages:
#     print(lang)

# NESTING
# we we want to store multiple dictionaries in a list, or a list of items as value in a dictionary

# A list of Dictionaries
# dic_0 = {"fname": "alireza", "lname": "mohseni", "age": 23, "status": False}
# dic_1 = {"fname": "ali madad", "lname": "nawid", "age": 25, "status": True}

# users = [dic_0, dic_1]
# for user in users:
#     print(user['fname'].title() + " " + user['lname'].title())
#     print(user.values())

# A list inside a dictionaries
# dic_0 = {
#     "fname": "alireza",
#     "lname": "mohseni",
#     "phones": [
#         748482555,
#         704788403,
#         202201093
#     ]
# }

# print(dic_0['fname'])
# print(dic_0['lname'])
# for phone in dic_0['phones']:
#     print(f"Phone: {phone}")

# NOTE:: we sould not nest lists and didctionaries too deeply.
# if we nesting items much deeper than what you see in the preceding expamples or you're working with someone else;s code with significant levels of nesting, most likly a simple way to solve the problem exits

# A Dictionary In A Dictionary

# users = {
#     "alirezamohseni_778854203": {
#         "fname": "alireza",
#         "lname": "mohseni",
#         "phone": 704788403
#     },
#     "karimalawi_88503878489": {
#         "fname": "karim",
#         "lname": "alawi",
#         "phone": 748482555
#     }
# }


# for user in users.values():
#     print(user['fname'])
#     print(user['lname'])
#     print(user['phone'])