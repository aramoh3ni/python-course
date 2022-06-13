# Alireza Mohseni
# 11/June/2022

# Python Crash Course Chapter 15
# Data Visualization


# involves exploring data through visual representations.
# Closely Associated with data analysis.

# Data set -> can me made up of small list of numbers that fits in one line of code, or it can be manage giga bytes of data.

# People use Python for (data-intensive work in genetics, climate research, political, economic analysis).

# ----------------------------------------------------------------------------------
# Installing Matplotlib

# $ python -m pip install --user matplotlib # windows
# $ python3 -m install --user matplotlib    # Max and Linux

# NOTE:: if command not working in macOS do not use (--user)

# ----------------------------------------------------------------------------------
# Plotting a Simple Line Graph
# import matplotlib.pyplot as plt

# squares = [1, 4, 9, 16, 25]
# fig, ax = plt.subplots()

# ax.plot(squares)
# plt.show()

# ----------------------------------------------------------------------------------
# Channging the Lablel type and Line Thickness

# ax.plot(squares, linewidth=3)
# ax.set_title("Square Numbers", fontsize=24)
# ax.set_xlabel("Value", fontsize=16)
# ax.set_ylabel("Square of value", fontsize=24)
# ax.tick_params(axis='both', labelsize=14)

# plt.show()

# ----------------------------------------------------------
# Correcting the Plot
# input_values = [1, 2, 3, 4, 5]
# ax.plot(input_values, squares, linewidth=3)

# plt.show()


# ---------------------------------------------------------------------------------
# Using Built-in Styles
# Matplotlib has a number of  predefined styles available.
# 1- Background colors
# 2- Gridlines
# 3- Line widths
# 4- Fonts
# 5- Font sizes

# import matplotlib.pyplot as plt
# print(plt.style.available)

# ['seaborn-dark', 'seaborn-darkgrid', 'seaborn-ticks', 'fivethirtyeight']

# squares = [1, 4, 9, 16, 25]

# plt.style.use('seaborn') # gray with chart

# fig, ax = plt.subplots()

# ax.plot(squares, linewidth=3)
# ax.set_title("Square Numbers", fontsize=24)
# ax.set_xlabel("Value", fontsize=16)
# ax.set_ylabel("Square of value", fontsize=24)
# ax.tick_params(axis='both', labelsize=14)

# plt.show()

# ----------------------------------------------------------------------------------
# Ploting and Styling indicidual Points with scattter()

# it is useful to plot and style individual points based on certain characteristics.
# we may plot small values in one color and larger values in a different color. 

# scatter() method -> to plot a single point,
# import matplotlib.pyplot as plt

# plt.style.use('seaborn')
# fig, ax = plt.subplots()

# ax.scatter(2, 4) # for a single point

# Styling points
# ax.set_title("Square Number", fontsize=14)
# ax.set_xlabel("value", fontsize=14)
# ax.set_ylabel("Square of value", fontsize=14)

# Set size of tick labels.
# ax.tick_params(axis='both', which='major', labelsize=14)

# plt.show()
# ------------------------------------------------------------------------------------
# Ploting a Series of Points with scatter() method

# to plot a series of points. we can pass scatter() separate lists of x- and y- values, like this:

# import matplotlib.pyplot as plt

# initialized values
# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 4, 9, 16, 25]

# plt.style.use('seaborn')
# fig, ax = plt.subplots()

# ax.scatter(x_values, y_values, s=100)

# plt.show()

# ----------------------------------------------------------------------------------
# Calculating Data Automatically
# import matplotlib.pylab as plt

# x_values = range(1, 1001)
# y_values = [x**2 for x in x_values]

# plt.style.use('seaborn')
# fig, ax = plt.subplots()
# ax.scatter(x_values, y_values, s=10)

# ax.axis([0, 1100, 0, 1100000])

# plt.show()

# ----------------------------------------------------------------------------------
# Defining Custom Colors

# to change the color of points pass, (c='color_name') as parameter
# import matplotlib.pylab as plt

# x_values = range(1, 1001)
# y_values = [x**2 for x in x_values]

# plt.style.use('seaborn')
# fig, ax = plt.subplots()
# ax.scatter(x_values, y_values, s=10, c='yellow') # using color name
# ax.scatter(x_values, y_values, s=10, c=(0, 0.8, 0)) #using RGB color set

# ax.axis([0, 1100, 0, 1100000])

# plt.show()

# ----------------------------------------------------------------------------------
# Using a Colormap

# A colormap is a series of color in a gradient that moves from a starting to an ending color. 
# we use colormaps in visualizations to emphasize a pattern in the data. 

# pyplot module includes a set of built-in colormaps. 

# import matplotlib.pyplot as plt

# x_values = range(1, 1001)
# y_values = [x**2 for x in x_values]

# plt.style.use("seaborn")
# fig, ax = plt.subplots()

# ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

# plt.show()

# -----------------------------------------------------
# Saving Our Plots Automatically

# plt.savefig() functin -> to save as file in our local computer

# import matplotlib.pyplot as plt

# x_values = range(1, 1001)
# y_values = [x**2 for x in x_values]

# plt.style.use('seaborn')
# fig, ax = plt.subplots()

# ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

# ax.set_title("Square Number", fontsize=14)
# ax.set_xlabel("value", fontsize=14)
# ax.set_ylabel("Square of value", fontsize=14)

# plt.show()

# plt.savefig('./squares_plot.png', bbox_inches='tight')

# ------------------------------------------------------------------------------
# Random Walks
# we'll use Python to generate data for a random walk. 
# A Random Walks is a path that has no clear direction but is determined by a serise of random decisions. 

# Random Walks have partical applications in nature, physics, biology, chemistry, and economics. for example, a pollen grain floating on a drop of water moves across the surface of the water becuase it's constatly pushed around by water moecules.

# -----------------------
#   Creating the RandomWalk() Class
# files inside randomewalk.py file      

import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:

    # Make Random Walk
    rw = RandomWalk(50000)
    rw.fill_walk()

    # Plot the points in the walk. 
    plt.style.use('classic')
    # Altering the sise to fill the screen
    fig, ax = plt.subplots(figsize=(15,9), dpi=64)
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=rw.y_values, cmap=plt.cm.Blues, s=10)
    # ax.plot(rw.x_values, rw.y_values, linewidth=3) # return line points

    # Emphasize the first and last points
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
    

    # Remove the axes
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another Walk? (y/n): ")
    if keep_running == 'n':
        break