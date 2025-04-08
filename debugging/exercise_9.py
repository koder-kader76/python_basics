# 9. Find Maximum

# Your colleague has implemented a custom 
# function to find the maximum value in a 
# list. However, the function sometimes works 
# correctly, but other times it produces 
# incorrect results. Can you help your 
# colleague fix the bug?

def find_maximum(numbers):
    if not numbers:
        return None
    # bug in this code
    # max_number = 0

    # fix this code by assigning the 
    # first element to max_number
    max_number = numbers[0]

    for number in numbers:
        # print(f"number is: {number}")
        # print(f"max number is: {max_number}")
        if number > max_number:
            max_number = number
    return max_number

print(find_maximum([45, 3, 10, 98, 22]))  
# Expected 98       # 98
print(find_maximum([-1, 0, 5, 3]))         
# Expected 5        # 5
print(find_maximum([-10, -3, -20, -2]))   
# Expected -2       # 5

# the following code works for positive
# integers but in the last print call
# output is as follows:
# number is: -10
# max number is: 0
# number is: -3
# max number is: 0
# number is: -20
# max number is: 0
# number is: -2
# max number is: 0
# 0

print(find_maximum([10, -3, 20, -2])) 


# LS Solution 2:

def find_maximum(numbers):
    if not numbers:
        return None

    max_number = float('-inf')

    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number