import tkinter as tk
from tkinter import ttk

# Function to update the greeting displayed on the label
def update_greeting():
    # Retrieve the name from the entry widget and the selected color from the dropdown
    name1 = name.get()
    selected_color = color1.get()
    
    # Set the greeting label's text to a personalized greeting using the retrieved name
    # and set its text color to the chosen color from the dropdown
    greet.config(text=f"Sup, {name1}!", fg=selected_color)

# Set up the main application window with a title
root = tk.Tk()
root.title("Personalized Greeting App")

# Define the background colors for the frames and button, and text color for the title label
bgcolor = '#DDEEFF'  # Background color for the input frame
bgcolor2 = '#CCDDFF'  # Background color for the display frame
text = 'blue'  # Text color for the title label
buttonC = '#AACCEE'  # Background color for the update button

# Input frame where user can input their details
input = tk.Frame(root, bg=bgcolor)
input.pack(padx=10, pady=10, fill='x')

# Title label within the input frame
title = tk.Label(input, text="Enter your name:", fg=text, bg=bgcolor)
title.pack()

# Entry widget for the user to input their name
name = tk.Entry(input)
name.pack(pady=5)

# Dropdown menu (Combobox) for selecting a greeting color
color1 = tk.StringVar(value='black')  # Variable to store the selected color, default is black
color2 = ttk.Combobox(input, textvariable=color1, values=['red', 'green', 'blue', 'black'])
color2.pack(pady=5)

# Button that, when clicked, calls the function to update the greeting label
button = tk.Button(input, text="Update Greeting", command=update_greeting, bg=buttonC)
button.pack(pady=5)

# Display frame for showing the personalized greeting after the button is clicked
display = tk.Frame(root, bg=bgcolor2)
display.pack(padx=10, pady=10, fill='both', expand=True)

# Label in the display frame where the personalized greeting will be shown
greet = tk.Label(display, text="", bg=bgcolor2)
greet.pack(expand=True)

# Start the Tkinter main loop to render the GUI and wait for user interactions
root.mainloop()
