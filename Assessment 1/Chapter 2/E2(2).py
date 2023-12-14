import tkinter as tk

# Create the main application window
root = tk.Tk()
root.title("GUI Pack Example")

# Set the default window size
root.geometry("400x300")
# Configure the background color of the window
root.configure(bg='white')

# Create labels with specified background colors, border widths, and relief styles
# Label A with red background, raised border
label_a = tk.Label(root, text="A", bg="red", bd=5, relief="raised")
# Label B with yellow background, sunken border
label_b = tk.Label(root, text="B", bg="yellow", bd=5, relief="sunken")
# Label C with blue background, groove border
label_c = tk.Label(root, text="C", bg="blue", bd=5, relief="groove")
# Label D with green background, ridge border
label_d = tk.Label(root, text="D", bg="green", bd=5, relief="ridge")

# Arrange the labels using pack geometry manager with the specified fill and expand options
label_a.pack(fill=tk.X)        # Label A fills the X direction
label_b.pack(side=tk.BOTTOM, fill=tk.X)  # Label B at the bottom, fills the X direction
label_c.pack(side=tk.LEFT, fill=tk.Y)    # Label C on the left, fills the Y direction
label_d.pack(side=tk.LEFT, fill=tk.BOTH, expand=True) # Label D on the left, fills both directions and expands

# Start the Tkinter event loop
root.mainloop()
