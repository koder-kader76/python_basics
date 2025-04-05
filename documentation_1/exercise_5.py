# List Element Access

# Locate the documentation for the list built-in object in Python Documentation.

# How can we access the second element ('and') in the list ['fish', 'and', 'chips']?

# s.index(x[, i[, j]])
    # index of the first occurrence of x in s (at or after index i and before index j)

my_list = ['fish', 'and', 'chips']
print(my_list.index('and'))     # 1

print(my_list[1])     # and