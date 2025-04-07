# 3. What's my value? (Part 3)

# What will the following code do and why? 
# Don't run it until you have tried to answer.

def my_function():
    a = 1

    if True:
        print(a)

my_function()

# output: 1
# a is local variable within the function
# the if block will run as it evaluates to 
# truth which will cause the print function
# to be invoked
