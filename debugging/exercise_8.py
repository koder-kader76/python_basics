# 8. Matrix

# We wanted to create a matrix 3x3 so we 
# could use it to build a Tic-Tac-Toe game. 
# However, we encountered an issue, as 
# whenever we change a value in one nested 
# list, all nested lists are affected. Can 
# you fix the code?

sub_list = ["-", "-", "-"]
matrix = []

for _ in range(3):
    # amend this line with list(sub_list)
    # matrix.append(sub_list)
    matrix.append(list(sub_list))

matrix[0][0] = "X"

print(matrix) # [['X', '-', '-'], ['X', '-', '-'], ['X', '-', '-']]


# print(matrix[0] is matrix[1]) # True
# print(matrix[0] is matrix[2]) # True

# in this code, matrix[0] is matrix[1]
# returns True
# matrix[0] is matrix[2] also returns True
# basically the matrix.append(sub_list) is
# referencing the same list object during the
# for loop

# matrix.append(sub_list) -
# matrix.append(list(sub_list))
# print(matrix[0] is matrix[1])   # False
# print(matrix[0] is matrix[2])   # False


# LS:
sub_list = ["-", "-", "-"]
matrix = []

for _ in range(3):
    matrix.append(sub_list.copy())

matrix[0][0] = "X"
print(matrix) # [['X', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]