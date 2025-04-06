# Take Two

# Write a for loop that iterates over the integers from 1 to 100 and prints the result of multiplying each integer by 2.

# 1. using a for loop with a range constructor
for number in range(1, 101):
    number *= 2
    print(number)

# 2. using a comprehension to generate a list of integers doubled
numbers = [number * 2 for number in range(1, 101)]
print(numbers)

# ls:
for num in range(1, 101):
    print(num * 2)