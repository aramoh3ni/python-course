# Alireza Mohseni 
# May/19/2022
# Python Crash Course

players = ['ronaldo', 'nymar.jr', 'messi', 'florence', 'eli']

# NOTE:: Chapter 4 - working with part of a list
# Slicing list

# Slicing allow us to show/return a range of elements
# print(players[0:2]) # ['ronaldo', 'nymar.jr']

# it ignore the last element because it is start with index 0
# print(players[1:4]) # ['nymar.jr', 'messi', 'florence']

# If we omit the first index in a slice, python automatically starts
# Your slice at the beginning of the list
# print(players[:4]) # ['ronaldo', 'nymar.jr', 'messi', 'florence'

# If we Omit the end index in a slice, python automatically eng till
# to the end of list
# print(players[2:]) # ['messi', 'florence', 'eli']

# Putting (-) on the first index of a slice starts from end
# print(players[-2:])

# Putting (-) on the last index of a slice starts form beginning of the list
# print(players[0:3])

# Putting third index in alice it allow us to ignore current index you added
# print(players[1:3:2]) # ['nymar.jr']

# Looping Through a slice
# print("Here are the first three players on my team: ")
# for player in players[:3]:
#     print(player.title())

# Copying a List
# [:] tells python start at the beginning tell to the end
# first_list = ['pizza', 'falafel', 'carrot cake']
# second_list = first_list[:]

# print(f"My favorite foods are: {first_list}")
# print(f"My best friend favorite foods are: {second_list}")

