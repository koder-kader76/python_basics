# Locale Part 1

# Write a function that extracts the language 
# code from a locale. A locale is a 
# combination of a language code, a region, 
# and usually also a character set, e.g en_US.
# UTF-8.

# first thing when you see the argument
# it is in a string format and the code
# requires that print out the locale which 
# the first 2 characters of the string
# so using slicing method, we can extract 
# the first two characters with str[:2]
# and return the value

def extract_language(locale):
    language_code = locale[:2]
    
    return language_code


print(extract_language('en_US.UTF-8'))      # en
print(extract_language('en_GB.UTF-8'))      # en
print(extract_language('ko_KR.UTF-16'))     # ko

# LS:
def extract_language(locale):
    return locale.split('_')[0]

print(extract_language('en_US.UTF-8'))      # en
print(extract_language('en_GB.UTF-8'))      # en
print(extract_language('ko_KR.UTF-16'))     # ko