# Alireza Mohseni
# 18, May, 2022
# list Lessons
# ------------------------------------------
# list is the important feature of Python
# list elements can contain letters, digits or names
# collection of item in partuicolar order
# list []

names = ['Ali Mohammadi', 'Karimuldin', "Jawed Mohammad", 'Alireza']
motorcycles = ['yamaha', 'suzuki', 'honda']
cars = ['bmw', 'audi', 'toyota', 'subaru']

# display how excally list is.
# print(names)

# access each elements of a list with index
# print(names[3])

# print(names[0].title())
# print(names[1].upper())
# print(names[2].lower())
# print(names[3].title())

# access to last element of a list
# we can access elements form the last index with puting (-) before index 
# puthing (-0) or (0) in index are the smae both are first element of a list
# print(names[-0])

# using individual values for a list
# message = "Hey there 🖐️, {}"
# print(message.format(names[-1].title()))

# Modifying element of a list
# names[0] = "Lambordgani"
# print(names)

# Adding element to the list ussing append() method
# print(names.__len__()) # 4
# names.append("Hamidullah")
# print(names)
# print(names.__len__()) # 5
# using empty list and adding element dynamically
# cars = []
# cars.append("Toyota")
# cars.append("Honda")
# cars.append("Lambordgani")
# cars.append("Benz")
# print(cars)

# Inserting element in the list by index
# we can insert value in every index we want
# print(names[3])
# names.insert(3, "Bookstore")
# print(names[3]) 
# print(names)

# Removing element with del statment
# if we know the the index of element we use del statement
# print(names)
# del names[0]
# print(names)
# We can remove multiple element usign (,)
# del names[0], names[1]
# print(names)

# Removing element with pop() method
# the concept looks like stack
# the concept of stact is last in first out (LF)
# print(names)
# poped_element = names.pop()
# print(poped_element)
# print(names)
# usage for example we bought a list of motorcycles such as Honda
# Suzuki, Yamaha in this list we don't know the last motorcycle we
# owned so we use pop() method
# last_owned = motorcycles.pop()
# message = f"The last Motorcycle i have owned was a {last_owned.title()}"
# print(message)

# Removing items form any posistion in a list
# we can use pop() method and add index of element as argument
# first_owned = motorcycles.pop(0)
# print(first_owned)

# NOTE:: if we want to delete an element from the list and we
# have never will use it we must to use del statement but if 
# we want remove element from the the and no longer it be in the list
# and using it some where we use pop() method

# Removing Element by Value
# if we want to remove some spacific element but we don't now the
# index so we use remove() method and the vlaue as argument 
# print(motorcycles)
# too_expensive = "suzuki"
# motorcycles.remove(too_expensive)
# print(motorcycles)
# message = f"\n{too_expensive.title()} is expensize for me and i can't own that, let\'s try another."
# print(message)
# print(motorcycles)

# Organizin a List
# Sorting a list permanently with the sort() method
# sort() method sort list alphabetically, assume that all the values in the list be lowercase
# print(f"unOrdered List {cars}")
# cars.sort() # a-z
# print(f"Ordered List {cars}")
# We can also sort reversely our list
# cars.sort(reverse=True) # z-a
# print(f"Reverse Ordered List {cars}")

# Sorting a List Temporarily with the sorted() fucntion
# it display our list in a particular order but doesn't affect the actual order of the list
# print(f"not Sorted() fucntion Orders {cars}")
# print(f"Sorted() fucntion Orders {sorted(cars)}")
# print(f"not Sorted() fucntion Orders {cars}")

# Printing a list Reverse Order
# to reverse order a list using revers() method
# print(f"Orginal list {cars}")
# cars.reverse()
# print(f"Orginal list {cars}")

# Finding the length of a list
# we use in 2 methos and function 
# list_name.__len__()
# len(list_name)

# print(names.__len__()) # return int (4)
# print(len(names)) # return int (4)

# NOTE:: len() method starting from 1 not 0 index of list
# so don't use if anyway otherwize get error
# we solve is by puting -1


# Avoiding Index Erros when working with lists
# print(motorcycles)
# print(motorcycles[3])
# print(len(motorcycles))