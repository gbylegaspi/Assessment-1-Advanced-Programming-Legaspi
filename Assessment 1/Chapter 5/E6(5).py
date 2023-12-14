import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Define the ArithmeticOperations class with a result variable and a calculate function
class ArithmeticOperations:
    def __init__(self):
        self.result = 0

    # Function to perform an arithmetic operation based on user input
    def calculate(self, operation, num1, num2):
        try:
            num1, num2 = float(num1), float(num2)
            if operation == 'Add':
                self.result = num1 + num2
            elif operation == 'Subtract':
                self.result = num1 - num2
            elif operation == 'Multiply':
                self.result = num1 * num2
            elif operation == 'Divide':
                if num2 == 0:
                    messagebox.showerror("Error", "Cannot divide by zero.")
                    return None
                self.result = num1 / num2
            return self.result
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers.")
            return None

# GUI application class
class ArithmeticApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Arithmetic Operations")
        self.root.configure(bg='#282c34')  # Dark background color

        # Styling
        entry_font = ('Arial', 12)
        label_font = ('Arial', 12, 'bold')
        button_font = ('Arial', 12, 'bold')
        result_font = ('Arial', 14, 'bold')
        button_color = '#61afef'
        text_color = '#abb2bf'
        entry_bg = '#3c4049'
        entry_fg = 'white'

        # Instance of ArithmeticOperations
        self.arithmetic_operations = ArithmeticOperations()

        # Entry widgets for the values with styling
        self.num1_entry = tk.Entry(root, font=entry_font, bg=entry_bg, fg=entry_fg)
        self.num1_entry.pack(pady=5)
        self.num2_entry = tk.Entry(root, font=entry_font, bg=entry_bg, fg=entry_fg)
        self.num2_entry.pack(pady=5)

        # Combobox for selecting the arithmetic operation
        self.operation_var = tk.StringVar(root)
        self.operations = ('Add', 'Subtract', 'Multiply', 'Divide')
        self.operation_combobox = ttk.Combobox(root, textvariable=self.operation_var, values=self.operations, state='readonly', font=label_font)
        self.operation_combobox.set('Add')  # Default operation
        self.operation_combobox.pack(pady=5)

        # Button to perform the calculation with styling
        self.calculate_button = tk.Button(root, text="Calculate", command=self.perform_calculation, bg=button_color, fg=text_color, font=button_font)
        self.calculate_button.pack(pady=10)

        # Label to display the result with styling
        self.result_label = tk.Label(root, text="", bg='#282c34', fg='#98c379', font=result_font)
        self.result_label.pack(pady=5)

    # Function to invoke the calculate function and display the result
    def perform_calculation(self):
        operation = self.operation_var.get()
        num1 = self.num1_entry.get()
        num2 = self.num2_entry.get()
        result = self.arithmetic_operations.calculate(operation, num1, num2)
        if result is not None:
            self.result_label.config(text=f"Result: {result:.2f}")

# Initialize the Tkinter GUI application
root = tk.Tk()
app = ArithmeticApp(root)
root.geometry("300x200")  # Set a fixed size for the window
root.mainloop()
