#Exercise: look at the behaviour of the builtin enumerate function, and write an
#          equivalent my_enumerate function.

# Helper function to print a list.
def print_list(lst):
    print("[ ", end="")
    for el in lst:
        print(el, end=", ")
    print("]")

test_list = [i * 2 for i in range(10)]

print_list(enumerate(test_list))

def my_enumerate(lst):
    pass

