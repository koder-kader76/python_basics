# What's my value? (Part 7)

# What will the following code do and why? 
# Don't run it until you have tried to answer.

a = 1

def my_function():
    global a
    a = 2

my_function()
print(a)

# output: 2
# when my_function is called, it changes the
# global variable a and re-assigns it to the 
# value of 2 - so during the print call, the 
# value of a will 2