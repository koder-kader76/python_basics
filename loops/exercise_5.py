# 5. Looping over List Elements

# Using the code below as a starting point, write a while loop that prints the elements of lst at each index and terminates after printing the last element of the list.

lst = [1, 3, 7, 15]
index = 0

# use len(lst) to terminate loop
while index < len(lst):
    print(lst[index])
    index += 1

# 1
# 3
# 7
# 15

# using an infinite loop with the break keyword to terminate loop
index = 0

while True:
    if index == len(lst):
        break
    print(lst[index])
    index += 1

# 1
# 3
# 7
# 15
    
# What would the code output if lst is empty? Why is that?

lst2 = []
counter = 0

while counter < len(lst2):
    print(lst2[counter])
    counter += 1

# no output