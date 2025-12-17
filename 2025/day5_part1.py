"""
Advent of Code 2025 - Day 5 part i
"""
import sys


def add_to_fresh_list(new_IDs: list) -> range:
    lower, upper = new_IDs
    return range(lower, upper+1)


def is_it_fresh(ID: int, fresh_IDs: list) -> int:
    for fresh_ID in fresh_IDs:
        if ID in fresh_ID:
            return 1
    return 0


if __name__ == '__main__':
    input_file = str(
        sys.argv[1]
        if len(sys.argv) > 1
        else FileNotFoundError('Input file not specified')
    )
    with open(input_file) as f:
        fresh_IDs = []
        fresh_ingredients = 0
        for line in f:
            IDs = [int(x) for x in line.split('-') if x != '\n']
            if len(IDs) > 1:
                fresh_IDs.append(add_to_fresh_list(IDs))
            elif line == '\n':
                continue
            else:
                fresh_ingredients += is_it_fresh(IDs[0], fresh_IDs)
    print(f'Number of fresh ingredients: {fresh_ingredients}')
