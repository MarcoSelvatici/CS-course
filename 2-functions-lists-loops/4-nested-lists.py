# As we briefly mentioned in part 2-lists, lists can contain any data type, including other lists.
# A list inside another list is usually called nested.
# For example:

# Simple list of integers.
simple_list = [
    1, 2, 3, 4, 5, 6, 7, 8, 9
]

# A list containing 3 lists.
nested_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("\n<<1>>")
# Let's try to print the elements of each list.
for element in simple_list:
    print(element)

for element in nested_list:
    print(element)

# As you can see, the elements in the simple_list are just numbers, as expected.
# In the nested_list, each element is a list.

print("\n<<2>>")
# Each element in the nested list is a list, therefore we can do a for loop on it
# to print its elements. To do so, we need two nested for loops.

for row in nested_list:
    for element in row:
        print(element)

print("\n<<3>>")
# To access a specific element in the simple list, we can use the square brackets, like this:
print(simple_list[3])
# To access a specific element in the nested list we need to do the same thing twice:
second_row = nested_list[1] # This accesses the second row of the list of lists (the first one is at index 0).
first_element_of_second_row = second_row[0]
print(first_element_of_second_row)

# In short you can write:
print(nested_list[1][0])
