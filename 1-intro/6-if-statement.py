# Sometimes you want your program to behave differently depending on some conditions.
# This behaviour can be done by using if statements.
# An if statement is composed of three parts:
# 1- a condition that can be either True or False.
# 2- some instructions that have to be executed if the condition is True.
# 3- some instructions that have to be executed if the condition is False (optional).
# Let's see an example:

a = 5

if a > 10:                        # 1- Condition: a is bigger than 10.
    print("a is bigger than 10")  # 2- Instruction to execute if True.
else:
    print("a is smaller than 10") # 3- Instruction to execute if False. This part is not necessary.


# Exercise: write some code to test whether a number is odd or even.


# Extras:
# - try to nest if statements (one within the other).
# - try to have more complex conditions. For example: a > 3 and a < 10
# - elif

# Extra exercise:
# The user inserts a number between 0 and 50 and you tell them in what range the number is.
# For example, the user inserts 36, and the program says: "your number is between 30 and 40".
