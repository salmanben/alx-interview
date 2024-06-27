#!/usr/bin/python3
""" This module contains the island_perimeter solution """


def island_perimeter(grid):
    """ Returns the perimeter of the island. """

    if not grid or len(grid) == 0 or len(grid[0]) == 0:
        return 0

    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                perimeter += 4

                top = grid[row - 1][col]
                side = grid[row][col - 1]
                if row > 0 and top == 1:
                    perimeter -= 2

                if col > 0 and side == 1:
                    perimeter -= 2
    return perimeter
