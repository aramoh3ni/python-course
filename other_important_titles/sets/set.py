#  Alireza Mohseni
# 06/June/2022

# Python Course
# https://w3schools.com/python/python_sets_methods.html

# SET
# Store Muliple Items in a single variable.
# written with curly brackets
# new_set = (1, 3, 3, 4, 5)


# NOTE:: SET
# 1- Unordered.
# 2- Unchangeable but allow to add new item.
# 3- not allow duplicate values.

# the set() constracture
# new_set = set(("applie", "banana", "cherry"))
# print(set_one)

# ---------------------------------------------------------
# Access Items
# thisset = {"apple", "banna", "cherry"}
# # Using for loop
# for x in thisset:
#     print(x)

# print("apple" in thisset) # if avilible return true other wise return false

# ---------------------------------------------------------
# Add to Set Item
# thisset = {"apple", "banna", "cherry"}

# Add Single Item
# thisset.add("orange")
# print(thisset)

# Add Multiple Items
# thisset.update({"kabul", "new york", "tehran"})
# print(thisset)


# ---------------------------------------------------------
# Remove Set of Items

# remove() fucntion
# thisset.remove("apple")
# print(thisset)

# NOTE:: if item we wanna remove() not exists, it will raise an error
# Solution
# dicard() function
# thisset.discard("cucomber")
# print(thisset)

# pop() method
# NOTE:: when using pop() method, we don't know which item will remove.

# clear()
# thisset.clear()
# print(thisset) # empty set

# del Keyword
# del thisset     # delete the set
# print(thisset)

# --------------------------------------------------------
# Join two sets
# There are several ways to join two or more sets in python
# 1- union() method -> return new set containing all items from both.
# 2- update() method -> insert all the items from one set to another.

# set1 = {1, 2, 3}
# set2 = {"a", "b", "c"}

# new_set = set1.union(set2)
# print(new_set)

# set1.update(set2)
# print(set1)


# ---------------------------------------------------------
# Python Collections (Array)
# we have 4 collection data types in Python.

# List =        Ordered,    Changeable,     Allow duplicate
# Tuple =       Ordered,    Unchangeable,   Allow duplicate
# Set =         Unordered,  Unchangeable,   No duplicate
# dictionary =  Unordered,  Changeable,     No duplicate



