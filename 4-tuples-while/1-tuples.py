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
