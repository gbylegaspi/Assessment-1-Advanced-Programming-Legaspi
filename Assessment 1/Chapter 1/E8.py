# Outer loop for the number of rows
for i in range(1, 6):  # Range 1 to 5 for 5 rows
    # Inner loop for each row
    for j in range(1, i + 1):  # Increase the range in each iteration
        print(j, end=" ")  # Print the number and stay on the same line
    print()  # Print a newline after each row is completed
