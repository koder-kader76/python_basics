# 5. What's my value? (Part 5)

# What will the following code do and why? 
# Don't run it until you have tried to answer.

a = 1

def my_function():
    print(a)
    a = 2

my_function()

# What will the following code do and why?
# output: UnboundLocalError: cannot access 
# local variable 'a' where it is not 
# associated with a value

# the variable a is assigned after the print 
# call which raises an error - any assignment 
# has to be done before the print call 
# instead of after which also ignores the 
# global variable a since there already is a 
# variable assigned by the same name inside 
# the function