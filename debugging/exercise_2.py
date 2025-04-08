# 2. Weather Forecast

# Our predict_weather function should output 
# a message indicating whether a sunny or 
# cloudy day lies ahead. However, the output 
# is the same every time the function is 
# invoked. Why? Fix the code so that it 
# behaves as expected.

import random

def predict_weather():
    # bug in code
    # sunshine = random.choice(['True', 'False'])

    sunshine = random.choice([True, False])

    if sunshine:
        print("Today's weather will be sunny!")
    else:
        print("Today's weather will be cloudy!")

predict_weather()
# Today's weather will be sunny!
# The output is always "Today's weather will  
# be sunny!" as the if condition always 
# evaluates to truthy as a 'True' or 'False' 
# string is always assigned to sunshine

# Fix: change the 'True' and 'False' values 
# to actual boolean values: True & False