# NOTE:: EXCERCISE 1
# peroson = {
#     "first_name": "Alireza",
#     "last_name": "Mohseni",
#     "age": 22.5,
#     "city": "kabul",
#     "status": True,
#     "favorite_number": 11
# }

# print(f"Firstname: {peroson['first_name']}")
# print(f"Lastname: {peroson['last_name']}")
# print(f"Age: \t{peroson['age']}")
# print(f"City: \t{peroson['city']}")
# print(f"Status: {peroson['status']}")
# print(f"Favorite Numer: {peroson['favorite_number']}")


# glossary = [
#     {
#         "title": "sort() method",
#         "describ": "a method for sorting list  primanitly"
#     }, 
#     {
#         "title": "sorted() function",
#         "describ": "a function for sorting list temporarly"
#     },
#     {
#         "title": "get() method",
#         "describ": "a method to get value by key, if leave out second argument and key value was emple it will return NONE"
#     }
# ]

# for topic in glossary:
#     print(topic['title'].upper())
#     print(topic['describ'].capitalize() + "\n")

# NOTE:: Excercise 2
# glossary = {
#     "sort() method": "a method for sorting list  primanitly",
#     "sorted() function": "a function for sorting list temporarly",
#     "get() method": "a method to get value by key, if leave out second argument and key value was emple it will return NONE",
#     "dictionary": "a collection of data with key-value"
# }

# for k, v in glossary.items():
#     print(f"title: {k}, Describtion: {v}")

# revers = {
#     "nile": "egypt",
#     "aamo": "afghanistan",
#     "harirod": "afghanistan"
# }

# for k, v in revers.items():
#     print(f"{k.title()} is run on {v.title()}")

# favorite_languages = {
#     "ali": "python",
#     "karim": "c",
#     "mahmod": "c#",
#     "zahra": "ruby"
# }

# people = ['ali', 'zahra', 'shir']

# for person in people:
#     if person in favorite_languages.keys():
#         print(f"thank you dear, {person}")
#         continue
#     else:
#         print(f"hey, {person} please take a pole")

# NOTE:: Excercise 3
# people = {
#     "nid": "77888876555",
#     "fname": "alireza",
#     "lname": "mohseni",
#     "passport": "p48393948",
#     "age": 23,
#     "location": "franch"
# }

# for key, value in people.items():
#     print(f"{key.title()}: {str(value).title()}")


# pets = {
#     "ronaldo": "cat",
#     "naymar": "bird",
#     "messi": "dog"
# }

# for owner, pet in pets.items():
#     print(f"{owner.title()} loves to have more {pet.title()}s")

# favorite_palces = {
#     "ronaldo": ["paris", "barcelona", "madrid"],
#     "messi": ["paris", "barcelona", "madrid"],
#     "naymary": ["paris", "barcelona", "madrid"],
#     "alireza": ["kabul", "ghazni", "🤭"]
# }

# for person, place in favorite_palces.items():
#     print(person.title())
#     for city in place:
#         print(f"Love to go {city.title()}")

#     print("\n")


# cities = {
#     "kabul": {
#         'name': "kabul",
#         "country": "afghanistan",
#         "population": 3000000,
#         "point": "asia"
#     },
#     "dubai": {
#         "name": "dubai",
#         "country": "emarates",
#         "population": 500000000,
#         "point": "asia"
#     }
# }

# for kay, value in cities.items():
#     print(f"Name: {value['name'].title()}")
#     print(f"Country: {value['country'].title()}")
#     print(f"Population: {value['population']}")
#     print(f"Located on: {value['point'].title()}\n")

# dic_0 = {"fname": "alireza", "lname": "mohseni", "age": 23, "status": False}
# dic_1 = {"fname": "ali madad", "lname": "nawid", "age": 25, "status": True}

# users = [dic_0, dic_1]
# for user in users:
#     print(user['fname'].title() + " " + user['lname'].title())
#     print(user.values())