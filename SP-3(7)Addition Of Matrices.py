def add_matrices(mat1, mat2):
    # Get the number of rows and columns
    rows = len(mat1)
    cols = len(mat1[0])
    # Initialize the result matrix with zeroes
    result = [[0 for _ in range(cols)] for _ in range(rows)]
    # Add corresponding elements from both matrices
    for i in range(rows):
        for j in range(cols):
            result[i][j] = mat1[i][j] + mat2[i][j]
        return result
# Define the matrices
mat1 = [[1, 2], [5, 3]]
mat2 = [[2, 3], [4, 1]]
# Add the matrices
mat_sum = add_matrices(mat1, mat2)
# Print the result
print("Mat Sum = ")
for row in mat_sum:
    print(row)