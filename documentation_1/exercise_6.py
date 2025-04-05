# Finding Index

# Python lists come with a variety of built-in methods that allow for common list manipulations. One such operation is determining the index of an item in the list.

# Given a list:


# How would you determine the index of the fruit "cherry" in this list?

#  list.index(x[, start[, end]])
    # Return zero-based index in the list of the first item whose value is equal to x. Raises a ValueError if there is no such item.

    # The optional arguments start and end are interpreted as in the slice notation and are used to limit the search to a particular subsequence of the list. The returned index is computed relative to the beginning of the full sequence rather than the start argument.

fruits = ["apple", "banana", "cherry", "peach", "watermelon"]

print(fruits.index("cherry"))   # 2