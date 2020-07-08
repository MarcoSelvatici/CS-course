# For the homework we will have some fun!
# We are going to use turtle.
# turtle is a library to draw figures.
# What is a library? We will cover that later in the course, but essentially it is a collection of ready-to-use functions.

# Here you go a quick tutorial for turtle.
# The main idea is: imagine there is a turtle with a pen on its belly, and when it walks it draws a line.
# Depending how you move the turtle, you can draw cool stuff!
# In this and the next file I will show you some of the most useful turtle functions.
# A complete list of all the functions can be found here:
# https://docs.python.org/3.3/library/turtle.html?highlight=turtle#turtle-methods

from turtle import * # Import the library, now we can use all the turtle functions.

color('red') # Select the color for your turtle.
width(3)     # Decide how wide the pen is.
forward(100) # Move the turtle 100 steps forward.

input("press enter to terminate... ") # Wait for the user indication to stop the program?
