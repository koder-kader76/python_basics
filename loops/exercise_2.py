# 2. Countdown

# The following code prints the numbers from 1 to 10. Modify it so that it instead prints the numbers from 10 to 1 in descending order, followed by 'Launch!'

for i in range(10, 0, -1):
    print(i)

print('Launch!')

# first we print 'Launch' which is the print function call after the loop iteration is done

# second we change the range object to range(10, 0, -1), where the range objects will start in descending order

# output
# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1
# Launch!