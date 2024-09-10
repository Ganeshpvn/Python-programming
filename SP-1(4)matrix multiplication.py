def matrix_multiplication(A, B):
    # Get the dimensions of the matrices
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])
    # Check if the matrices can be multiplied
    if cols_A != rows_B:
        return "Matrices cannot be multiplied"
    # Create a result matrix filled with zeros
    C = [[0 for _ in range(cols_B)] for _ in range(rows_A)]
    # Perform matrix multiplication
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):  # or 'range(rows_B)'
                C[i][j] += A[i][k] * B[k][j]
    return C
# Get the matrices as input
A = [[2, 1], [3, 4]]
B = [[3, 1], [1, 2]]
# Perform matrix multiplication and print the result
print("Matrix A:", A)
print("Matrix B:", B)
print("Matrix C (A * B):", matrix_multiplication(A, B))