# 5. Filter

# Count the number of elements in scores that 
# are 100 or above.

scores = [96, 47, 113, 89, 100, 102]

count = 0

for number in scores:
    if number >= 100:
        count += 1

print(count)