# NOTE:: Excercise 1
# def display_message():
#     print("What you are learning about in this chapter?")

# display_message()

# def favorite_book(title):
#     print(f"You love to read {title} book.")

# favorite_book("Python Crash Course")

# NOTE:: Excercise 2
# def make_shirt(size, message):
#     """retunr string, to front shirt style"""
#     print(f"shirt size: {size}")
#     print(f"shirt text: {message}")

# make_shirt("xl", "I love Python")
# make_shirt(message="I love Python", size="xl")

# def make_shirt(size = 'sm', message='I love Python'):
#     """retunr string, to front shirt style"""
#     print(f"shirt size: {size}")
#     print(f"shirt text: {message}")

# make_shirt()
# make_shirt("xl")
# make_shirt(message="I love Python")

# def describe_city(city, country='United State'):
#     """a function to describe city details"""
#     print(f"{city.title()} is located in {country.title()}")

# describe_city("new york")
# describe_city("Kabul", "Afghanistan")
# describe_city(city="Homborg", country="Germany")


# NOTE:: Excercise 3
# def city_country(city, country):
#     """return city and country name"""
#     return "{}, {}".format(city, country).title()

# print(city_country("kabul", "afghanistan"))

# def make_album(title, artist, songs = None):
#     """return album dictiona object"""
#     album = {
#         "title": title,
#         "artist": artist
#     }

#     if songs:
#         album['songs'] = songs

#     return album


# while True:
#     print("\nEnter you album")
#     title = input("Enter title: ")

#     if title == 'q': break

#     artist = input("Enter Artist: ")
#     songs = input("Enter total Songs: ")


#     ablum = make_album(title, artist, songs)
#     print(ablum)


# NOTE:: Excercise 4
# def show_messages(messages):
#     for msg in messages:
#         print(msg)

# messages = [
#     "Hello for every one",
#     "Please confirm you email address",
#     "Hello you team to grow"
# ]
# show_messages(messages)

# def send_message(messages):
#     sent_messages = []
#     while messages:
#         current_message = messages.pop()
#         sent_messages.append(current_message)
#         print(f"{current_message} is in progress...")
#         print("DONE")
    
#     print("\nALL MESSAGES IS HERE\n")
#     for msg in sent_messages:
#         print(msg)

# send_message(messages)

# NOTE:: Excercise 5
# def sandwich_ingerdiends(*args):
#     print('\nThere are the sandwich ingerdiends: ')
#     for sandwich in args:
#         print(f"- {sandwich.title()}")

# sandwich_ingerdiends()
# sandwich_ingerdiends('salad', 'cucumber', 'chicken')
# sandwich_ingerdiends('salad', 'cucumber', 'chicken', 'pastrami', 'tuna')

# def build_profile(first, last, **kwargs):
#     kwargs['first_name'] = first
#     kwargs['last_name'] = last
#     return kwargs

# my_profile = build_profile(
#     "Alireza",
#     "Mohseni",
#     age=23,
#     country="Afghanistan",
#     education="Bachelor"
# )

# print(type(my_profile))

# def cars(manufacturer, model, **kwargs):
#     kwargs['manufacturer'] = manufacturer
#     kwargs['model'] = model
#     return kwargs

# print(cars("subru", 'outback', color='red', tow_package=True))