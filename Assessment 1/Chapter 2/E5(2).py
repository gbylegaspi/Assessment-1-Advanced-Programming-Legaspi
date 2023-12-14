import tkinter as tk

# Initialize the main window
root = tk.Tk()
root.title("Basic Calculator")
# You can adjust the window size as needed
root.geometry("300x200")

# Function to update the result label with the calculation result or an error message
def update_result(text):
    result.config(text=f"Result: {text}")

# Function to perform calculation based on the operation parameter
def calculate(operation):
    try:
        # Retrieve numbers from the entry widgets, converting them to float for calculation
        a = float(usera.get())
        b = float(userb.get())

        # Dictionary mapping operations to their respective calculations
        diction = {
            '+': a + b,
            '-': a - b,
            '*': a * b,
            '/': a / b if b != 0 else "Error: Div by zero",  # Guard against division by zero
            '%': a % b if b != 0 else "Error: Div by zero"
        }

        # Perform the operation and update the result label
        update_result(diction[operation])

    except ValueError:
        # If the numbers entered are not valid, update the result label with an error message
        update_result("Error: Invalid Input")

# Entry widget for the first number
usera = tk.Entry(root)
usera.grid(row=0, column=0, columnspan=4, padx=5, pady=5)  # Span across the grid for alignment

# Entry widget for the second number
userb = tk.Entry(root)
userb.grid(row=1, column=0, columnspan=4, padx=5, pady=5)  # Span across the grid for alignment

# Define the calculator's diction
diction = ['+', '-', '*', '/', '%']
# Create a button for each operation using a loop
for i, operation in enumerate(diction):
    # Lambda function captures the operation and passes it to the calculate function
    button = tk.Button(root, text=operation, command=lambda op=operation: calculate(op))
    button.grid(row=2, column=i, padx=5, pady=5)  # Place buttons in a row

# Label to display the result of the calculation
result = tk.Label(root, text="Result: ")
result.grid(row=3, column=0, columnspan=4)  # Span across the grid to center align

# Start the Tkinter event loop to display the window and await user interactions
root.mainloop()
