# Matrix Transposition

# Given a 2D array of integers, matrix, your task is to return its transpose.
# Transposing a matrix involves flipping it along its main diagonal, which means swapping the matrix's row and column indices.

# For example:
# Example 1:
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[1,4,7],[2,5,8],[3,6,9]]

# Example 2:
# Input: matrix = [[1,2,3],[4,5,6]]
# Output: [[1,4],[2,5],[3,6]]

# In the above examples, matrix transposition involves transforming the original rows into columns in the resulting matrix. This task requires you to transform any given 2D integer array into its transposed form, where rows become columns and vice versa.

# Constraints
# matrix is a 2D array of integers
# dimensions of the matrix (m x n) where 1 <= m, n <= 100

## Step-by-Step Problem-Solving Guide:
# 1. **Identify the dimensions**: Determine the number of rows (m) and columns (n) in the input matrix.
# 2. **Create output matrix with swapped dimensions**: The transposed matrix will have n rows and m columns.
# 3. **Map elements correctly**: The element at position [i][j] in the original matrix goes to position [j][i] in the transposed matrix.
# 4. **Iterate through the matrix**: Visit each element of the original matrix and place it in its corresponding position in the new matrix.
# 5. **Handle non-square matrices**: Make sure your solution works for both square and rectangular matrices.
# 6. **Verify correctness**: Check that the first row of the original matrix becomes the first column of the transposed matrix, and so on.
# 7. **Consider edge cases**: What if the matrix has only one row or one column?
# 8. **Avoid in-place modifications**: Create a new matrix rather than trying to transpose in-place (which is complex for non-square matrices).
# 9. **Use appropriate data structures**: A 2D list (list of lists) is the natural choice for representing matrices in Python.
# 10. **Return the complete matrix**: Make sure to return the entire transposed matrix, not just individual elements.

# BruteForce Method

def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
    rows = len(matrix)
    cols = len(matrix[0])
    transposed = [[0] * rows for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]
    return transposed
