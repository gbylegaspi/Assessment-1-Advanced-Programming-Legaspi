import tkinter as tk
from tkinter import ttk

# Initialize the main window for the application
root = tk.Tk()
root.title("New Student Registration")
# Set the window size to 400x600 pixels
root.geometry("400x600")

# Load the university logo image from a specified path
# Make sure to use the correct path where the image is located on your system
logo = tk.PhotoImage(file=r"D:\Advanced prog acts\Assessment 1\Chapter 2\Screenshot 2023-12-13 105305.png")

# Create a frame to hold the header content with a navy background
header = tk.Frame(root, bg='navy')
# Make the header frame expand the full width of the window
header.pack(fill='x')

# Add the university logo to the header frame
logoL = tk.Label(header, image=logo, bg='navy')
# Add some vertical padding and display it at the top of the header frame
logoL.pack(side='top', pady=10)

# Add a title label below the logo with specified font and color
title = tk.Label(header, text="Student Management System\nNew Student Registration",
                 font=('Helvetica', 16, 'bold'), fg='white', bg='navy')
# Make the title expand the full width of the header frame and pack it below the logo
title.pack(side='top', fill='x')

# Set up the main form frame for input fields
form = tk.Frame(root)
# Add horizontal and vertical padding around the form frame
form.pack(padx=10, pady=10)

# Define labels for each input field in the form
labels = ['Student Name', 'Mobile Number', 'Email Id', 'Home Address', 'Gender', 'Course Enrolled', 'Languages known', 'Rate your English communication skills']
# Create a dictionary to store the entry widgets for each label
entries = {}

# Loop through the labels and create corresponding input fields
for i, label in enumerate(labels[:-3]):
    # Create and place a label for the input field
    tk.Label(form, text=label).grid(row=i, column=0, sticky='W', pady=2)
    # Create an entry widget, place it next to the label, and store it in the dictionary
    entry = tk.Entry(form)
    entry.grid(row=i, column=1, pady=2, sticky='EW')
    entries[label] = entry

# Create a dropdown for gender selection using a Combobox widget
gender = tk.StringVar()
genderbox = ttk.Combobox(form, textvariable=gender, values=["Male", "Female", "Other"], state='readonly')
genderbox.grid(row=4, column=1, pady=2, sticky='EW')

# Create radio buttons for course enrollment selection
course = tk.StringVar(value='BSc CC')  # Set a default value
courses = ['BSc CC', 'BSc CY', 'BSc PSY', 'BA & BM']
# Iterate over the courses and create a radio button for each
for i, c in enumerate(courses):
    tk.Radiobutton(form, text=c, variable=course, value=c).grid(row=5+i, column=1, sticky='W')

# Create a frame for language checkboxes with a title
lang = tk.LabelFrame(form, text="Languages known", padx=5, pady=5)
lang.grid(row=9, column=0, columnspan=2, pady=5, sticky='EW')
# Create checkbox variables to keep track of selections
english_var, tagalog_var, hindi_urdu_var = tk.BooleanVar(), tk.BooleanVar(), tk.BooleanVar()
# Create and pack the checkboxes inside the languages frame
tk.Checkbutton(lang, text="English", variable=english_var).pack(side='left')
tk.Checkbutton(lang, text="Tagalog", variable=tagalog_var).pack(side='left')
tk.Checkbutton(lang, text="Hindi/Urdu", variable=hindi_urdu_var).pack(side='left')

# Create a scale widget for rating English communication skills
tk.Label(form, text="Rate your English communication skills").grid(row=10, column=0, sticky='W', pady=2)
com = tk.Scale(form, from_=0, to=10, orient='horizontal')
com.grid(row=10, column=1, pady=2, sticky='EW')

# Create Submit and Clear buttons and place them in the form frame
submit = tk.Button(form, text="Submit", bg='blue', fg='white')
submit.grid(row=11, column=0, pady=10)
clear = tk.Button(form, text="Clear", bg='blue', fg='white')
clear.grid(row=11, column=1, pady=10)

# Ensure that the second column of the form expands to fill the available space when the window is resized
form.columnconfigure(1, weight=1)

# Enter the Tkinter main event loop to display the window and start the application
root.mainloop()
