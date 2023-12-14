# Initialize a counter variable to count the number of loop executions
looped = 0

# Start a while loop that will continue as long as the user inputs 'Y'
while True:
    # Ask the user if they want to continue
    a = input("Do you want to continue? (Y/N): ").upper()

    # Check if the user entered 'Y'
    if a == 'Y':
        # Increment the counter
        looped += 1
    else:
        # Break out of the loop if the input is not 'Y'
        break

# After the loop ends, print the number of times the loop was executed
print("This looped", looped, "times.")
