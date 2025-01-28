# Python Program to check whether given sudoku board is valid

# Checks for duplicates in the current row
def validRow(mat, row):

    # Visited array to track occurrences
    vis = [0] * 10
    
    for i in range(9):

        # If the cell is not empty
        if mat[row][i] != 0:
            val = mat[row][i]

            # If duplicate is found
            if vis[val] != 0:
                return False

            # Mark the number as visited
            vis[val] += 1
    return True

# Checks for duplicates in the current column
def colValid(mat, col):

    # Visited array to track occurrences
    vis = [0] * 10
    
    for i in range(9):

        # If the cell is not empty
        if mat[i][col] != 0:
            val = mat[i][col]

            # If duplicate is found
            if vis[val] != 0:
                return False

            # Mark the number as visited
            vis[val] += 1
    return True

# Checks for duplicates in the current 3x3 submatrix
def subMatValid(mat, startRow, startCol):

    # Visited array to track occurrences
    vis = [0] * 10
    
    for row in range(3):
        for col in range(3):

            # Current element in the submatrix
            curr = mat[row + startRow][col + startCol]

            # If the cell is not empty
            if curr != 0:

                # If duplicate is found
                if vis[curr] != 0:
                    return False

                # Mark the number as visited
                vis[curr] += 1
    return True

# Validates the Sudoku board
def isValid(mat):
    for i in range(9):
        for j in range(9):

            # Check if the row, column, or submatrix is invalid
            if not validRow(mat, i) or not colValid(mat, j) or \
               not subMatValid(mat, i - i % 3, j - j % 3):
                return False
    return True 

# Driver code
mat = [
    [9, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 5, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]
print("true" if isValid(mat) else "false")
