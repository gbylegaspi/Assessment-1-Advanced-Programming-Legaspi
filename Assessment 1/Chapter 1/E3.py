a = float(input("Enter the length of the first side: "))
b = float(input("Enter the length of the second side: "))
c = float(input("Enter the length of the third side: "))

if a + b > c and a + c > b and b + c > a:
    print("A triangle can be formed.")
else:
    print("A triangle cannot be formed.")