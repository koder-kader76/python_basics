# Right Justifying Strings

# 3. Use the Python documentation for the str class to determine which method can be used to right justify a str object.

# str.rjust(width[, fillchar])
    # Return the string right justified in a string of length width. Padding is done using the specified fillchar (default is an ASCII space). The original string is returned if width is less than or equal to len(s).

title = 'aloha, world!'
print(title.rjust(8))
# '-------Aloha, World!'

print('123'.rjust(10))