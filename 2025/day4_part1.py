"""
Advent of Code 2025 - Day 4 part i
"""
import sys
import numpy as np


def surrounding_rolls(grid: np.ndarray,
                      row_inds: list,
                      col_inds: list,
                      limit: int) -> int:
    """
    This function is only called if the current grid location
    has a roll of paper
    Hence, - 1
    """
    sub_grid = grid[row_inds[0]:row_inds[1], col_inds[0]:col_inds[1]] == '@'
    if (sum(sum(sub_grid)) - 1) < limit:
        return 1
    return 0


def define_range(index: int, ind_limit: int) -> list:
    if index == 0:
        prev_index = None
        next_index = index + 2
    elif index == ind_limit - 1:
        prev_index = index - 1
        next_index = None
    else:
        prev_index = index - 1
        next_index = index + 2
    return [prev_index, next_index]


def find_rolls(grid: np.ndarray, limit: int) -> int:
    height, width = grid.shape[0], grid.shape[1]
    access_rolls = 0
    for row in range(height):
        row_inds = define_range(row, height)
        for col in range(width):
            if grid[row, col] == '@':
                col_inds = define_range(col, width)
                access_rolls += (
                    surrounding_rolls(grid, row_inds, col_inds, limit))
            else:
                continue
    return access_rolls


if __name__ == '__main__':
    input_file = str(
        sys.argv[1]
        if len(sys.argv) > 1
        else FileNotFoundError("Input file not specified")
    )
    with open(input_file) as f:
        roll_grid = np.array([list(row.strip()) for row in f])
        limit = 4
        accessible_rolls = find_rolls(roll_grid, limit)
        print(f'Number of accessible rolls: {accessible_rolls}')
