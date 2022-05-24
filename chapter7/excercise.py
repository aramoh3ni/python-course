# NOTE:: Excercise 1

# Rental Car
# favorite_car = input("Tell me about your rental car: ")
# print(f"Let me see if i can find you a {favorite_car}")

# Resturatnt Seating
# message = "Wellcome to GOG resturant."
# seating_max = 8

# reserve_date = input("When you want to came: [2022/10/10]")
# total_customer = int(input("Enter your maximam guests: "))
# if total_customer > seating_max:
#     message = "Sorry! 🙄 your guests out of rand."
#     message += "\nOnly 8 person can join in one seat"
#     print(message)
# else:
#     print(f"Table is ready on {reserve_date}")

# Multiples of Ten:
# user_value = int(input("Your your number"))
# user_value = user_value % 10
# if user_value == 0:
#     print("Correct Your value can muliples of ten")
# else:
#     print("Can\'t muliples with then")


# NOTE:: Excercise 2
# Food Ordering
# requested_foods = []
# avilibal_foods = {
#     "001": "chess pizza",
#     "002": "qabli",
#     "003": "bolani",
#     "004": "chopan kabab"
# }   

# message = "Welecome to GOG Resturan, Afghanistan"
# message += "\nPlease Select each of then by code then enter [O] to submit your order"
# message += "Chess Pizza [001], Qabli [002], Bolani [003], Chopan Kabab [004]"


# def showOrders(foods):
#     for food in foods:
#         print(f"Dear Customer you have select: {food}.")

#     print("Thank you for visiting GOG Resturant.")

# print(message)
# while True:
#     food = str(input("Enter the code here: ")).lower()
#     if food == "o":
#         print("Your Order Submited 🤭")
#         showOrders(requested_foods)
#         break
#     else:
#         for key, value in avilibal_foods.items():
#             if food == key:
#                 requested_foods.append(value)
#             else: continue

# MOVIE TAKED BOOKING
# message = "Wellcome to Kabul Cinama Hotal"
# message += "\n\n----ROLLS------"
# message += "\n1: Child Under 3 is free"
# message += "\n1: between 3 - 12 for each 10$"
# message += "\n3: Between 12 - 18 for each 25$"
# message += "\n\n ---- group of 3 persons 10% discount 🤭"
# message += "\n4: Adult over age of 18 for each 27$"

# movies = {
#     "1": {
#         "title": "Help me to go!",
#         "genru": "lovestory",
#     },
#     "2": {
#         "title": "The Simpsons",
#         "genru": "cartoon",
#     }
# }

# money = []

# print(message)
# print("\n ======== TONIGH MOVIES =========")
# for key, movie in movies.items():
#     print(f"Movie Title: {movie['title']} = code: {key}")

# while True:
#     code = str(input("Enter Move Code: "))
#     group = int(input("total Group members: "))
#     group_start = 1
#     while group_start <= group:
#         name = str(input("Enter each person name: "))
#         age = int(input("Enter each person ages: "))

#         if age >= 3 and age <= 12:
#             money.append(10)
#         elif age >= 12 and age <= 18:
#             money.append(25)
#         elif age > 18:
#             money.append(27)
#         else:
#             money.append(0)
        
#         group_start += 1
    
    
#     total_price = 0
#     dics = 0
#     for item in money:
#         total_price += item
#         amount += item
    
#     if group > 3: 
#         print("You are More then 3, you got 10% discount")    
#         dics = total_price * 0.10
#     else:
#         dics = 0

#     print(f"Amout: {total_price}$")
#     print(f"Discount: {dics}%")
#     print(f"Net pay: {total_price - dics}$")
#     break

# Moving items from one list to another list
# unconfirmed_users = ['karim', 'hamid', 'jawid']
# confirmed_users = []

# while unconfirmed_users:
#     current_user = unconfirmed_users.pop()

#     print(f"Verfying : {current_user} ...")
#     confirmed_users.append(current_user)
#     print(f"{current_user} is active now \n")

# Removing All Instances of specific value from a list
# pets = ["dog", 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
# print(pets)
# while 'cat' in pets:
#     pets.remove("cat")

# print(pets)

# Filling a Dictionary with user input
# responses = {}
# Set a flag to indicate that polling is active.
# polling_active = True
# while polling_active:
# Prompt for the person's name and response.
    # name = input("\nWhat is your name? ")
    # response = input("Which mountain would you like to climb someday? ")
# Store the response in the dictionary.
    # responses[name] = response
# Find out if anyone else is going to take the poll.
    # repeat = input("Would you like to let another person respond? (yes/ no) ")
    # if repeat == 'no':
    #     polling_active = False
# Polling is complete. Show the results.
#     print("\n--- Poll Results ---")
# for name, response in responses.items():
#     print(f"{name} would like to climb {response}.")  

# Sandwich orders example
# sandwich_orders = ['abc', 'ors', 'ppafg']
# finished_sandwiches = []

# while True:
#     print("Choose Sandwich and enter the name")
#     for sand in sandwich_orders:
#         print(f"- {sand}")

#     name = input("Enter Sandwich Name: ")
#     print("In progress...")
#     finished_sandwiches.append(name)
#     print("Done")
#     break

# print(finished_sandwiches)
