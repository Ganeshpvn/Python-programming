def find_greatest(a, b, c):
    if a >= b and a >= c:
        print(a, "is the greatest.")
    elif b >= a and b >= c:
        print(b, "is the greatest.")
    else:
        print(c, "is the greatest.")
# Get the three numbers from the user
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
# Call the function to find the greatest number
find_greatest(a, b, c)