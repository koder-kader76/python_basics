# 8. Capitalize Words

# Write code that capitalizes the words in 
# the string 'launch school tech & talk', so 
# that you get the string 'Launch School 
# Tech & Talk'.

message = "launch school tech & talk"

# use the str.title() method
titlized_message = message.title()

print(titlized_message)
# Launch School Tech & Talk

# LS:
def capitalize_words(string):
    return string.title()

string = 'launch school tech & talk'
result = capitalize_words(string)
print(result)  # Launch School Tech & Talk