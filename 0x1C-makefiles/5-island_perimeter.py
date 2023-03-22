#!/usr/bin/python3
"""5-island_perimeter module"""

def island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid.
    
    Args:
        grid (list of list of int): A list of lists representing the grid.
                                   0 represents a water zone.
                                   1 represents a land zone.
    
    Returns:
        int: The perimeter of the island in the grid.
    """
    perimeter = 0
    grid_height = len(grid) - 1
    grid_width = len(grid[0]) - 1

    for row_idx, row in enumerate(grid):
        for col_idx, cell in enumerate(row):
            if cell == 1:
                if row_idx == 0 or grid[row_idx - 1][col_idx] != 1:
                    perimeter += 1
                if col_idx == 0 or grid[row_idx][col_idx - 1] != 1:
                    perimeter += 1
                if col_idx == grid_width or grid[row_idx][col_idx + 1] != 1:
                    perimeter += 1
                if row_idx == grid_height or grid[row_idx + 1][col_idx] != 1:
                    perimeter += 1
    return perimeter
