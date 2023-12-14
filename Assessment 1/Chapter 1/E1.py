# the following will ask the user what's his/her name and age
name = input("Hello, user!\nWhat is your name? ").title()
age = int(input("What is your age? "))

# this will determine the length of the name
nameL = len(name)

# this is to calculate the age for next year
agenY = age + 1

# this will display the messages
print(f"It is good to meet you, {name}")
print(f"The length of your name is: {nameL}")
print(f"You will be {agenY} in a year.")
