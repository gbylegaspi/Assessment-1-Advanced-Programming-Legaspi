import re
import tkinter as tk
from tkinter import messagebox

# Function to check password validity
def check_password():
    password = pw_entry.get()
    if (6 <= len(password) <= 12 and
            re.search("[a-z]", password) and
            re.search("[A-Z]", password) and
            re.search("[0-9]", password) and
            re.search("[$#@]", password)):
        messagebox.showinfo("Success", "Password is valid.")
    else:
        global attempts
        attempts -= 1
        if attempts > 0:
            messagebox.showwarning("Warning", f"Invalid password. {attempts} attempts left.")
        else:
            messagebox.showerror("Error", "The police is on there way!!! lol")
            root.destroy()  # Close the application if the max attempts are reached

# Initialize the main application window
root = tk.Tk()
root.title("Password Validator")

# Maximum password attempts
attempts = 5

# Create a frame for the password entry
pw_frame = tk.Frame(root)
pw_frame.pack(padx=10, pady=10)

# Entry field for the password
pw_label = tk.Label(pw_frame, text="Enter password:")
pw_label.grid(row=0, column=0)
pw_entry = tk.Entry(pw_frame, show="*")  # The 'show' parameter masks the password input
pw_entry.grid(row=0, column=1)

# Button to check the password
check_button = tk.Button(pw_frame, text="Check Password", command=check_password)
check_button.grid(row=1, column=0, columnspan=2)

# Run the main application loop
root.mainloop()
