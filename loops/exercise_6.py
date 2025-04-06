# 6. Greet Your Friends

# Your friends just showed up! Given the following list of names, use a for loop to greet each friend individually.

friends = ['Sarah', 'John', 'Hannah', 'Dave']

# using a for loop
for name in friends:
    print(f"Hello, {name}!")

# using a for loop with a match case statement
for name in friends:
    match name:
        case 'Sarah':
            print(f"Hello, {name}!")
        case 'John':
            print(f"Bonjour, {name}!")
        case 'Hannah':
            print(f"Salud, {name}!")
        case 'Dave':
            print(f"Aloha, {name}!")
        case _:
            print(f"Hi There!")