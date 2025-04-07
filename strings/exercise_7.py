# 7. Is Empty or Blank?

# Write an is_empty_or_blank function to 
# determine whether a string is either empty 
# or consists entirely of spaces. For example:

# use the not operator twice
# once in the if statement using str.isspace()
# and then the return statement
def is_empty_or_blank(text):
    if not text.isspace():
        return not text
    
    return True


print(is_empty_or_blank('mars'))  # False
print(is_empty_or_blank('  '))    # True
print(is_empty_or_blank(''))      # True

# LS:
def is_empty_or_blank(s):
    return not s.strip(' ')