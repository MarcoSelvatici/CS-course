# List comprehension allows to write more readable and coincise code for creating list
# with particular values in them.
# Though it is convenient, it is not always possible to use it (but when it is,
# you probably should use it).

# Simple list comprehension.
numbers = []
for i in range(10):
    numbers.append(i)

numbers1 = [i for i in range(10)]

print(numbers == numbers1)

# List comprehension with if.
even_numbers = []
for i in range(10):
    if i % 2 == 0:
        even_numbers.append(i)

even_numbers1 = [i for i in range(10) if i % 2 == 0]

print(even_numbers == even_numbers1)

# More details in the answer here:
# https://stackoverflow.com/questions/4260280/if-else-in-a-list-comprehension

# 1-Exercise: write code to put in a list the square of the first ten numbers.
#             do this both with a list comprehension and without, and compare the results.
#             Which way is cleaner?

# 2-Exercise: write a function that takes in input a number, and returns a list with its divisors.
#             For example, input is 8, the function returns [1, 2, 4, 8].
