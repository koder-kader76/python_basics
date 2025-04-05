# TypeError

# 9. The following code raises a TypeError:

tweet = 'Woohoo! :-)'

if len(tweet) > 140:
    print('Tweet is too long!')

length_of_tweet = len(tweet + 5)

# What does a TypeError indicate? Try running the above code, then use the resulting error message to determine exactly what is wrong. (You don't have to fix this code.)

# source: https://docs.python.org/3/library/exceptions.html

# when you run this code, you get this error - length_of_tweet = len(tweet + 5)
# TypeError - usually raised when 2 different object types are found in an expression - in this case, string is concatenated with an integerw