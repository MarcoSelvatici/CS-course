# Tuples are data types that allow to put together some values.
# They are somewhat similar to lists, but they are immutable.
# This means that you cannot change a tuple once you created it!

my_tuple = (1, "hello", True)
print(my_tuple)

# You can access particular elements in the tuple.
print(my_tuple[1])

# You cannot change the values in a tuple.
# my_tuple[0] = 2 # Throws error!

# Tuples have len(), but do not have methods like .append().
print(len(my_tuple))

# Tuples are usually used with different data types, like a number with a string and a bool.
# Lists are usually contain a single data type (for example, a list of strings).

# Tuples have a very useful feature: they can be nicely unpacked!

tup0, tup1, tup2 = (1, "hello", True)
print(tup0) # 1
print(tup1) # "hello"
print(tup2) # True
print(my_tuple)

# In the code above, Python understands that you want to assign the value of the first
# element of the tuple to tup0, the second element to tup1 and the third element to tup2.

# Tuples are often useful to return multiple values from a function.

def my_fun():
    return 1, "hello"

int_val, string_val = my_fun()
print(int_val)    # 1
print(string_val) # "hello"
