# 3. Ignoring Case

# Using the following code, compare the value 
# of name with the string 'RoGeR' while 
# ignoring the case of both strings. Print 
# true if the values are the same; print 
# false if they aren't. Next, perform a 
# case-insensitive comparison between the 
# value of name and the string 'DAVE'.

name = "Roger"

# to compare the 2 strings, 
# use str.casefold() method
print(name.casefold() == 'RoGeR'.casefold())
# True

print(name.casefold() == 'DAVE'.casefold())
# False