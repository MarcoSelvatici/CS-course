# A function is a block of organized,reusable code that is used to perform a single task.
# Like any other block of code, a function is a series of instructions.
# Functions have 2 main advantages:
# - they split up big programs into smaller pieces. Smaller pieces are easier to implement,
#   debug and reason about.
# - they allow to avoid duplicated code (no need to rewrite the same stuff over and over).

# Functions are formed by:
# 1- a function name.
# 2- a list of arguments (parameters).
# 3- a function body (sometimes containing a return value).

# In Python, a function that doubles a number looks like this:

def multiply_by_two(x):
    return x * 2

# 1- function name: multiply_by_two
# 2- argument:      x
# 3- function body: return x * 2

# The function takes in input a number x and returns the double of the number.
# We can call the function like this.

test1 = multiply_by_two(4)
print(test1)
test2 = multiply_by_two(27)
print(test2)




# Another example:

def add(a, b):
    sum = a + b
    return sum

# 1- function name: add
# 2- arguments:     a, b
# 3 function body:  sum = a + b
#                   return sum

test3 = add(4, 8)
print(test3) 




# One last example:

def print_hello_world():
    print("hello world!")

# 1- function name: print_hello_world
# 2- arguments:     no arguments
# 3- function body: print("hello world")
# Note that this function does not return anything!

# Calling the function without saving its result in a variable.
# In fact, the function does not return a value at all!
print_hello_world()




# 1- Exercise: write a function that takes a number and adds 20 to it.

# 2- Exercise: write a function that takes two arguments and return the biggest one.

# 3- Exercise: write a function that takes a name and prints "hello <name>". The function should not return anything.
