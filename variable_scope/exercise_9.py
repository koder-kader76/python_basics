# 9. What's my value? (Part 9)

# What will the following code do and why? 
# Don't run it until you have tried to answer.

a = 7

def my_function(b):
    b += 10

my_function(a)
print(a)

# output: 7
# when my_function is invoked, the value of a
# is passed in as an argument and the value 
# is changed to a += 10 but that has no 
# effect on the global variable a as the 
# global keyword is not passed in the 
# function.