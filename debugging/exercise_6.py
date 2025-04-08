# 6. Populate List

# You want to add the numbers from 1 to 5 to 
# a list, but the code below is not producing 
# the expected result. How can you fix it?

# empty list - no issue
numbers = []

# for i in range(5):

# amend the range object in fo loop
for i in range(1, 6):
    # check what are the numbers being pass
    # in the iteration - 0, 1, 2, 3, 4
    print(i)
    numbers.append(i)

# print call - no issue
print(numbers)

# 1. check what numbers are being passed
# no issue with rest of code so the problem
# lies in the for loop
# the numbers being printed is - 0, 1, 2, 3, 4
# for loop is working as expected

# problem lies with range object
# range(start, stop) - range(5)- 0 1 2 3 4
# to print out numbers 1 - 5
# range(1, 6)

# print call outputs - [1, 2, 3, 4, 5]