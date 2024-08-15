import matplotlib.pyplot as plt
import numpy as np


def draw_sudoku(grid):
    fig, ax = plt.subplots()
    ax.axis("tight")
    ax.axis("off")
    table = ax.table(
        cellText=grid,
        cellLoc="center",
        loc="center",
        cellColours=[["w"] * 9] * 9,
        bbox=[0, 0, 1, 1],
    )
    table.scale(1, 1.5)

    plt.show()


# Example usage:
sudoku_grid = [
    [1, 0, 0, 0, 0, 7, 0, 9, 0],
    [0, 3, 0, 0, 2, 0, 0, 0, 8],
    [0, 0, 9, 6, 0, 0, 5, 0, 0],
    [0, 0, 5, 3, 0, 0, 9, 0, 0],
    [0, 1, 0, 0, 8, 0, 0, 0, 2],
    [6, 0, 0, 0, 0, 4, 0, 0, 0],
    [3, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 4, 0, 0, 0, 0, 0, 0, 7],
    [0, 0, 7, 0, 0, 0, 3, 0, 0],
]

draw_sudoku(sudoku_grid)
