# Loops allow to repeat the same operations many times.
# For example, imagine you have to print the numbers from 0 to 9.
# You could write
# print(0)
# print(1)
# print(2)
# and so on...

# But as you can see those instructions are all similar, so you can use a loop.
for i in range(10):
    print(i)

# Another example: sum the first 50 numbers.
sum = 0
for i in range(50):
    sum = sum + i
print(sum)

# For loops can also be used to go through values in lists.
alphabet = ["a", "b", "c", "d", "e"]
for letter in alphabet:
    print(letter)


# 1-Exercise: write a function that, given a number N, returns the value of N! (N factorial).
#             Remember that N! is defined as 1*2*3*4*...*N

# 2-Exercise: write a function that, given a list of integers, returns a list with all numbers doubled.

# 3-Exercise: write a function that, given a base and an exponent, returns the base to the power of the exponent.
#             For example, 2 to the power of three is 8. You are NOT allowed to use the ** operator.
