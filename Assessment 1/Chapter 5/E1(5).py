import tkinter as tk
from datetime import datetime

# Initialize the main window for the application
app_window = tk.Tk()
app_window.title("Dog Information Display")
app_window.geometry("200x100")

# Define a class Dog to store and handle dog-related information
class Dog:
    # Constructor to initialize a Dog object
    def __init__(self, dog_name, birth_date, dog_breed):
        self.name = dog_name
        self.birthdate = datetime.strptime(birth_date, '%Y-%m-%d')
        self.breed = dog_breed

    # Method to return information about the dog
    def get_info(self):
        return f"Name: {self.name}\nBirthdate: {self.birthdate.strftime('%Y-%m-%d')}\nBreed: {self.breed}\n"

    # Method to determine the dog's 'woof' based on its age
    def woof(self):
        age = datetime.now().year - self.birthdate.year
        return f"{self.name} says Woof!" if age >= 0 else f"{self.name} is not old enough to woof yet."

# Function to create Dog objects and identify the oldest dog
def create_dogs_display_oldest():
    # List of Dog objects
    dogs_list = [
        Dog("Jack", "2009-10-08", "Golden Retriever"),
        Dog("Buddy", "2023-10-22", "Labrador Retriever")
    ]

    # Finding the oldest dog
    oldest_dog = min(dogs_list, key=lambda dog: dog.birthdate)

    # Print information for each dog
    for dog in dogs_list:
        print(dog.get_info())

    # Print information about the oldest dog
    print(f"The oldest dog is {oldest_dog.name} who woofs {oldest_dog.woof()}")

# Frame for the button in the main window
button_frame = tk.Frame(app_window)
button_frame.pack()

# Button to trigger the creation and display of dog information
dogs_button = tk.Button(button_frame, text="Create Dogs", command=create_dogs_display_oldest)
dogs_button.pack(pady=20)

# Start the application's main loop
app_window.mainloop()
