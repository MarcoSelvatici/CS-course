# Let's do some data analysis!
# In the folder data you can find a database recording the most common names in the US since 1880.

# For each year of birth YYYY after 1879, we created a comma-delimited file called yobYYYY.txt.
# Each record in the individual annual files has the format "name,sex,number" where name is 2 to 15
# characters, sex is M (male) or F (female) and "number" is the number of occurrences of the name.
# Each file is sorted first on sex and then on number of occurrences in descending order. When there is
# a tie on the number of occurrences, names are listed in alphabetical order. This sorting makes it easy to
# determine a name's rank. The first record for each sex has rank 1, the second record for each sex has
# rank 2, and so forth.
# To safeguard privacy, we restrict our list of names to those with at least 5 occurrences.

# We are going to do some exercises in reading and handling these large amount of data.

# For example, let's read and analyse the data from 1880.

names_1880_file = open("data/yob1880.txt", "r")
names = names_1880_file.readlines()
for i in range(10): # print the first 10 lines.
    print(names[i])
names_1880_file.close()

#1- Exercise: write a function that given a string like "Anna,F,2604" splits it into a list with
#             a the name (a string), the sex (a string) and the number of occurrences (an int).
# I solved this exercise for you already ;)

def split_line(line):
    tmp = line.split(",")
    tmp[2] = int(tmp[2]) # Convert the number of occurrences to an int.
    return tmp

print( split_line("Anna,F,2604") )

#2- Exercise: write a function that counts how many female names are there in a file.

def count_females(filename):
    # TODO: implement this!
    pass

print(count_females("data/yob1880.txt"))

#3- Exercise: write a function that checks whether your name is in a file.

#4- Exercise: write a function that tells you in what years your name was there!
#             To do so, you will have to open all the files (in a loop).

#5- Exercise: write a function that finds each year's most common female name, and puts it in a dictionary.
#             The dictionary key is the the year, the value is the name.
#             For example: {1880: "Mary", 1881: "Mary", ..., 2018: "Emma"}

#6- Exercise: write a function that sums all of the name occurrences in a file.

#7- Exercise: write a function that calculates what year had the highest number of total occurrences.

#8- Exercise: write a function that finds out what year had the most distinct names (which is equivalent
#             to the number of lines in each file).
