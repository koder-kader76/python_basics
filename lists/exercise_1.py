# First Element

# Write a function that returns the first 
# element of a list provided as an argument. 
# For example:

# Be sure to handle the case where the input 
# list is empty.

def first(elements):
    first_element = (elements[0] if elements 
                     else "empty")
    
    return first_element

print(first(['Earth', 'Moon', 'Mars']))  # Earth
print(first([])) # empty