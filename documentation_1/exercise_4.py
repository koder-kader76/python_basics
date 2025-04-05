# Reverse

# 4. Is there a method to reverse a string, for example turning 'hello' into 'olleh'?

# short answer: no

# strings are immutable objects 

# using str.reverse() will raise an error
# AttributeError: 'str' object has no attribute 'reverse'

# one way to reverse a string without a method would be to use the slicing method
print('hello'[::-1])    # 'olleh'

# 2nd way would be to use the reversed function with the list and join the result in the end
print(''.join(list(reversed('hello')))) # 'olleh'