from Sudoku_Solver import draw_sudoku

# Define a string representing a Sudoku puzzle, where 0s represent empty cells
sudoku_string = "3 0 9 0 5 0 0 2 0 0 0 6 0 0 0 0 1 0 4 5 2 0 0 0 6 8 3 0 0 4 0 0 0 0 0 2 0 0 1 0 7 4 5 0 0 8 0 5 1 0 9 7 6 0 5 0 3 2 9 6 8 0 0 6 0 0 0 8 1 3 0 0 0 9 8 0 4 0 0 0 6"

# Split the string into individual numbers and convert them to integers
sudoku_list = list(map(int, sudoku_string.split()))

# Group the numbers into sublists of 9 elements each to form a 2D list representing the Sudoku grid
sudoku = [sudoku_list[i : i + 9] for i in range(0, len(sudoku_list), 9)]

# Draw the initial state of the Sudoku puzzle
draw_sudoku(sudoku)

# Define the coordinates of an empty cell in the Sudoku grid
row = 8
col = 3

# Calculate the starting coordinates of the 3x3 box that the empty cell belongs to
row_start = (row // 3) * 3
col_start = (col // 3) * 3

# Print the coordinates of the empty cell and its 3x3 box
print(
    f"Empty cell {row + 1}, {col + 1} is in row-start = {row_start + 1}, col_start = {col_start + 1}"
)

# Loop over all possible numbers that can be filled in the empty cell
for guess in range(1, 10):

    # Loop over all cells in the 3x3 box
    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):

            # If the current number already exists in the 3x3 box, calculate the starting coordinates of the box
            if sudoku[r][c] == guess:
                r_start = r // 3
