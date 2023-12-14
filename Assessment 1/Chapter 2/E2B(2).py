import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("GUI Pack Example")

# Create frames with a border value of 5
left = tk.Frame(root, borderwidth=5)
right = tk.Frame(root, borderwidth=5)

# Pack frames into the main window to fill available space and allow resizing
left.pack(side="left", expand=True, fill="both")
right.pack(side="right", expand=True, fill="both")

# Create labels with a border value of 5
a = tk.Label(left, text="A", borderwidth=5)
b = tk.Label(left, text="B", borderwidth=5)
c = tk.Label(right, text="C", borderwidth=5)
d = tk.Label(right, text="D", borderwidth=5)

# Pack labels to align A and C at the top, and B and D at the bottom of their respective frames
# Use `expand` and `fill` options to support resizing and expand the labels into the available space
a.pack(side="top", expand=True, fill="both")
b.pack(side="bottom", expand=True, fill="both")
c.pack(side="top", expand=True, fill="both")
d.pack(side="bottom", expand=True, fill="both")

# Start the GUI loop
root.mainloop()
