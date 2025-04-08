# 2. Last Element

# Write a function that returns the last 
# element of a list provided as anargument.  
# For example:

# Be sure to handle the case where the input list is empty.

def last(lst):
    if lst:
        return lst.pop()
    else:
        return None

print(last(['Earth', 'Moon', 'Mars']))  # Mars
print(last([])) # None

# LS:
def last(lst):
    if lst:
        return lst[-1]
    else:
        return None