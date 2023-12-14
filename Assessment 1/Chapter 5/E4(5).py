import tkinter as tk
from tkinter import messagebox
import math

# Parent class Shape
class Shape:
    def __init__(self):
        self.sides = []

    # Method to input sides. For a circle, it will input the radius.
    def inputSides(self, sides):
        self.sides = sides

    # Placeholder for the area method to be overridden by subclasses
    def area(self):
        pass

# Subclass Circle
class Circle(Shape):
    def area(self):
        # Calculate the area of a circle: π * r^2
        return math.pi * (self.sides[0] ** 2)

# Subclass Rectangle
class Rectangle(Shape):
    def area(self):
        # Calculate the area of a rectangle: w * h
        return self.sides[0] * self.sides[1]

# Subclass Triangle
class Triangle(Shape):
    def area(self):
        # Calculate the area of a triangle using Heron's formula
        a, b, c = self.sides
        s = (a + b + c) / 2  # Semi-perimeter
        return (s * (s - a) * (s - b) * (s - c)) ** 0.5

# GUI application class
class ShapeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Area Calculator")

        # Define the color scheme
        self.bg_color = '#333333'  # Dark gray background
        self.text_color = '#FFFFFF'  # White text
        self.button_color = '#4CAF50'  # Green button
        self.entry_bg_color = '#555555'  # Lighter gray for entry

        # Set the background color for the application
        self.root.configure(bg=self.bg_color)

        # Label for instructions
        tk.Label(root, text="Select a shape and enter the required dimensions:", bg=self.bg_color, fg=self.text_color).pack()

        # Dropdown for shape selection
        self.shape_var = tk.StringVar(root)
        self.shapes = {'Circle': Circle(), 'Rectangle': Rectangle(), 'Triangle': Triangle()}
        self.shape_var.set('Circle')  # Default shape
        self.popupMenu = tk.OptionMenu(root, self.shape_var, *self.shapes.keys())
        self.popupMenu.config(bg=self.button_color, fg=self.text_color)
        self.popupMenu.pack()

        # Entry widgets for dimensions, with configured background and text color
        self.entry1 = tk.Entry(root, bg=self.entry_bg_color, fg=self.text_color, insertbackground=self.text_color)
        self.entry1.pack()
        self.entry2 = tk.Entry(root, bg=self.entry_bg_color, fg=self.text_color, insertbackground=self.text_color)
        self.entry2.pack()
        self.entry3 = tk.Entry(root, bg=self.entry_bg_color, fg=self.text_color, insertbackground=self.text_color)
        self.entry3.pack()

        # Function to update entry fields based on selected shape
        def change_dropdown(*args):
            shape = self.shape_var.get()
            # Reset entries and adjust visible entry fields according to the selected shape
            self.entry1.delete(0, tk.END)
            self.entry2.delete(0, tk.END)
            self.entry3.delete(0, tk.END)
            if shape == 'Circle':
                self.entry2.pack_forget()
                self.entry3.pack_forget()
            elif shape == 'Rectangle':
                self.entry2.pack()
                self.entry3.pack_forget()
            else:  # Triangle
                self.entry2.pack()
                self.entry3.pack()

        # Watch for changes in the shape dropdown to update UI accordingly
        self.shape_var.trace('w', change_dropdown)

        # Button to calculate the area with configured background and text color
        tk.Button(root, text="Calculate Area", command=self.calculate_area, bg=self.button_color, fg=self.text_color).pack()

    # Method to calculate and display the area
    def calculate_area(self):
        shape = self.shapes[self.shape_var.get()]
        try:
            # Get input from the user and calculate the area
            if self.shape_var.get() == 'Circle':
                sides = [float(self.entry1.get())]
            elif self.shape_var.get() == 'Rectangle':
                sides = [float(self.entry1.get()), float(self.entry2.get())]
            else:  # Triangle
                sides = [float(self.entry1.get()), float(self.entry2.get()), float(self.entry3.get())]
            shape.inputSides(sides)
            area = shape.area()
            messagebox.showinfo("Result", f"The area of the {self.shape_var.get()} is: {area}")
        except ValueError:
            # Handle the error if the input is not a valid number
            messagebox.showerror("Error", "Please enter valid numbers for dimensions.")

# Initialize the Tkinter GUI application
root = tk.Tk()
app = ShapeApp(root)
root.geometry("300x200")  # Set a fixed size for the window
root.mainloop()
