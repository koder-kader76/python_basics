# 11. Internationalization 2

# Building on your solutions from the 
# previous exercises, write a function 
# local_greet that takes a locale as input, 
# and returns a greeting. The locale lets us 
# greet people from different countries 
# appropriately, even when they share a 
# common language, for example:

# print(local_greet('en_US.UTF-8'))       # Hey!
# print(local_greet('en_GB.UTF-8'))       # Hello!
# print(local_greet('en_AU.UTF-8'))       # Howdy!

# Distinguish greetings for English speaking  
# countries like the US, UK, Canada, or 
# Australia in your implementation, and feel 
# free to fall back on the language-specific 
# greetings in all other cases, for example:

# print(local_greet('fr_FR.UTF-8'))       # Salut!
# print(local_greet('fr_CA.UTF-8'))       # Salut!
# print(local_greet('fr_MA.UTF-8'))       # Salut!

# When implementing local_greet, make sure 
# you re-use your extract_language, 
# extract_region, and greet functions from 
# the previous exercises.


# create the data structure for the languages
# in a dictionary and within that dicionary,
# contains nested dictionary with the custom
# greetings

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
    'pt': {
        'PT': "Ola!",
        'BR': "Ola!",
        'CV': "Ola!",
    },
    'de': "Hallo!",
    'sv': "Hej!",
    'af': "Haai!",
}

# retrieving the functions from previous 
# exercises 
# greet(language)
# extract_language(locale)
# extract_region(locale)

def greet(language):
    return languages[language]

def extract_language(locale):
    language_code = locale[:2]
    
    return language_code

def extract_region(locale):
    language_code = locale.split('_')
    country_code = language_code[1][:2]
    
    return country_code

# use 3 functions above to extract the values
# to return a greeting variable which
# extracts the greeting as per language and
# as per country

def local_greet(locale_code):
    language = extract_language(locale_code)
    region = extract_region(locale_code)
    
    greeting = greet(language)[region]
    
    return greeting


print(local_greet('en_US.UTF-8')) # Hey!
print(local_greet('en_GB.UTF-8')) # Hello!
print(local_greet('en_AU.UTF-8')) # Howdy!

print(local_greet('fr_FR.UTF-8')) # Salut!
print(local_greet('fr_CA.UTF-8')) # Salut!
print(local_greet('fr_MA.UTF-8')) # Salut!

# LS:
def greet(language_code):
    match language_code:
        case 'en':
            return 'Hi!'
        case 'fr':
            return 'Salut!'
        case 'pt':
            return 'Olá!'
        case 'de':
            return 'Hallo!'
        case 'sv':
            return 'Hej!'
        case 'af':
            return 'Haai!'

def extract_language(locale):
    return locale.split('_')[0]

def extract_region(locale):
    return locale.split('.')[0].split('_')[1]

def local_greet(locale):
    language = extract_language(locale)
    region = extract_region(locale)

    match (language, region):
        case ('en', 'US'):
            return 'Hey!'
        case ('en', 'GB'):
            return 'Hello!'
        case ('en', 'AU'):
            return 'Howdy!'
        case _:
            return greet(language)