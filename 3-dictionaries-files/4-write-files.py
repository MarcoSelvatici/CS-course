# You can also write files from Python!

file = open("write-example1.txt", "w")  # Open a file in write mode ("w"). If the file does not exist it gets created.
file.write("This is the first line!\n") # Write the line to the file. Note the final \n to insert a new line.
file.write("This is the second line!\n")
file.close()

# You can do this operation in a loop.

file = open("write-example2.txt", "w")
for i in range(10):
    file.write(f"This is line {i}\n")
file.close()

# You can also give a list of lines to write on the file.

lines = [
    "These are\n",
    "my beautiful\n"
    "lines.\n",
    "Yay!"
]
file = open("write-example3.txt", "w")
file.writelines(lines)
file.close()
