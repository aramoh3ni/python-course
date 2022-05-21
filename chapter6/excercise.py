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


glossary = [
    {
        "title": "sort() method",
        "describ": "a method for sorting list  primanitly"
    }, 
    {
        "title": "sorted() function",
        "describ": "a function for sorting list temporarly"
    },
    {
        "title": "get() method",
        "describ": "a method to get value by key, if leave out second argument and key value was emple it will return NONE"
    }
]

for topic in glossary:
    print(topic['title'].upper())
    print(topic['describ'].capitalize() + "\n")