#!/usr/bin/python3
"""
function returns perimeter of the island described in grid
"""


def island_perimeter(grid):
    """The grid is completely surrounded by water
    Args:
        grid ([int]): is a list of list of integers
    Returns:
        [int]: perimeter of the island described in grid
    """

    perimeter = 0
    l = len(grid)
    w = len(grid[0])

    for i in range(l):
        for j in range(w):
            if grid[i][j] == 1:
                for x, y in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    A, B = i + x, j + y
                    # display
                    if A >= l or B >= w or A < 0 or B < 0 or grid[A][B] == 0:
                        perimeter += 1

    return perimeter
