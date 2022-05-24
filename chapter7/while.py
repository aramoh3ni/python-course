# Alireza Mohseni
# 24/May/2022
# Python Crash Course

# Intoduction while loops
# for loop: takes a collection of items then executes block of code once for each item in the collection

# while loop: runs as long as or while, a certain condition is true.

# current_number = 0
# while current_number <= 10:
#     print(current_number)
#     current_number += 1

# Let user to choose when to quit

# stop = ""
# while stop != 'q':
#     messsage = "Enter what ever you want i will repeat it for you 😁😉"
#     messsage += "\n or enter [q] to quit"
#     print(messsage)
    
#     user_input = input("Enter you text: ")
#     if user_input == 'q':
#         stop = user_input
#     else:
#         print(user_input)
#         stop = ''

# Using Break to eit a loop
# break the while if statment false

# while True:
#     city = input("Enter [q] to quit")

#     if city == "q":
#         break
#     else:
#         print(city)

# Using Continue in a loop
# continus the loop while if statment in false
# ignor 

# current_numer = 0
# while current_numer < 10:
#     current_numer += 1
#     if current_numer % 2 == 0:
#         continue

#     print(current_numer)

# # Avoiding Infinite Loops
# x = 1
# while x <= 5:
#     print(x)
#     x += 1


