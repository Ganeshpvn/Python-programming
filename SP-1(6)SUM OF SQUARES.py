def sum_of_squares(N):
    return N * (N + 1) * (2 * N + 1) // 6
N = int(input("Enter a positive integer: "))
print("Sum of squares of first", N, "natural numbers is:", sum_of_squares(N))