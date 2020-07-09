# You can also add keys to dictionaries.

days_full_name = {
    "Mon": "Monday",
    "Tue": "Tuesday"
}

days_full_name["Wed"] = "Wednesday"
days_full_name["Thu"] = "Thursday"
days_full_name["Fri"] = "Friday"
days_full_name["Sat"] = "Saturday"
days_full_name["Sun"] = "Sunday"

print("<<1>>")
print(days_full_name)

print("\n<<2>>")
# It is also possibe the change values inside the dictionary.

days_full_name["Mon"] = "Worst day of the week!"

print(days_full_name)

print("\n<<3>>")
# Finally, it is possible to loop through the elements of a dictionary, similarly to what we can do for lists.
for key, value in days_full_name.items():
    print(f"{key}  --->  {value}")

print("\n<<4>>")
# Alternatively, it is possible to only iterate on the keys.
for key in days_full_name:
    print(key)


#1-Exercise: take your grades from the previous exercises and write a function that calculates their average.

#2-Exercise: write a function that prints the name of all of the subjects (hint: they are the keys of the dictionary!).

