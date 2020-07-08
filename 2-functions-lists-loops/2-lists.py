# Lists are ordered collections of elements.
# The elements contained can be of any type:
# - integers
# - strings
# - other lists
# - ...

# Lists are useful because the data can often be represented as ordered collections of elements.

# An example of list in Python.

list1 = [1, 2, 3]          # List of integers.
list2 = ["hello", "world"] # List of strings.
list3 = [ [1, 2], [3, 4] ] # List of lists.
list4 = []                 # Empty list (no elements).

print("\n<<1>>")
# It is possible to print a list like any other variable.
print(list1)

print("\n<<2>>")
# Or you can access specific elements of a list.
a = list2[0]
b = list2[1]
# c = list1[2] # Gives an error!
print(a)
print(b)

print("\n<<3>>")
# Lists indexes are zero-based. In other words, the first element is at index 0.
# index:         |    0     |    1    |     There is no element at index 2!
# list2 element: | "hello"  | "world" | 

# You can append elements at the end of a list:
print(list1)
list1.append(4)
print(list1)

print("\n<<4>>")
# You can also see how many elements are in the list.
print(len(list1))
print(len(list4))


# 1- Exercise: write a function that, given a list of 3 elements in input, returns the maximum element.

# 2- Exercise: write a function that appends the number 42 to a list.

# 3- Exercise: write a function that prints the length of a list.
