# 5. Contains Character

# Write code that checks whether the string 
# char_sequence contains the character x.

char_sequence = 'TXkgaG92ZXJjcmFmdCBpcyBmdWxsIG9mIGVlbHMu'

# use the in operator to check if x appears
print('x' in char_sequence) # True

# use str.find - if x in sequence, the index 
# will be returned
print(char_sequence.find('x') > 0)  # True