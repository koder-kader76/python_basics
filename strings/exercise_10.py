# 10. Count Substrings

# Write a function that counts the number of 
# occurrences of a substring in a string.

# use the str.count() method
def count_substrings(text, substring):
    return text.count(substring)

print(count_substrings("lemon lemon lemon", "lemon")) # 3
print(count_substrings("laLAlaLA", "la")) # 2
print(count_substrings("launch", "uno")) # 0