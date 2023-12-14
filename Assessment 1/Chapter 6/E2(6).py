# Initialize the array
a = [20, 23, 82, 40, 32, 15, 67, 52]

# Find the indices of even numbers
even = [i for i, num in enumerate(a) if num % 2 == 0]

# Sort the array
sorted = sorted(a)

# Slice elements from index 3 to the end of the array
slice3 = a[3:]

# Slice elements from index 0 to index 4 (not inclusive)
slice4 = a[:4]

# Print [32, 15, 67] using negative slicing
nega = a[-4:-1]  # [32, 15, 67]

# Printing the results
print("Indices of even numbers:", even)
print("Sorted array:", sorted)
print("Elements from index 3 to end:", slice3)
print("Elements from index 0 to 4:", slice4)
print("Elements [32, 15, 67] using negative slicing:", nega)
