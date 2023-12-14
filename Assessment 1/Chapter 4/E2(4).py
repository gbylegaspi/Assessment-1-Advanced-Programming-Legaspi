import tkinter as tk
from tkinter import filedialog, messagebox

# Initialize the main Tkinter window with a more appealing design
main_window = tk.Tk()
main_window.title("String Occurrence Counter")
main_window.configure(bg='#2E3440')  # Setting a dark background color

# Styling constants
BUTTON_COLOR = '#88C0D0'
TEXT_COLOR = 'white'
FRAME_BG = '#3B4252'
BUTTON_FONT = ('Arial', 12, 'bold')
TEXT_FONT = ('Arial', 10)

# Function to count the occurrences of specific strings in a text file
def count_occurrences():
    strings_to_count = [
        "Hello my name is Peter Parker",
        "I love Python Programming",
        "Love",
        "Enemy"
    ]

    file_path = filedialog.askopenfilename(title="Select a file", filetypes=[("Text files", "*.txt")])
    if not file_path:
        return

    try:
        with open(file_path, 'r') as file:
            content = file.read()

        occurrences = {string: content.count(string) for string in strings_to_count}

        result_text.config(state=tk.NORMAL)
        result_text.delete('1.0', tk.END)
        for string, count in occurrences.items():
            result_text.insert(tk.END, f'{string}: {count} occurrences\n')
        result_text.config(state=tk.DISABLED)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Frame for the result with a specific background color
result_frame = tk.Frame(main_window, bg=FRAME_BG)
result_frame.pack(padx=10, pady=10)

# Text widget for results with a custom font and color
result_text = tk.Text(result_frame, height=6, width=100, state=tk.DISABLED, fg=TEXT_COLOR, bg=FRAME_BG, font=TEXT_FONT)
result_text.pack()

# Button to start the counting process with a custom font and color
count_button = tk.Button(main_window, text="Count Occurrences", command=count_occurrences, bg=BUTTON_COLOR, fg=TEXT_COLOR, font=BUTTON_FONT)
count_button.pack(pady=10)

# Run the main event loop of the Tkinter application
main_window.geometry("600x200")  # Set window size
main_window.mainloop()
