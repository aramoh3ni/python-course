# Alireza Mohseni
# 2022-May-17
# Main.py file

# a method to greeting users
# return string
def sayHello(name):
    return "Hello Dear, {}".format(name)

# a method for zen of python
def zen():
    import this
    return this


message = sayHello("Alireza")
print(message)

print(zen())