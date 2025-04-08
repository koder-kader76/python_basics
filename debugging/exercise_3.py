# 3. Multiply By Five

# When the user inputs 10, we expect the 
# program to print The result is 50!, but 
# that's not the output we see. Why not?

def multiply_by_five(n):
    return n * 5

print("Hello! Which number would you like to multiply by 5?")
# bug in original code
# number = input()

# fix the code by changing its type with int()
number = int(input())
print(repr(number))

print(f"The result is {multiply_by_five(number)}!")

# Hello! Which number would you like to multiply by 5?
# 10
# The result is 1010101010!

# when user provides an input, the value
# assigned to number is a string not an 
# integer - which can be seen when you print
# repr(number)

# After fixing it
# Hello! Which number would you like to multiply by 5?
# 10
# 10
# The result is 50!