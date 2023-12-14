import tkinter as tk

# Define a function to draw the selected shape on the canvas
def draw_shape():
    # Retrieve the shape selected by the user from the dropdown
    shape = shape_var.get()
    # Split the string of coordinates entered by the user and convert them to integers
    coords = list(map(int, coord_entry.get().split(',')))
    
    # Draw the selected shape on the canvas using the coordinates provided
    if shape == 'Rectangle':
        # For a rectangle, expect four coordinates: x1, y1, x2, y2
        canvas.create_rectangle(*coords, outline='black', fill='')
    elif shape == 'Oval':
        # For an oval, expect four coordinates representing the bounding box: x1, y1, x2, y2
        canvas.create_oval(*coords, outline='black', fill='')
    elif shape == 'Square':
        # For a square, expect three coordinates: x1, y1, side length
        # Draw a rectangle where the width and height are both the side length
        canvas.create_rectangle(coords[0], coords[1], coords[0]+(coords[2]-coords[0]), coords[1]+(coords[2]-coords[0]), outline='black', fill='')
    elif shape == 'Triangle':
        # For a triangle, expect six coordinates representing three vertices: x1, y1, x2, y2, x3, y3
        canvas.create_polygon(*coords, outline='black', fill='')

# Create the main application window
root = tk.Tk()
root.title("Shape Drawer")

# Create a frame to hold the shape selection dropdown
shape_frame = tk.Frame(root)
shape_frame.pack(padx=10, pady=10)

# Create a StringVar to hold the value of the selected shape
shape_var = tk.StringVar(value='Rectangle')
# Define the list of shapes that can be drawn
shape_options = ['Rectangle', 'Oval', 'Square', 'Triangle']

# Add a label and a dropdown menu to the shape selection frame
shape_label = tk.Label(shape_frame, text="Select Shape:")
shape_label.pack(side='left')
shape_menu = tk.OptionMenu(shape_frame, shape_var, *shape_options)
shape_menu.pack(side='left')

# Create a frame to hold the coordinate input field
coord_frame = tk.Frame(root)
coord_frame.pack(padx=10, pady=10)

# Add a label and an entry widget to the coordinate input frame
coord_label = tk.Label(coord_frame, text="Enter coordinates:")
coord_label.pack()
coord_entry = tk.Entry(coord_frame)
coord_entry.pack()

# Create a canvas widget where shapes will be drawn
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

# Add a button that will call the draw_shape function when clicked
draw_button = tk.Button(root, text="Draw Shape", command=draw_shape)
draw_button.pack(pady=10)

# Start the main loop to run the application
root.mainloop()
