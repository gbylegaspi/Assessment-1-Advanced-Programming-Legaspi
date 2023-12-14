a = int(input("Enter the first integer: "))
b = int(input("Enter the second integer: "))

# Perform calculations and print results
print("Sum:", a + b)
print("Difference:", a - b)
print("Product:", a * b)

# Check for division by zero
if b != 0:
    print("Quotient:", a / b)
    print("Remainder:", a % b)
else:
    print("Cannot divide by zero, so quotient and remainder cannot be calculated.")