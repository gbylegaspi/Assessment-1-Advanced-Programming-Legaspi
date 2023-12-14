import tkinter as tk
from tkinter import messagebox

# Function to save user input to a file and display it on the GUI
def save_and_display_info():
    # Get the name, age, and hometown from the respective entry fields
    name = name_entry.get()
    age = age_entry.get()
    hometown = hometown_entry.get()

    # Open the file bio.txt in write mode and write the data
    with open('bio.txt', 'w') as file:
        file.write(f"{name}\n{age}\n{hometown}")

    # Open the file bio.txt in read mode and read the data
    with open('bio.txt', 'r') as file:
        data = file.read()

    # Update the output label with the data read from the file
    output_label.config(text=data)

# Set up the main window of the application
root = tk.Tk()
root.title("Bio Data App")

# Create a frame to hold the input fields and add it to the main window
input_frame = tk.Frame(root)
input_frame.pack(padx=10, pady=10)

# Create a label and entry field for the name, and place them in the grid
name_label = tk.Label(input_frame, text="Name:")
name_label.grid(row=0, column=0)
name_entry = tk.Entry(input_frame)
name_entry.grid(row=0, column=1)

# Create a label and entry field for the age, and place them in the grid
age_label = tk.Label(input_frame, text="Age:")
age_label.grid(row=1, column=0)
age_entry = tk.Entry(input_frame)
age_entry.grid(row=1, column=1)

# Create a label and entry field for the hometown, and place them in the grid
hometown_label = tk.Label(input_frame, text="Hometown:")
hometown_label.grid(row=2, column=0)
hometown_entry = tk.Entry(input_frame)
hometown_entry.grid(row=2, column=1)

# Create a button that triggers the save_and_display_info function
save_button = tk.Button(input_frame, text="Save & Display", command=save_and_display_info)
save_button.grid(row=3, column=0, columnspan=2)

# Create a label to display the data read from the file
output_label = tk.Label(root, text="")
output_label.pack()

# Start the event loop to run the application
root.mainloop()
