# You can access libraries in various ways.
# - Some libraries are standard and are installed together with the language
#   interpreter. For example, os and math.
# - Some libraries can be downloaded from the internet. For example turle.
#   To do so, you usually use package managers (such as pip3).
# - You can also create your own libraries! Let's try this out.

# A library, in its simplest form, is just a file containing a bunch of functions.
# For example, have a look at `my_library.py`. It contains a function that we will
# now use.

import my_library

my_library.test_function()
print(my_library.test_function_2("hello world"))

# Or similarly.

from my_library import test_function

test_function()
# test_function_2("hi") # Gives error because it was not imported!

# Note that the file my_library.py must be in the same folder as the file
# that uses it as a library.
