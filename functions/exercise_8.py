# Internationalization 1

# Use Python's control structures to create a 
# function that takes an ISO 639-1 language 
# code and returns a greeting in that 
# language. You can take the examples below  
# or add whatever languages you like.

# the first solution that came to mind was 
# a match/case statement, but after reviewing 
# the code, if you had 200 or 300 languages to
# add, this code wouldn't be feasible

def greet(language):
    match language:
        case 'en':
            return "Hi!"
        case 'fr':
            return "Salut!"
        case 'pt':
            return "Ola!"
        case 'de':
            return "Hallo!"
        case 'sv':
            return "Hej!"
        case 'af':
            return "Haai!"
        case 'gd':
            return "Halò!"
        case 'gl':
            return "Olá!"
        case 'gr':
            return 'Ja!'
        case 'ko':
            return 'Annyeong!'
        case 'ja':
            return "Kon'nichiwa!"
        case _:
            return "Hi!"

print(greet('en'))         # Hi!
print(greet('fr'))         # Salut!
print(greet('pt'))         # Olá!
print(greet('de'))         # Hallo!
print(greet('sv'))         # Hej!
print(greet('af'))         # Haai!
print(greet('gd'))         # Halò!
print(greet('gr'))         # Ja!!
print(greet('gl'))         # Olá!!
print(greet('ko'))         # Annyeong!!
print(greet('ja'))         # Kon'nichiwa!


# the practical solution would be to use 
# languages dictionary with the language 
#  as keys and greeting as values and extract
# the values with the greet function

languages = {
    'en': {
        'GB': "Hello!",
        'US': "Hey!",
        'AU': "Howdy!",
    },
    'fr': {
        'FR': "Salut!",
        'CA': "Salut!",
        'MA': "Salut",
    },
    'pt': "Ola!",
    'de': "Hallo!",
    'sv': "Hej!",
    'af': "Haai!",
}

def greet(language):
    return languages[language]

print(greet('en'))         # Hi!
print(greet('fr'))         # Salut!
print(greet('pt'))         # Olá!
print(greet('de'))         # Hallo!
print(greet('sv'))         # Hej!
print(greet('af'))         # Haai!