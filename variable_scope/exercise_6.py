# 6. What's my value? (Part 6)

# What will the following code do and why?   
# Don't run it until you have tried to answer.

a = 1

def my_function():
    a = 2

my_function()
print(a)

# invoking my_function doesn't do anything as 
# there is no return value - the a = 2 
# assigned means that Python will look at it 
# as a local variable
# output will print 1 - when print(a) is 
# invoked, python will evaluate the value 
# from the global variable a in the outer 
# scope