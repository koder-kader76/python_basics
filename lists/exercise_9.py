# Travel

# The destinations list contains a list of 
# travel destinations.

# Write a function that, without using the 
# built-in in operator, checks whether a 
# specific destination is included within 
# destinations. For example: When checking 
# whether 'Barcelona' is contained in 
# destinations, the expected output is True, 
# whereas the expected output for 'Nashville' 
# is False.

destinations = [
    'Prague', 
    'London', 
    'Sydney', 
    'Belfast',
    'Rome', 
    'Aruba', 
    'Paris', 
    'Bora Bora', 
    'Barcelona', 
    'Rio de Janeiro', 
    'Marrakesh',
    'New York City',
]

def contains(city, cities):
    return True if city in cities else False


print(contains('Barcelona', destinations))
print(contains('Nashville', destinations))
print(contains('Prague', destinations))
print(contains('New York City', destinations))
print(contains('Amsterdam', destinations))

# LS:
def contains(element, lst):
    return element in lst