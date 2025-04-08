# 7. Dictionary Access

# You are trying to access a value in a 
# dictionary, but the code is giving you an 
# error. Can you change line 3 so that it 
# prints "Unknown" instead of raising an 
# error?

info = {'name': 'Srdjan', 'age': 38}

# print(info['city'])
# KeyError: 'city'

# with dictionaries, we can use the dict.get()
# method and pass in an argument unknown
# is the key is not in the dictionary

print(info.get('city', 'Unknown'))
# Unknown