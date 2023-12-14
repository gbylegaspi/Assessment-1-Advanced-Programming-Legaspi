for number in range(1, 101):  # Looping through numbers from 1 to 100
    if number % 2 != 0:  # Check if the number is odd
        continue  # If it's odd, skip the rest of the loop and continue with the next iteration
    print(number)  # If it's even, print the number