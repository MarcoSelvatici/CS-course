from turtle import *

def draw_square(size):
    for i in range(4):
        forward(size) # Move forward.
        right(90)     # Rotate 90 degrees to the right. 

def move_to(x, y):
    penup()    # Do not draw lines.
    goto(x, y) # Move the turtle.
    pendown()  # Start again drawing lines.

def draw_cheessboard(rows, cols, square_size):
    for r in range(rows):
        for c in range(cols):
            move_to(r*square_size, c*square_size)
            draw_square(square_size)

color("green")
width(3)

draw_cheessboard(5, 5, 100)

input("press enter to terminate... ") # Wait for the user indication to stop the program?
