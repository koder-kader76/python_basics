# 3. Triple Greeting

# Write a loop that prints the value of the greeting variable three times


# use a for loop with a range(3) constructor to loop 3 times and call print function to print greeting variable
greeting = "Aloha!"

for index in range(3):
    print(greeting)


# using a while loop and an initial index of 0 and loop until index reaches 3
# index = 0

while index < 3:
    print(greeting)
    index += 1

# using an infinite while loop with an if statement and using the break keyword to break if index reaches 3

index = 0

while True:
    if index == 3:
        break
    print(greeting)
    index += 1
    
# ls:
# [print(greeting) for _ in range(0,3)]