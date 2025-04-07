# 10. Locale Part 2

# Similar to the previous exercise, write a 
# function that extracts the region code from 
# a locale. For example:


# as with the previous example, use the split
# method and use indexing with slicing method
# to extract the contry code

def extract_region(locale):
    language_code = locale.split('_')
    country_code = language_code[1][:2]
    
    return country_code

print(extract_region('en_US.UTF-8'))    # US
print(extract_region('en_GB.UTF-8'))    # GB
print(extract_region('ko_KR.UTF-16'))   # KR