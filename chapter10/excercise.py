# NOTE:: Excercise 1
# filename = "learning_python.txt"
# with open(filename) as file_obj:
#     lines = file_obj.readlines()

# for line in lines:
#     print(line.strip())

# with open(filename) as file_obj:
#     for line in file_obj:
#         line.replace("Python", "C#")
#         print(line.rstrip())

# NOTE:: Excercise 2

# msg = "Hello Dear, {} Welcome to our course."
# filename = "guest.txt"

# print("------------------------------------------")
# print("Enter (s) or (show) to display data.")
# print("Enter (e) or (entry) to add new data.")
# print("Enter (q) or (quit) to quit the program.")
# print("------------------------------------------")
# while True:
#     code = input("Please enter the code: ")
    
#     if code == "s" or code == "show":
#         with open(filename) as file_obj:
#             lines = file_obj.readlines()

#         for name in lines:
#             print(msg.format(name.title().strip()))

#     elif code == "e" or code == "entry":
#         users_name = input("Please Enter Your Name: ")
#         with open(filename, 'a') as file_obj:
#             file_obj.write(f"{users_name.lower()} \n")
        
#         print(f"{users_name.title()} add successfuly.")
#         print("Enter (s) or (show) to display data.")

#     elif code == "q" or code == "quit":
#         print("You are loged out!!!")
#         break
