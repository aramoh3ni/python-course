# Alireza Mohseni
# May/19/2022
# Numerical List

# Making Numerical Lists
# => range() function
# makes it easy to generate a series of number
# for value in range(1, 5):
    # print(value) # 1, 2, 3, 4 with out 5
# off-by-one behavior 

# for value in range(6):
#     print(value)

# To make a list of numbers
# list(range(6)) we add range in list() method as argument
# number_list = list(range(1, 7 + 1))
# print(number_list)

# => we can tell python range() function to skip number as a givin range
# we can add it at 3rd argument
# even_number = list(range(0, 100, 2))
# print(even_number)

# squares = []
# for value in range(1, 11):
#     squares.append(value ** 2)

# print(squares)

# help full methods
# numbers = list(range(1, 11000))
# print(sum(numbers))
# print(min(numbers))
# print(max(numbers))

# => Comperhensions List allow us to generate this same list 
# in just one line of code.
# squares = [value**2 for value in range(1, 11)]
# print(squares)