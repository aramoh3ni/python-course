# Alireza Mohseni
# 3/June/2022

# Python Crash Course

# NOTE:: Files and Exceptions

# Reading from  a file.
# An incredible amount of data is available in text files
# Text files can contain 
# - Weather data
# - Traffic data
# - Socioeconomic data
# - Literary Works
# - and more...


# Reading an Entire File
# with open("pi_digits.txt") as file_object:
#     contents = file_object.read()
# print(contents)

# (with) statement -> closes the file once access to it is no longer needed

# We can open and close file by calling open() and close()
# NOTE:: if a bug in our program precents the close() method from being exceuted, the file may never close.
# Python will close it automatically when the (with) block finished execution.

# Remove right each line spaces
# print(contents.rstrip())
# Remove left each line spaces
# print(contents.lstrip())
# Remove both each line spaces
# print(contents.strip())

# --------------------------------------------------------------
# File Path

# with open("file/txt/<file_name>.<extention>") as <file_name>:
# NOTE:: Windows use backslash (\) inside forwardslash (/) for path but we can still using forwardslash (/)

# but if we want to use backslash (\) we can use it like this
# with open("file\\txt\\<file_name>.<extention>") as <file_name>:
# with (\\) dual backslash beacuse with one backslash (\) we ignore the collens for string 

# --------------------------------------------------------------
# reading Line by Line

# file_name = "pi_digits.txt"
# with open(file_name) as file_obj:
#     for line in file_obj:
#         print(line.strip())

# when file run in terminal it have line space
# becuse at the end of each line use an invisblenewline character
# solution
# strip() or rstrip()

# -------------------------------------------------------------
# Making a list of lines from a file
# with open(file_name) as file_obj:
#     lines = file_obj.readlines()
# readlines() method takes each line from the file and stores it in a list[].
# for line in lines:
#     print(line.rstrip())

# NOTE:: When Python reads from a text file, it interperets all text in the file as string. If you read in a number and want to work with that value in a numerical context, you'll have to convert it to an integer using the int() function or convet it to a fload using the float() function.

# -------------------------------------------------------------
# Large Files: One Million Digits
# filename = "pi_digits.txt"
# with open(filename) as file_million_obj:
#     lines = file_million_obj.readlines()

# pi_string = ''
# for line in lines:
#     pi_string += line.strip()

# birthday = input("Enter your birthday, in the form mmddyy: ")
# if birthday in pi_string:
#     print("Your Birthday appears in the first million digits of pi!")
# else:
#     print("Your Birthday does not appears in the first million digits of pi.")

