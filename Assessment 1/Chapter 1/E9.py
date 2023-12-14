# 1. Create an int list with 10 values
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 2. Output the list using a for loop
print("main list:")
for item in list1:
    print(item, end=" ")
print()  # New line after printing the list

# 3. Output the highest and lowest int
print("highest int:", max(list1))
print("lowest int:", min(list1))

# 4. Sort the elements in ascending order
list1.sort()
print("ascending order:", list1)

# 5. Sort the elements in descending order
list1.sort(reverse=True)
print("descending order:", list1)

# 6. Append two elements
list1.append(0)
list1.append(-1)
print("appending two elements:", list1)
