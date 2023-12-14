import tkinter as tk

# Initialize the main window for the application
root = tk.Tk()
# Set the title of the main window
root.title("Login Page")

# Create a label for the username input and position it using the grid layout
# 'sticky="e"' aligns the label to the east (right side) within the grid cell
# 'padx' and 'pady' add padding on the x (horizontal) and y (vertical) axes for spacing
tk.Label(root, text="Username:").grid(row=0, column=0, sticky="e", padx=10, pady=10)

# Create an entry widget for the user to input their username
# This widget is placed in row 0, column 1 of the grid
user = tk.Entry(root)
user.grid(row=0, column=1, padx=10, pady=10)

# Create a label for the password input, similar to the username label
tk.Label(root, text="Password:").grid(row=1, column=0, sticky="e", padx=10, pady=10)

# Create an entry widget for the password, with the 'show' parameter
# This parameter ensures that the input is masked (e.g., with asterisks) for privacy
password = tk.Entry(root, show="*")
password.grid(row=1, column=1, padx=10, pady=10)

# Create a button for the user to attempt a login
# The 'command' parameter uses a lambda function to handle the button click
# The lambda function prints the username and password to the console
# This is a placeholder for the actual authentication logic you would implement
login = tk.Button(root, text="Login", command=lambda: print("Login attempt with username:", user.get(), "and password:", password.get()))
login.grid(row=2, column=0, columnspan=2, pady=10)

# Start the event loop to display the window and await user interaction
# The mainloop function is an infinite loop used to run the application,
# wait for an event to occur, and process the event until the window is closed
root.mainloop()
