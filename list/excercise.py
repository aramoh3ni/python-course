# NOTE:: EXCERCISE 1
# names = [
#     "Alireza",
#     "Mohsen",
#     "Amir Hussain",
#     "Parisa",
#     "Mohammad ALi",
#     "Layla",
#     "Zakir"
# ]
# Present ech elemet with index and .title() method after
# print(names[0].title())
# print(names[1].title())
# print(names[2].title())
# print(names[3].title())
# print(names[4].title())
# print(names[5].title())
# print(names[6].title())

# print message and put each name a argument of a meesgage
# message = "Hello there, {} hope you are doing well!"
# print(message.format(names[0]))
# print(message.format(names[1]))
# print(message.format(names[2]))
# print(message.format(names[3]))
# print(message.format(names[4]))
# print(message.format(names[5]))
# print(message.format(names[6]))

# NOTE:: EXSERCISE 2
# from datetime import datetime
# now = datetime.now()
# now = str(now).split(" ")

# persons = ["Mohammad Ali", "Jawid", "Taqi"]
# message = "Hello there {}, you are inviding for dinner on {}"


# print(message.format(persons[0].title(), now[0]))
# print(message.format(persons[1].title(), now[0]))
# print(message.format(persons[2].title(), now[0]))

# print("Mohammad Ali can\'t be preent for to night, unfortunatly.")
# new_person = "Hamid"
# persons[0] = new_person

# print(message.format(persons[0].title(), now[0]))
# print(message.format(persons[1].title(), now[0]))
# print(message.format(persons[2].title(), now[0]))

# print ("\nFount bigger dinner")
# first_person = "Amir Hussain"
# second_person = "Eshaq"
# third_person = "Shadab"

# persons.insert(0, first_person)
# middle_of_list = int(persons.__len__() / 2)
# persons.insert(middle_of_list, second_person)
# persons.append(third_person)

# print(message.format(persons[0].title(), now[0]))
# print(message.format(persons[1].title(), now[0]))
# print(message.format(persons[2].title(), now[0]))
# print(message.format(persons[3].title(), now[0]))
# print(message.format(persons[4].title(), now[0]))
# print(message.format(persons[5].title(), now[0]))

# print("\nSorry! You can only invide 2 person but you invide more")
# removed_person = persons.pop()
# print(f"{removed_person} removed from the list, new list ⬇️")
# removed_person = persons.pop()
# print(f"{removed_person} removed from the list, new list ⬇️")
# removed_person = persons.pop()
# print(f"{removed_person} removed from the list, new list ⬇️")
# removed_person = persons.pop()
# print(f"{removed_person} removed from the list, new list ⬇️")

# print(message.format(persons[0].title(), now[0]))
# print(message.format(persons[1].title(), now[0]))

# del persons[-1], persons[-1]
# print("\n Program is done! 😂" + str(persons))
