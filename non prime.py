def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def print_non_primes(A, B):
    for num in range(A + 1, B + 1):
        if not is_prime(num):
            print(num, end=" ")

# Get the range from the user
A = int(input("Enter A: "))
B = int(input("Enter B: "))

# Print non-prime numbers in the range
print_non_primes(A, B)
