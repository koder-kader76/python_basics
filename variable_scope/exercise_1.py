# 1 What's my value? (Part 1)

# What will the following code do and why? 
# Don't run it until you have tried to answer.

if True:
    my_value = 20

print(my_value)

# output will be 20
# the my_value variable is inside an if block
# which evaluates to truthy since the value 
# given is True 
# once the if block executes, then my value 
# is assigned the numeric value 20

# What do you think will happen if we run the 
# following code instead:

if False:
    my_new_value = 42

print(my_new_value)

# Python will raise an error - my_new_value
# variable not found
# The if block evaluates to falsy thus the 
# code block within that if statement is never
# executed