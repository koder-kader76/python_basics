# 4. Pets

# Magdalena has just adopted a new pet! She 
# wants to add her new dog, Bowser, to the 
# pets dictionary. After doing so, she 
# realizes that her dogs Sparky and Fido have 
# been mistakenly removed. Help Magdalena fix 
# her code so that all three of her dogs' 
# names will be associated with the key 'dog' 
# in the pets dictionary.

pets = { 'cat': 'pepe', 'dog': ['sparky', 'fido'], 'fish': 'oscar' }

print(pets['dog'])
# re-assigns the value of dog to 'bowser'
# the list is no longer being reference
# pets['dog'] = 'bowser'

# since the value is a list, use the append 
# method to add 'bowser' into the list
pets['dog'].append('bowser')

print(pets)  
# {'cat': 'pepe', 'dog': ['sparky', 'fido', 'bowser'], 'fish': 'oscar'}

print(pets['dog'])
# ['sparky', 'fido', 'bowser']
