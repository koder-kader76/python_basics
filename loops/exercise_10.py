# 10. Loop on Command

# Modify the following code so the loop continues iterating until the user inputs 'yes'.

while True:
    print('Should I stop looping?')
    # modify the input to prompt user
    # for yes or no answer
    answer = input("Please enter: (yes/no) ")
    
    # add an if statement with a break keyword
    # to stop iteration is answer is yes
    if answer == "yes":
        break

# Should I stop looping?
# Please enter: (yes/no) no
# Should I stop looping?
# Please enter: (yes/no) no 
# Should I stop looping?
# Please enter: (yes/no) yes

# LS:
while True:
    print('Should I stop looping?')
    answer = input()
    if answer == 'yes':
        break
    print('Incorrect answer. Please answer "yes".')