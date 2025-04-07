# 6. Is Empty?

# Write a function that checks whether a 
# string is empty or not. For example:

# to check if a string is empty, use the 
# len(str) function - an empty string will 
# evaluate to 0 which evaluates to falsy

# if len(text) is truthy, it returns False
# True if not
def is_empty(text):
    if len(text):
        return False
    
    return True

print(is_empty('mars'))  # False
print(is_empty('  '))    # False
print(is_empty(''))      # True

# LS:
def is_empty(s):
    return not s 