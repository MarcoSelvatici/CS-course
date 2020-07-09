from turtle import *

def draw_spiral(sides):
    side_length = 10
    for i in range(sides):
        forward(i * side_length) # Move forward.
        right(90)                # Rotate 90 degrees to the right. 

color("green")
width(3)

draw_spiral(40)

input("press enter to terminate... ") # Wait for the user indication to stop the program?
