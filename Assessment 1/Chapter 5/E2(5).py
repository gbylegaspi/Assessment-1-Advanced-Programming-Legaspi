import tkinter as tk

class Student:
    def __init__(self, name, m1, m2, m3):
        # Constructor for the Student class to initialize the student's name and marks
        self.name = name
        self.m1 = int(m1)
        self.m2 = int(m2)
        self.m3 = int(m3)

    def calcGrade(self):
        # Method to calculate the average of the three marks
        return (self.m1 + self.m2 + self.m3) / 3

    def display(self):
        # Method to create a display string with the student's name and average grade
        avg = self.calcGrade()
        return f"{self.name} Average: {avg:.2f}"

def create_student():
    # Function to handle the button click event; creates a student and updates the display
    student = Student(name_e.get(), m1_e.get(), m2_e.get(), m3_e.get())
    result.config(text=student.display())

# Set up the main window
root = tk.Tk()
root.title("Student Grades")

# Create and pack the label and entry for the student's name
name_l = tk.Label(root, text="Name:")
name_l.pack()
name_e = tk.Entry(root)
name_e.pack()

# Create and pack the label and entry for the student's first mark
m1_l = tk.Label(root, text="Mark 1:")
m1_l.pack()
m1_e = tk.Entry(root)
m1_e.pack()

# Create and pack the label and entry for the student's second mark
m2_l = tk.Label(root, text="Mark 2:")
m2_l.pack()
m2_e = tk.Entry(root)
m2_e.pack()

# Create and pack the label and entry for the student's third mark
m3_l = tk.Label(root, text="Mark 3:")
m3_l.pack()
m3_e = tk.Entry(root)
m3_e.pack()

# Create and pack the button that will create the student object
create_b = tk.Button(root, text="Create", command=create_student)
create_b.pack()

# Create and pack the label that will display the student information
result = tk.Label(root, text="")
result.pack()

# Start the Tkinter event loop
root.mainloop()
