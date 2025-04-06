# 9. Finding Nemo

# Loop over the elements of the fish_list list below, logging each one. Terminate the loop immediately after printing the string 'Nemo'.

fish_list = [
    'Dory',
    'Marlin',
    'Gill',
    'Nemo',
    'Bruce',
]

# use a for loop to iterate over the fish_list
for fish in fish_list:
    print(fish)
    # using fish is 'Nemo', raises a 
    # SyntaxWarning: "is" with 'str' literal. 
    # Did you mean "=="? 
    # if str(fish) is 'Nemo'
    # syntax warning comes up as both fish & 
    # 'Nemo' are referencing different objects
    if fish == 'Nemo':
        break

# use a for loop to iterate over the fish_list
# to use the is keyword, use index() method
# to retrieve index
# perform is comparison during the loop
# iteration

nemo = fish_list.index('Nemo')
print(nemo)

for fish in fish_list:
    print(fish)
    if fish is fish_list[nemo]:
        break

# Further Exploration
# Can you achieve the same result using a 
# while loop? What would the code look like?

nemo = fish_list.index('Nemo')
print(nemo)

counter = 0

while counter < len(fish_list):
    fish = fish_list[counter]
    print(fish)
    
    if fish is fish_list[nemo]:
        break
    
    counter += 1