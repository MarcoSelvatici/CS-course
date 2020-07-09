# Python (and all the other programming languages) allows the developer to interact
# with files.

# Let's see how we can read the content of a file.
# Note that in this folder there is a file called 'example.txt'.

print("<<1>>")
file = open("example.txt", "r") # Open the file example.txt in read mode ("r").
file_content = file.read()      # Read all the content.
print(file_content)
file.close()                    # Close the file. ALWAYS do that once you are done!

print("\n<<2>>")
# It is also possible to read the file line by line, with the functions readline.
file = open("example.txt", "r")
first_line = file.readline()     # Read one line.
second_line = file.readline()    # Read another line.
print(first_line)
print(second_line)
file.close()

print("\n<<3>>")
# It is also possible to read all the lines into a list of strings.
# Note that each string terminates with the \n characters. This two characters
# indicate a new line.
file = open("example.txt", "r")
lines_list = file.readlines()    # Read all the lines into a list of strings.
print(lines_list)
file.close()
