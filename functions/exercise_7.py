# 7. Transformation

# Use Python's string methods on the string 
# 'Captain Ruby' to create a string with the 
# value 'Captain Python'.

# use str.replace(old, new)
def replace_text(text, old, new):
    new_text = text.replace(old, new)
    return new_text

message = "Captain Ruby"
text1 = "Ruby"
text2 = "Python"
print(replace_text(message, text1, text2))