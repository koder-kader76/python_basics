# Checking Data Types

# Referring to the official Python documentation, how would you identify the data type of the following values?

# class type(object)
# With one argument, return the type of an object. The return value is a type object and generally the same object as returned by object.__class__.

print(type(23.5))   # <class 'float'>
print(type('Call me Ishmael.')) # <class 'str'>
print(type(False)) # <class 'bool'>
print(type(0))  # <class 'int'>
print(type(None)) # <class 'NoneType'>