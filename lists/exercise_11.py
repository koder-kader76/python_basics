# 11. Checking items off the grocery list

# We have a grocery list. As we check off  
# items on that list, from the top of the 
# list to the bottom, we want to remove them 
# from the list.


# Write code that removes the items from 
# grocery_list, one by one, until it is 
# empty. If you print the elements you  
# remove, the expected behavior would look as 
# follows.

grocery_list = [
    'paprika', 
    'tofu',
    'garlic', 
    'quinoa', 
    'carrots', 
    'broccoli', 
    'hummus',
]

while grocery_list:
    item = grocery_list.pop(0)
    print(item)

print(grocery_list)