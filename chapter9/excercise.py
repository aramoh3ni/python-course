# NOTE:: Excercise 1
from resturant import Rasturant

new_resturant = Rasturant("Kabul 5 Start Hotal", "VIP")
new_resturant2 = Rasturant("Syrina", "Cloub")
new_resturant3 = Rasturant("Inter cantinatal", "Family")

print(new_resturant.name)
describtion = new_resturant.describe_restaurant()
print(describtion)
new_resturant.open_restaurant()

describtion = new_resturant2.describe_restaurant()
print(describtion)
new_resturant2.open_restaurant()

describtion = new_resturant3.describe_restaurant()
print(describtion)
new_resturant3.open_restaurant()
