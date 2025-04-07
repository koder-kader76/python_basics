# What's my value? (Part 4)

# What will the following code do and why?
# Don't run it until you have tried to answer.

a = 1

def my_function():
    print(a)

my_function()

# output: 1
# Python will look inside the my_function for
# the variable a and then it will look in the 
# outerscope for the variable
# since there is no re-assignment, it will be
# able to access a and print the following 
# output