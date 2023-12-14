import tkinter as tk
from tkinter import messagebox

# Define the Animal class with its attributes and methods
class Animal:
    def __init__(self, animal_type='', name='', colour='', age=0, weight=0.0, noise=''):
        self.animal_type = animal_type
        self.name = name
        self.colour = colour
        self.age = age
        self.weight = weight
        self.noise = noise

    # Method to simulate the animal saying hello
    def sayHello(self):
        print(f"Hello, my name is {self.name}.")

    # Method to simulate the animal making noise
    def makeNoise(self):
        print(f"{self.name} says {self.noise}.")

    # Method to display the animal's details
    def animalDetails(self):
        details = (
            f"Type: {self.animal_type}\n"
            f"Name: {self.name}\n"
            f"Colour: {self.colour}\n"
            f"Age: {self.age}\n"
            f"Weight: {self.weight} kg\n"
            f"Noise: {self.noise}\n"
        )
        print(details)
        messagebox.showinfo(f"{self.name}'s Details", details)

# GUI application class
class AnimalApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Animal Class Interaction")

        # Instantiate at least two objects from the Animal class
        self.dog = Animal("Dog", "Rocky", "White", 3, 20, "Woof Woof")
        self.cow = Animal("Cow", "Stella", "Brown", 2, 150, "Mooooo")

        # Function to invoke class functions for the dog
        def interact_with_dog():
            self.dog.sayHello()
            self.dog.makeNoise()
            self.dog.animalDetails()

        # Function to invoke class functions for the cow
        def interact_with_cow():
            self.cow.sayHello()
            self.cow.makeNoise()
            self.cow.animalDetails()

        # Buttons to interact with the dog and cow
        tk.Button(root, text="Interact with Dog", command=interact_with_dog).pack()
        tk.Button(root, text="Interact with Cow", command=interact_with_cow).pack()

# Initialize the Tkinter GUI application
root = tk.Tk()
app = AnimalApp(root)
root.mainloop()
