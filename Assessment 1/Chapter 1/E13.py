# Define a list of numbers
numbers = [2, 3, 4, 5]

# Initialize a variable to store the product of the numbers
product = 1

# Iterate over each number in the list
for num in numbers:
    # Multiply the current number with the accumulated product
    product *= num

# Print the final product of all the numbers in the list
print("Product of list values:", product)
