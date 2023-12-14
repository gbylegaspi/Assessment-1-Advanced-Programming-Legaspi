# Display the menu with options for calculating the area of different shapes
print("1: Area of a square\n2: Area of a circle\n3: Area of a triangle")

# Prompt the user to choose an option by entering the corresponding number
choice = int(input("Choose an option by typing the number: "))

# Process the user's choice
if choice == 1:
    # If the user chooses 1, calculate the area of a square
    side = float(input("Enter the side of a square: "))  # Get the side length of the square from the user
    square = side * side  # Calculate the area of the square
    print("Square area:", square)  # Display the calculated area
elif choice == 2:
    # If the user chooses 2, calculate the area of a circle
    radius = float(input("Enter the radius of a circle: "))  # Get the radius of the circle from the user
    circle = 3.14 * radius**2  # Calculate the area of the circle using the formula πr² (π approximated as 3.14)
    print("Circle area:", circle)  # Display the calculated area
elif choice == 3:
    # If the user chooses 3, calculate the area of a triangle
    base = float(input("Enter the base of a triangle: "))  # Get the base length of the triangle from the user
    height = float(input("Enter the height of a triangle: "))  # Get the height of the triangle from the user
    triangle = 0.5 * base * height  # Calculate the area of the triangle using the formula ½ × base × height
    print("Triangle area:", triangle)  # Display the calculated area
else:
    # If the user enters a choice other than 1, 2, or 3, inform them of the invalid choice
    print("Invalid choice")

