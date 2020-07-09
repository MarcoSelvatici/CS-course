# Dictionaries are data structures (like lists), that allow to map a key to a value.
# Keys are unique (no duplicates).
# Keys and values can be (almost) any type.

# For example:
# Key is a string.
# Value is a string.
months_full_names = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}

# Another example.
# Key is a string.
# Value is an int.
months_length = {
    "Jan": 31,
    "Feb": 28,
    "Mar": 31,
    "Apr": 30,
    "May": 31,
    "Jun": 30,
    "Jul": 31,
    "Aug": 31,
    "Sep": 30,
    "Oct": 31,
    "Nov": 30,
    "Dec": 31
}

# Another one.
# Key is an int.
# Value is a list of strings.
length_to_months = {
    28: ["Feb"],
    30: ["Apr", "Jun", "Sep", "Nov"],
    31: ["Jan", "Mar", "May", "Jul", "Aug", "Oct", "Dec"]
}

print("<<1>>")
# Dictionaries can be printed like any other variable.
print(months_full_names)
print() # Print an empty line.
print(months_length)
print() # Print an empty line.
print(length_to_months)


print("\n<<2>>")
# Similarly to lists, it is possible to access specific elements.
# Instead of using indices (like in lists), we use the keys.
full_january_name = months_full_names["Jan"]
number_of_days_in_january = months_length["Jan"]
print(f"{full_january_name} has {number_of_days_in_january} days")
months_with_31_days = length_to_months[31]
print(f"Months that have 31 days: {months_with_31_days}")



#1- Exercise: create a dictionary to represent your grades (pagella). You can invent the grades.
#             For example: math:8, italian:7, ....

#2- Exercise: change the value of italian to 9.

#3- Exercise: print the sum of the grades for math and italian.

