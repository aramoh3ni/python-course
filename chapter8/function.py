#  Alireza Mohseni
# 25/May/2022
# Python Crash Course

# Function
# Block of code to perfome a particular task
# we should call function to execute the codes inside block
# Mutlipale call == multipale exceute
# Define Function
# def say_hello():
#     return f"Hello dear"
# msg = say_hello()
# print(msg)

# Passing Information to Function
# def say_hello(name):
#     return f"Hello dear, {name}"

# msg = say_hello("Alireza")
# print(msg)

# Argument and Parameters
# def get_full_name(fname, lname): # Parameters
#     return f"{fname} {lname}"

# full_name = get_full_name("Alireza", "Mohseni") # Arguments
# print(full_name)

# Passing Arguments
# Positional Arguments
# def describ_pet(animal_type, pet_name):
#     """Display information about a pet"""
#     print(f"\nI have a {animal_type}")
#     print(f"My {animal_type}'s name is {pet_name.title()}")

# describ_pet("hamster", "harry")

# Multiple Function Calls
# def describ_pet(animal_type, pet_name):
#     """Display information about a pet"""
#     print(f"\nI have a {animal_type}")
#     print(f"My {animal_type}'s name is {pet_name.title()}")

# describ_pet("hamster", "harry") # 1
# describ_pet("dog", "Willie") # 2

# NOTE:: Order Matters in Positional Arguments
# we get unexpected results if we mix up the order of the arguments

# def describ_pet(animal_type, pet_name):
#     """Display information about a pet"""
#     print(f"\nI have a {animal_type}")
#     print(f"My {animal_type}'s name is {pet_name.title()}")

# describ_pet("harry", "hamster")

# Keywor Arguments
# keyword argument is name-value - directly associate the name and the value within the argument
# no confusion in passing arrguments
# def say_hello(name, lname):
#     """return string, greeting some one"""
#     return f"your name is: {name} \nyour last name is {lname}"

# print(say_hello(lname="Mohseni", name="Alireza"))
# no confusion
# no order matters

# Default Value
# If we didn't pass argument we can use default value inside fucntion infront of inistialzion value of each parameter
# def you_name(name = "Joe"):
#     return f"Hello Dear, {name}"

# print(you_name("Alireza"))

# Equvalent function calls
# NOTE:: it doesn't realy matter which calling style we use.
# As logn our function calls produce the output you want, just the style you find easeiset to understant
# print(say_hello(name="Alireza", lname="Mohseni"))
# print(say_hello(lname="Mohseni", name="Alireza"))
# print(say_hello("Alireza", "Mohseni"))



# Return Value
# the return statement takes a value from inside a function and sends it back to the line that caled the function.

# def get_formatted_name(fname = 'johan', lname = "doe"):
#     """return full name as formatted title()"""
#     full_name = "{} {}".format(fname, lname)
#     return full_name.title()

# your_name = get_formatted_name("Alireza", "Mohseni")
# print(your_name)


# Making and Argument Optional
# we can pass argument optional inside calling a function
# def full_formatted_name(fName, lName, mName=''):
#     """return full name with middle name optional"""
#     full_name = "{} {} {}".format(fName, mName, lName)
#     return full_name.title()

# your_name = full_formatted_name("ali", "mohseni", "reza")
# print(your_name)


# Return Dictionary
# def build_person(fName, lName, height, eyeColor, color, mName=None):
#     person = {
#         "first_name": fName,
#         "last_name": lName,
#         "eye_color": eyeColor,
#         "color": eyeColor
#     }

#     if mName:
#         person["middle_name"] = mName

#     return person

# person = build_person("alireza", "mohseni", 184, "black", "Kandomi", "Ehaam")
# print(person)

# Using a function with a while loop
# def get_formatted_name(fName, lName):
#     """Return a full name, neatly formatted"""
#     full_name = "{} {}".format(fName, lName)
#     return full_name.title()

# while True:
#     print("\nEnter you information please. or enter [q] to quit")
#     f_name = input("Enter your name: ")
#     l_name = input("Enter your lname: ")

#     if f_name == 'q' or l_name == "q":
#         break

#     formatted_name = get_formatted_name(f_name, l_name)
#     print(f"\nHello, {formatted_name}. Wellcome back")
    

# Passing a List
# we will often find it useful to pass a list to a function
# def greet_users(users):
#     """Print a Simple greeting to each users"""
#     for user in users:
#         msg = "Hello Dear, {}"
#         print(msg.format(user).title())

# users = ["alireza", "karim", "hamid", "jawid"]
# greet_users(users)

# Modifying a list in function
# current_tasks = ['Fix the navbar responsive', 'Create Mobile Navbar', "Update New version", "Debug the ancomes"]

# def task(tasks):
#     complete_tasks = []
#     while tasks:
#         progress_task = tasks.pop()
#         complete_tasks.append(progress_task)
#         print(f"{progress_task} is in process")

#     print("\nTHE FOLLOWING MODELS HAVE BEEN DONE\n")
#     for c_task in complete_tasks:
#         print(f"{c_task} is done.")
# task(current_tasks)

# Passing an Arbitrary Number of Arguments
# Sometimes you won't know a head of time how many arguments a function needs to accept.

# NOTE:: THE Syntax works no matter how many arguments the function receives.

# def make_pizza(*toppings):
#     print("\nMaking a pizza with the follwing toppings.")
#     for topping in toppings:
#         print(f"- {topping}")

# make_pizza('extra cheese')
# make_pizza('mashrooms', 'green peppers', 'extra cheese')
# The asterisk in the parameter name *topping tells Python to make an empty tuple called toppings and pack whatever values it recevice into this tuple.

# Using Arbitrary Keyword Arguments
# def build_profile(first, last, **user_info):
#     user_info['first_name'] = first
#     user_info['last_name'] = last
#     return user_info


# user_profile = build_profile("Alireza", "Mohseni", location="Afghanistan", education="Bachler")

# print(user_profile)


