import tkinter as tk
import tkinter.simpledialog as simpledialog

# Function to handle coffee purchase process
def purchase_coffee():
    # Retrieve the name and coffee preferences
    name = nameE.get()
    coffee = coffeeV.get()
    sugar = 'with sugar' if sugarV.get() else 'without sugar'
    milk = 'with milk' if milkV.get() else 'without milk'
    
    # Set the price for the coffee
    yawa = 2.5
    
    # Prompt user for payment
    bayad = simpledialog.askfloat("Bayad", f"Hello, {name}. Your total is ${yawa}. Please enter your payment amount:")
    
    # Check payment amount and provide feedback
    if bayad is not None:
        if bayad >= yawa:
            sukle = bayad - yawa
            result.config(text=f"Thank you, {name}! Here is your {coffee} {sugar} and {milk}. Your change is ${sukle:.2f}.")
        else:
            result.config(text=f"That's not enough money, {name}. Please try again.")
    else:
        result.config(text=f"Purchase cancelled, {name}.")

# Initialize the main application window
root = tk.Tk()
root.title("Coffee Vending Machine")

# Frame for user input
input1 = tk.Frame(root)
input1.pack(padx=10, pady=10)

# Label and entry for user name
nameL = tk.Label(input1, text="Enter your name:")
nameL.pack()
nameE = tk.Entry(input1)
nameE.pack()

# Variable and menu for coffee selection
coffeeV = tk.StringVar(value='Espresso')
coffeeL = tk.Label(input1, text="Choose your coffee:")
coffeeL.pack()
menu = tk.OptionMenu(input1, coffeeV, 'Espresso', 'Latte', 'Cappuccino', 'Americano')
menu.pack()

# Variables and checkboxes for additional options
sugarV = tk.BooleanVar()
milkV = tk.BooleanVar()
checkbox1 = tk.Checkbutton(input1, text="Add sugar", variable=sugarV)
checkbox1.pack()
checkbox2 = tk.Checkbutton(input1, text="Add milk", variable=milkV)
checkbox2.pack()

# Button to confirm the order and trigger the purchase process
button1 = tk.Button(input1, text="Update Greeting", command=purchase_coffee)
button1.pack()

# Frame for displaying the result of the purchase
display1 = tk.Frame(root)
display1.pack(padx=10, pady=10, fill='both', expand=True)

# Label for showing the result
result = tk.Label(display1, text="")
result.pack()

# Start the Tkinter event loop
root.mainloop()
