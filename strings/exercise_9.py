# 9. Check Prefix

# Write a function that checks whether a 
# string starts with a specific prefix.


# use str.find() method which returns the
# index of where the substring starts from
# use the comparison operator to check if 
# it returns 0 - True if it does, False if not
def starts_with(text, substring):
    return text.find(substring) == 0

print(starts_with("launch", "la"))   # True
print(starts_with("school", "sah"))  # False
print(starts_with("school", "sch"))  # True
print(starts_with("school", "ch"))   # False

# LS:
def starts_with(string, prefix):
    return string.startswith(prefix)