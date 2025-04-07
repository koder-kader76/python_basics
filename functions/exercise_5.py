# 5. Display Division

# Without running the following code, 
# determine what it will print:

def multiples_of_three():
    divisor = 1

    for dividend in range(3, 31, 3):
        print(f'{dividend} / {divisor} = 3')
        divisor += 1

multiples_of_three


# there will be no output
# during a function call, there has to be 
# parentheses on the calling function
# multiples_of_three does not have ()
# parentheses when it is supposedly being
# invoked

# from looking at the code, it is supposed to
# print the following values

# 3, 6, 9, 12, 15, 18, 21, 24, 27, 30
# 1  2  3   4   5   6   7   8   9  10