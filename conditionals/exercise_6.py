# 6. Check the Weather, Part 2

# Take your code from the previous Check the 
# Weather exercise and rewrite it as a 
# match-case statement. 
# Feel free to add more cases 
# besides 'sunny' and 'rainy'.

weather = 'hot hot hot!'

match weather:
    case 'sunny':
        print("It's a beautiful day!")
    case 'rainy':
        print("Grab your umbrella.")
    case 'snowy':
        print("Make sure you have your mittens on.")
    case 'cloudy':
        print("Any chance of meatballs?")
    case _:
        print("Let's stay inside.")