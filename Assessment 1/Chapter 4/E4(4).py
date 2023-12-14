import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox

# Function to count the occurrences of a character in a file
def count_character_in_file(character, file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            return content.count(character)
    except FileNotFoundError:
        messagebox.showerror("Error", "File not found.")
        return None
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
        return None

# Function to prompt for character input, open file dialog, and display the count
def get_character_and_count():
    # Ask the user to enter a character
    character = simpledialog.askstring("Input", "Enter a character to count:")
    
    # Validate the character input
    if not character or len(character) != 1:
        messagebox.showerror("Error", "Please enter a single character.")
        return

    # Open a file dialog to select a text file
    file_path = filedialog.askopenfilename(title="Select a file", filetypes=[("Text files", "*.txt")])
    if not file_path:
        return

    # Count the occurrences of the character
    count = count_character_in_file(character, file_path)
    if count is not None:
        messagebox.showinfo("Result", f"The character '{character}' appears {count} times in the file.")

# Create the main Tkinter window
main_window = tk.Tk()
main_window.title("Character Occurrence Counter")

# Styling parameters
BUTTON_COLOR = '#61afef'
FONT = ('Arial', 11)

# Create a button to start the process
start_button = tk.Button(main_window, text="Count Character", command=get_character_and_count, bg=BUTTON_COLOR, fg='white', font=FONT)
start_button.pack(pady=20)

# Run the GUI application
main_window.geometry("300x100")  # Set a fixed size for the window
main_window.mainloop()
