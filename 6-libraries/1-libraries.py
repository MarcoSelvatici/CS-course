# Libraries are collections of functions (and classes) previosly written.
# Code in libraries can be easily reused via import statements.
# For example:

import turtle

# allows us to use all the turtle library capabilities.

# Another few examples:

import random # To have access to random numbers and so on...
import os     # To perform Operating System operations.
import math   # For example, to use the sqrt function.

# Let's use some functions from these libraries.

print('<<1>>')
print(math.sqrt(9))           # Take the square root of a number.
print(random.randint(0, 100)) # Pick a random number between 0 and 100.
print(os.uname())             # Get some info about the current user.
print(os.listdir())           # List the files in the current directory.

# Alternatively, it is possible to import specific functions from the library.
# In this case, you don't have to put the library name before the dot in order
# to use them.

print('\n<<2>>')

from math import sqrt
print(sqrt(16))

from random import * # * means import all functions.
                     # This is usually not a good idea as you may have many functions
                     # you don't need, and their names may conflict with the functions
                     # you define.
print(randint(0, 100))
print(choice([1, 2, 3]))
