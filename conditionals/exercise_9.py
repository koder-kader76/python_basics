# Logical Conditions 3

# Without running the following code, 
# determine what will be printed.

sale = True
admission_price = 5.25 if not sale else 3.99

print(f"${admission_price}")

# output: $3.99

# first line: sale = True
# which means there's a sale going on 

# 2nd line: admission_price is being assigned 
# a ternary expression using the not operator

# with the 'not' operator, whatever is on the
# right side of operator will invert its value
# so when sale is truthy, not sale will falsy
# which will result in the else statement
# being executed which is 3.99