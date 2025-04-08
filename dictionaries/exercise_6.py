# 6. Checking Key Existence

# Check whether the keys 'name' and 'grade' 
# exist in the following dictionary:

student = {
    'id': 123,
    'grade': 'B',
}

keys = student.keys()
print('name' in keys)   # False
print('grade' in keys)  # True

# LS:
print('name' in student)      # False
print('grade' in student)     # True