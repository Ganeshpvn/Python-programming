def factorial(n):
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    # Recursive case: n! = n * (n-1)!
    else:
        return n * factorial(n-1)
# Get the number from the user
num = int(input("Enter a number: "))
# Calculate the factorial and print the result
# print("Factorial of", num, "is:", factorial(num))