import operator  # Import the operator module for arithmetic operations

# Function to get and validate user input
def get_input(prompt):
    """ Helper function to handle user input and validation. """
    while True:  # Infinite loop to keep asking for input until valid
        try:
            return float(input(prompt))  # Convert input to float and return it
        except ValueError:  # Handle exception if input is not a number
            print("Invalid input. Please enter a number.")

# Function to display the calculator menu
def calculator_menu():
    """ Displays the calculator operations menu. """
    print("Calculator Menu:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulus")
    print("6. Check greater number")
    print("Enter Q to quit")

# Function to perform the selected operation
def perform_operation(choice, a, b):
    """ Perform calculation based on user choice using operator module. """
    # Dictionary mapping choices to corresponding operator functions
    operations = {
        '1': operator.add,
        '2': operator.sub,
        '3': operator.mul,
        '4': operator.truediv,
        '5': operator.mod,
        '6': max  # max function to check the greater number
    }

    # Execute the operation if the choice is valid
    if choice in operations:
        return operations[choice](a, b)
    else:
        return "Invalid choice"

# Main function to run the calculator program
def main():
    while True:  # Infinite loop for continuous operation
        calculator_menu()  # Display the calculator menu
        choice = input("Choose an operation (1-6) or Q to quit: ").strip()  # Get user choice

        if choice.upper() == 'Q':  # Check if user wants to quit
            break  # Break the loop to end the program

        # Check if the choice is one of the valid operations
        if choice in ['1', '2', '3', '4', '5', '6']:
            a = get_input("Enter first number: ")  # Get first number
            b = get_input("Enter second number: ")  # Get second number

            result = perform_operation(choice, a, b)  # Perform the operation and get the result
            print(f"Result: {result}")  # Display the result
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")  # Handle invalid choice

# Check if the script is run directly (not imported)
if __name__ == "__main__":
    main()  # Run the main function
