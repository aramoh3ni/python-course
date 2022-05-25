#  Alireza Mohseni
# 25/May/2022
# Python Crash Course

# Function
# Block of code to perfome a particular task
# we should call function to execute the codes inside block
# Mutlipale call == multipale exceute
# Define Function
def say_hello():
    return f"Hello dear"
msg = say_hello()
print(msg)

# Passing Information to Function
def say_hello(name):
    return f"Hello dear, {name}"

msg = say_hello("Alireza")
print(msg)

# Argument and Parameters
def get_full_name(fname, lname): # Parameters
    return f"{fname} {lname}"

full_name = get_full_name("Alireza", "Mohseni") # Arguments
print(full_name)


