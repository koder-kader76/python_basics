# Out Of Bounds

# 7. What happens if we take the list ['fish', 'and', 'chips'] and try to access the element at index position 10? First try to determine what will happen by consulting the documentation, then verify your understanding in the Python REPL.

# exception IndexError
    # Raised when a sequence subscript is out of range. (Slice indices are silently truncated to fall in the allowed range; if an index is not an integer, TypeError is raised.)

my_list = ['fish', 'and', 'chips']
print(my_list[10])
# IndexError: list index out of range