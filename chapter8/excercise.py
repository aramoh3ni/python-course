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