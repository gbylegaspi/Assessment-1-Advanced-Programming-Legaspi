import tkinter as tk
from tkinter import messagebox

# Employee class to store employee details
class Employee:
    def __init__(self, name='', position='', id=0, salary=0.0):
        self.name = name
        self.position = position
        self.id = id
        self.salary = salary

    # Method to set the data for an employee
    def setData(self, name, position, id, salary):
        self.name = name
        self.position = position
        self.id = id
        self.salary = salary

    # Method to return the employee's data in a string format
    def getData(self):
        return f"{self.name}\t{self.position}\t{self.salary}\t{self.id}"

# GUI application class
class EmployeeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Employee Data Entry")
        
        self.employees = []  # List to store employees

        background_color = '#191414'  
        text_color = '#FFFFFF'  
        accent_color = '#1DB954'  
        entry_background = '#535353'  
        
        self.root.configure(bg=background_color)  # Set the background color

        # Define the style for labels 
        label_style = {'bg': background_color, 'fg': text_color}

        # Create labels
        tk.Label(root, text="Name:", **label_style).grid(row=0, column=0, sticky='w')
        tk.Label(root, text="Position:", **label_style).grid(row=1, column=0, sticky='w')
        tk.Label(root, text="Salary:", **label_style).grid(row=2, column=0, sticky='w')
        tk.Label(root, text="ID:", **label_style).grid(row=3, column=0, sticky='w')
        
        # Create entry fields 
        self.name_entry = tk.Entry(root, fg=text_color, bg=entry_background, insertbackground=text_color)
        self.name_entry.grid(row=0, column=1)
        
        self.position_entry = tk.Entry(root, fg=text_color, bg=entry_background, insertbackground=text_color)
        self.position_entry.grid(row=1, column=1)
        
        self.salary_entry = tk.Entry(root, fg=text_color, bg=entry_background, insertbackground=text_color)
        self.salary_entry.grid(row=2, column=1)
        
        self.id_entry = tk.Entry(root, fg=text_color, bg=entry_background, insertbackground=text_color)
        self.id_entry.grid(row=3, column=1)
        
        # Create buttons 
        tk.Button(root, text="Add Employee", command=self.add_employee, fg=text_color, bg=accent_color).grid(row=4, column=0)
        tk.Button(root, text="Display Employees", command=self.display_employees, fg=text_color, bg=accent_color).grid(row=4, column=1)
        
    # Method to add an employee to the list
    def add_employee(self):
        name = self.name_entry.get()
        position = self.position_entry.get()
        salary = self.salary_entry.get()
        id = self.id_entry.get()
        
        # Validation to ensure all fields are filled
        if not all([name, position, id, salary]):
            messagebox.showerror("Error", "Please fill in all fields.")
            return
        
        # Limit the number of employees to 5
        if len(self.employees) >= 5:
            messagebox.showinfo("Info", "Maximum of 5 employees have been added.")
            return
        
        try:
            # Convert ID and salary to proper data types
            id = int(id)
            salary = float(salary)
        except ValueError:
            messagebox.showerror("Error", "Please enter valid number for ID and salary.")
            return

        # Create a new Employee object and add it to the list
        new_employee = Employee(name, position, id, salary)
        self.employees.append(new_employee)
        
        # Clear the entry fields after adding an employee
        self.name_entry.delete(0, tk.END)
        self.position_entry.delete(0, tk.END)
        self.salary_entry.delete(0, tk.END)
        self.id_entry.delete(0, tk.END)
        
        # Confirmation message
        messagebox.showinfo("Info", f"Employee {name} added successfully.")
    
    # Method to display all employees in a message box
    def display_employees(self):
        output = "Name\tPosition\tSalary\tID\n"
        for emp in self.employees:
            output += emp.getData() + "\n"
        messagebox.showinfo("Employee List", output)

# Initialize the Tkinter GUI application
root = tk.Tk()
app = EmployeeApp(root)
root.mainloop()
