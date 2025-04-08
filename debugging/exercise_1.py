# 1. Reading Error Messages

# You come across the following code. What 
# errors does it raise for the given examples 
# and what exactly do the error messages mean?

def find_first_nonzero_among(numbers):
    for n in numbers:
        if n != 0:
            return n

find_first_nonzero_among(0, 0, 1, 0, 2, 0)
find_first_nonzero_among(1)

# 1st function call - wrong number of 
# arguments - expecting 1 argument
# 2nd function call - argument provided is 
# not an iterable