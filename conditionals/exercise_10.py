# 10. Are we moving?

# Determine what the following code snippet 
# prints. First solve it in your head or on 
# paper, then run it in your Python 
# environment to check the result.

speed = 0
acceleration = 24
braking_force = 19
is_moving = (
        braking_force < acceleration 
    and (speed > 0 or acceleration > 0)
)

print(is_moving)

# is_moving variable is assigned to 2 
# logical operators, 'and' and 'or'
# the second expression:
# speed > 0 or acceleration > 0
# speed > 0 -> falsy
# acceleration > 0 -> truthy
# the second expression will return truthy

# the first expression:
# braking_force < acceleration 
# 19            < 24  -> truthy

# so on either side of the 'and' operator
# the expresssions evaluate to truthy
# so is_moving will return True

# Bonus question: Do we need the parentheses in the boolean expression or could we have written the following?:

#  is_moving = 
#               braking_force < acceleration
#           and speed > 0 or acceleration > 0

# do we need parentheses? Yes
# if there is no parentheses, then the first
# operator which will be evaluated will be
# the and operator according to the logical
# operator precedence
# this may result in an inaccurate expression