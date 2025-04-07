# What's my value? (Part 2)

# What will the following code do and why? 
# Don't run it until you have tried to answer.

x = 10

def my_function():
    x = x + 5
    print(x)

my_function()

# UnboundLocalError: cannot access local 
# variable 'x' where it is not associated 
# with a value
# when variables are assigned within a  
# function, Python will assume the variables 
# local variables, so it will raise an error
# when x is not defined
# in order to make this function work, you 
# add a global keyword for the assignment 
# to work