# 6. Three-way Comparison

# Write a function that compares the length 
# of two strings. It should return -1 if the 
# first string is shorter, 1 if the second 
# string is shorter, and 0 if they're of 
# equal length. For example:

# 1. solution - using if statement
def compare_by_length(text1, text2):
    if len(text1) < len(text2):
        return -1
    elif len(text1) > len(text2):
        return 1
    else:
        return 0
    
# 2. solution - using True/False logic
# found it on stack overflow
# True - False -> 1
# False - True -> 1
# False - False -> 0
def compare_by_length(text1, text2):
    return ((len(text1) > len(text2)) 
          - (len(text1) < len(text2)))


print(compare_by_length('patience', 'perseverance')) # -1
print(compare_by_length('strength', 'dignity'))      #  1
print(compare_by_length('humor', 'grace'))           #  0