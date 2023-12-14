import tkinter as tk
from math import pi

# Function to calculate the area of a circle and display the result
def calculate_circle():
    radius = float(circle_radius.get())
    area = pi * radius**2
    circle_area.config(text=f"Area: {area:.2f}")

# Function to calculate the area of a square and display the result
def calculate_square():
    side = float(square_side.get())
    area = side * side
    square_area.config(text=f"Area: {area:.2f}")

# Function to calculate the area of a rectangle and display the result
def calculate_rectangle():
    length = float(rect_length.get())
    width = float(rect_width.get())
    area = length * width
    rectangle_area.config(text=f"Area: {area:.2f}")

# Main window initialization
root = tk.Tk()
root.title("Area Calculator")

# Frame for circle calculation
circle_frame = tk.Frame(root, bg='#FFDDC1')
circle_frame.pack(padx=10, pady=5, fill='x')
tk.Label(circle_frame, text="Circle Radius:", bg='#FFDDC1').pack(side='left')
circle_radius = tk.Entry(circle_frame)
circle_radius.pack(side='left')
tk.Button(circle_frame, text="Calculate Area", command=calculate_circle).pack(side='left')
circle_area = tk.Label(circle_frame, text="Area: ", bg='#FFDDC1')
circle_area.pack(side='left')

# Frame for square calculation
square_frame = tk.Frame(root, bg='#D1FFC1')
square_frame.pack(padx=10, pady=5, fill='x')
tk.Label(square_frame, text="Square Side:", bg='#D1FFC1').pack(side='left')
square_side = tk.Entry(square_frame)
square_side.pack(side='left')
tk.Button(square_frame, text="Calculate Area", command=calculate_square).pack(side='left')
square_area = tk.Label(square_frame, text="Area: ", bg='#D1FFC1')
square_area.pack(side='left')

# Frame for rectangle calculation
rect_frame = tk.Frame(root, bg='#C1D1FF')
rect_frame.pack(padx=10, pady=5, fill='x')
tk.Label(rect_frame, text="Rectangle Length:", bg='#C1D1FF').pack(side='left')
rect_length = tk.Entry(rect_frame)
rect_length.pack(side='left')
tk.Label(rect_frame, text="Width:", bg='#C1D1FF').pack(side='left')
rect_width = tk.Entry(rect_frame)
rect_width.pack(side='left')
tk.Button(rect_frame, text="Calculate Area", command=calculate_rectangle).pack(side='left')
rectangle_area = tk.Label(rect_frame, text="Area: ", bg='#C1D1FF')
rectangle_area.pack(side='left')

# Run the main application loop
root.mainloop()
