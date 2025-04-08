# 5. Confucius Says

# You want to have a small script delivering 
# motivational quotes, but with the following 
# code you run into a very common error 
# message: TypeError: can only concatenate 
# str (not "NoneType") to str. What is the 
# problem and how can you fix it?

def get_quote(person):
    # add a return keyword
    if person == 'Yoda':
        return 'Do. Or do not. There is no try.'
    if person == 'Confucius':
        return 'I hear and I forget. I see and I remember. I do and I understand.'
    if person == 'Einstein':
        return 'Do not worry about your difficulties in Mathematics. I can assure you mine are still greater.'


# TypeError: can only concatenate str (not "NoneType") to str
# print('"' + get_quote('Confucius') + '"')


print('Confucius says:')
print(f'"{get_quote('Confucius')}"')
# "I hear and I forget. I see and I remember. I do and I understand."



# debugging - check output from get_quote
# print(get_quote('Confucius'))

# output from the get_quote() function  
# returns None which is the default value 
# when a function does not return anything

# once the return keyword is added, 
print(get_quote('Confucius'))
# I hear and I forget. I see and I remember. I do and I understand.