# Alireza Mohseni
# 06/June/2022

# Python Crash Course Chapter 15

# Data visualization involves exploring data through visual representations.

# closely associated with data analysis. with we code to explore the patterns and connections in a data set. 

# What is data set?
# A data set can be made up of a small list of numbers that fits in one line of code or it can be many giga bytes of data. 

# --------------------------------------------------------------
# Matplotlib
# is a low level graph plotting library in python that serves as a visualization utility. 

# Created by Johan D. Hunter

# Open sourse

# written in python, few segements written in C, Object-C and JavaScript for platform compatibility. 

import matplotlib.pyplot as plt

squares = [2, 4, 9, 16, 25]

fig, ax = plt.subplots()
ax.plot(squares)

plt.show()