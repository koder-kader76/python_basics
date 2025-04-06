# 2. Yes? No? Part 1

# The code provided below randomly initializes random_number to either 0 or 1 each time it is executed.

# Write an if statement that prints Yes! if random_number is 1, and No. if random_number is 0.

import random

random_number = random.randint(0, 1)

# print random_number to verify output
print(random_number)

# using an if/else statement with an equality expression
if random_number == 1:
    print('Yes!')
else:
    print('No')

# using if statement which  truthy or falsy
if random_number:
    print('Yes!')
else:
    print('No')

# using a ternary expression with truthy/falsy
print('Yes!') if random_number else print('No')

# using ternary expression using a print call
print('Yes!' if random_number else 'No')