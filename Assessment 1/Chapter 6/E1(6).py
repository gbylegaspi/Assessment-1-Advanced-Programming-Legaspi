import math

def display_results():
    # Given value
    a = 2.3

    # Perform calculations
    ceil_a = math.ceil(a)  # Ceiling of a
    floor_a = math.floor(a)  # Floor of a
    factorial_5 = math.factorial(5)  # Factorial of 5
    value_2_cube = 2 ** 3  # Cube of 2
    sqrt_16 = math.sqrt(16)  # Square root of 16

    # Print the results with explanations
    print(f"The ceiling of {a} is {ceil_a}.")
    print(f"The floor of {a} is {floor_a}.")
    print("The factorial of 5 is {}.".format(factorial_5))
    print("The value of 2 cubed (2^3) is {}.".format(value_2_cube))
    print("The square root of 16 is {}.".format(sqrt_16))

# Call the function to display the results
display_results()
