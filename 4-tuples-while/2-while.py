# While loops are conceptually similar to a for loop: they allow to repeat instructions multiple times.
# In particular, a while loop executes its content while a condition is true.

print("<<1>>")
a = 10
while a > 0:
    print(a)
    a = a - 1


print("\n<<2>>")
def is_valid_input(inp):
    return inp == "a" or inp == "b"

inp = ""
while not is_valid_input(inp):
    inp = input("type a or b: ")
