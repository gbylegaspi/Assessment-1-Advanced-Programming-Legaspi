# Looping through numbers from 1 to 100
for i in range(1, 101):
    # First, check if 'i' is a multiple of both 3 and 5
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")  # Print 'FizzBuzz' for multiples of both 3 and 5
    # If not, check if 'i' is a multiple of 3
    elif i % 3 == 0:
        print("Fizz")  # Print 'Fizz' for multiples of 3
    # If not, check if 'i' is a multiple of 5
    elif i % 5 == 0:
        print("Buzz")  # Print 'Buzz' for multiples of 5
    # If 'i' is not a multiple of 3 or 5, print the number itself
    else:
        print(i)
