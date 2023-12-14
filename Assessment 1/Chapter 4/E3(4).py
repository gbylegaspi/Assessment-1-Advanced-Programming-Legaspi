import tkinter as tk
from tkinter import filedialog, messagebox

# Function to read numbers from a file and return them as a list of integers
def read_numbers_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            # Read each line, strip whitespace, and convert to integer
            numbers = [int(line.strip()) for line in file]
        return numbers
    except FileNotFoundError:
        messagebox.showerror("Error", "File not found.")
        return []
    except ValueError:
        messagebox.showerror("Error", "The file contains non-integer values.")
        return []

# Function to open a file dialog, read numbers from the selected file, and display them
def open_file_and_display_numbers():
    # Open a file dialog to select a text file
    file_path = filedialog.askopenfilename(title="Select a file", filetypes=[("Text files", "*.txt")])
    if file_path:
        numbers_list = read_numbers_from_file(file_path)

        # Display the numbers in the text widget
        result_text.config(state=tk.NORMAL)
        result_text.delete('1.0', tk.END)
        result_text.insert(tk.END, '\n'.join(map(str, numbers_list)))
        result_text.config(state=tk.DISABLED)

# Create the main Tkinter window
main_window = tk.Tk()
main_window.title("Integer Number Reader")

# Styling parameters
BG_COLOR = '#282c34'  # Background color
FG_COLOR = '#abb2bf'  # Foreground color
BUTTON_COLOR = '#61afef'
FONT = ('Arial', 11,)

# Set background color for the main window
main_window.configure(bg=BG_COLOR)

# Create a text widget to display the numbers with custom styling
result_text = tk.Text(main_window, height=15, width=50, state=tk.DISABLED, bg=BG_COLOR, fg=FG_COLOR, font=FONT)
result_text.pack(padx=10, pady=10)

# Create a button to open the file dialog with custom styling
open_file_button = tk.Button(main_window, text="Open File", command=open_file_and_display_numbers, bg=BUTTON_COLOR, fg=FG_COLOR, font=FONT)
open_file_button.pack(pady=10)

# Run the GUI application
main_window.mainloop()
