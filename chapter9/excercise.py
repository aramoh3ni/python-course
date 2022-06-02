# NOTE:: Excercise 1
# from resturant import Rasturant

# new_resturant = Rasturant("Kabul 5 Start Hotal", "VIP")
# new_resturant2 = Rasturant("Syrina", "Cloub")
# new_resturant3 = Rasturant("Inter cantinatal", "Family")

# print(new_resturant.name)
# describtion = new_resturant.describe_restaurant()
# print(describtion)
# new_resturant.open_restaurant()

# describtion = new_resturant2.describe_restaurant()
# print(describtion)
# new_resturant2.open_restaurant()

# describtion = new_resturant3.describe_restaurant()
# print(describtion)
# new_resturant3.open_restaurant()



# NOTE:: Excercise 2
# from resturant import Rasturant
# new_resturant = Rasturant("Syrina Hotal", "Family")
# data = new_resturant.describe_restaurant()
# print(f"Resturant Name: {data['name']}")
# print(f"Type of Cuisine: {data['cuisine_type']}")
# print(f"Total Served Today: {data['number_served']}")

# new_resturant.set_number_served(200)
# data = new_resturant.describe_restaurant()
# print(f"Total Served Today: {data['number_served']}")

# from user import Users

# new_user = Users("Alireza", "Mohseni", "ara@ehaam", "JAJACXDR3ERSAHLJMMZAW112QA", "08-12-1997")
# print(new_user.get_user_info())

# new_user.increment_login_attempts(10)
# print(new_user.login_attempt)

# new_user.reset_login_attempts()
# print(new_user.login_attempt)


# NOTE:: Excercise 3
# from resturant import Rasturant

# class IceCreamStand(Rasturant):
#     def __init__(self, name, cuisine_type, flavors):
#         super().__init__(name, cuisine_type)
#         self.flavors = flavors

#     def display_flavor(self):
#         print(f"The Flavors are: ")
#         for flavor in self.flavors:
#             print(f"- {flavor}")
    

# new_ice_cream = IceCreamStand("HRT HOTAL", "Family", ['chocolate', 'banana'])

# new_ice_cream.display_flavor()

# from user import Users

# class Privileges:
#     def __init__(self, privileges):
#         self.privileges = privileges

#     def show_privileges(self):
#             print("Privileges")
#             for privilege in self.privileges:
#                 print(f"- {privilege}")
# class Admin(Users):
#     def __init__(self, first, last, username, password, dob, privileges):
#         super().__init__(first, last, username, password, dob)
#         self.privileges = Privileges(privileges)

# user_admin = Admin("Alireza", "Mohseni", "aramoh3ni", "JAMCIE2OSXZZEWA", "1997", [
#     'add_post',
#     'delete_post',
#     'add_user',
#     'delete_user',
#     'set_user_privilege'
# ])

# user_admin.privileges.show_privileges()

# class Car: 
#     def __init__(self, name, model, year):
#         self.name = name
#         self.model = model
#         self.year = year

#     def set_car(self, name, model, year):
#         self.name = name
#         self.model = model
#         self.year = year

#     def get_car(self):
#         car_info = f"{self.name} {self.model} {self.year}"
#         return car_info.title()

# class Battery:
#     def __init__(self, battery_size = 75):
#         self.battery_size = battery_size

#     def describe_battery(self):
#         print(f"This car has a {self.battery_size}-kWH battery.")

#     def get_range(self):
#         if self.battery_size == 75:
#             range = 260
#         elif self.battery_size == 100:
#             range = 315
        
#         print(f"This car can got about {range} miles on a full charge")

#     def upgrade_battery(self):
#         if self.battery_size < 100:
#             self.battery_size = 100
#         else:
#             print("Battery is Fully Charged.")
        
    
# class ElectricCar(Car):
#     """Represent aspects of a car, specific to electric vehicles"""

#     def __init__(self, name, model, year, price):
#         super().__init__(name, model, year)
#         self.battery = Battery() # Define Attribute for child class and creating object of a class (Battery)
#         self.price = price # Define Attribue for Child class

#     def fill_gas_tank(self):
#         print("This car doesn't need a gas tank")

# my_tesla = ElectricCar("Tesla", "GTR2600", 2022, price=90000)

# print(my_tesla.get_car())
# my_tesla.battery.describe_battery()
# my_tesla.fill_gas_tank()
# my_tesla.battery.get_range()

# my_tesla.battery.upgrade_battery()
# my_tesla.battery.get_range()

# from resturant import Rasturant
# my_hotal = Rasturant("seyna hotal", "Family")
# my_hotal.number_served = 2001
# print(my_hotal.describe_restaurant())

# NOTE:: Excercise 4
# from user import Users

# admin = Users("alireza", "mohseni", "aramoh3ni", "JALKJASDFJI343", 1997)
# print(admin.get_user_info())

# from admin import Admin

# privelage = ['add_post', 'delete_post', 'control_users']
# new_admin = Admin("alireza", "mohseni", "aramoh3ni", "123", 1997, privelage)
# new_admin.privelage.show_privileges()

# NOTE:: Excercise 5

# from random import randint, choice
# class Die: 
#     def __init__(self, sides = 6):
#         self.sides = sides

#     def roll_die(self):
#         return randint(1, self.sides)

# die = Die(6)
# for _ in range(0, 8):
#     print(die.roll_die())

# lottery_item = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "a", "b", "c", "d", "e"]

# print("Follwing Charcters will win a prize.")
# for _ in range(0, 4):
#     print(str(choice(lottery_item)).title())

# my_ticket = choice(lottery_item)

# for i in range(0, len(lottery_item)):
#     print(choice(lottery_item))
#     if lottery_item[i] == my_ticket:
#         print(f"It took { i+1 } iterations to get the ticket {lottery_item[i]}")
#         break


