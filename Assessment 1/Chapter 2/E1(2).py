import tkinter as tk

# Create the main window
root = tk.Tk()

# Set the title of the window (optional)
root.title("Welcome App")

# Set the default window size to 400 pixels width and 300 pixels height
root.geometry("400x300")

# Disable resizing of the window. This makes the window fixed in size,
# and the user cannot change its dimensions.
root.resizable(False, False)

# Add background color to the window. 'lightblue' is the color name,
# but you can use hex color codes as well.
root.configure(bg='lightblue')

# Create a label widget. This will display text on the window.
# "wassup bro" is the text displayed.
# We set the font to 'Helvetica', with a size of 16 and make it bold.
# The background color of the label is also set to 'lightblue' to match the window.
welcome_label = tk.Label(root, text="wassup bro", font=("Helvetica", 16, "bold"), bg='lightblue')

# Place the label on the window. 'pack()' is a geometry manager that handles the widget's position. 
# 'pady=50' provides vertical padding of 50 pixels from the top and bottom of the label to other elements.
welcome_label.pack(pady=50)

# Run the application's main loop. This call is necessary for making the window appear
# and wait for user interaction until the application is closed.
root.mainloop()
