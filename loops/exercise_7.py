# 7. Continue

# Take a moment to read the Python documentation on the continue statement.

# Write a for loop that iterates over the elements of the list cities and prints the length of each string. If the element is None, use the continue statement to skip forward to the next iteration without printing anything.

# Python documentation "continue"
# continue may only occur syntactically nested in a for or while loop, but not nested in a function or class definition within that loop. It continues with the next cycle of the nearest enclosing loop.


cities = [
    'Istanbul', 
    'Los Angeles', 
    'Tokyo', 
    None,
    'Vienna', 
    None, 
    'London', 
    'Beijing', 
    None,
]

# using a for loop, print the length of each string
for city in cities:
    if city == None:
        continue
    print(len(city))

# using a while loop to perform the same iteration

counter = 0

while counter < len(cities):
    if cities[counter] == None:
        # if counter is not present before the continue keyword, the loop becomes an inifinite loop
        counter += 1
        continue 
    print(len(cities[counter]))
    counter += 1


# using a while loop but without the continue keyword

count = 0

while count < len(cities):
    city = cities[count]
    
    if city != None:
        print(len(city))
    count += 1

# 8
# 11
# 5
# 6
# 6
# 7

# LS:
cities = ['Istanbul', 'Los Angeles', 'Tokyo',
          None,'Vienna', None, 'London','Beijing', None]

for city in cities:
    if city is None:
        continue

    print(len(city))