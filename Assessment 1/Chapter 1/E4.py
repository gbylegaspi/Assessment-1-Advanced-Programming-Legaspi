# Python program to find the largest of three numbers using user input and if-else statements

# Prompt the user to input the first, second and third number and convert it to a float for more flexibility (allows decimals)
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
c = float(input("Enter the third number: "))

# Using if-else statements to find the largest number among the three
if a >= b and a >= c:
    d = a
elif b >= c:
    d = b
else:
    d = c

# Finally, print the largest number
print("The largest number is:", d)
