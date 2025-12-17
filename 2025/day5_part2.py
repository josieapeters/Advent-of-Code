"""
Advent of Code 2025 - Day 5 part ii
"""
import sys
import intervaltree


def add_to_fresh_list_tuple(new_IDs: list) -> tuple:
    lower, upper = new_IDs
    return (lower, upper+1)


def count_fresh_IDs(fresh_IDs_tuple: list[tuple]) -> int:
    ID_tree = intervaltree.IntervalTree.from_tuples(fresh_IDs)
    ID_tree.merge_overlaps(strict=True)
    return sum([x.end - x.begin for x in ID_tree])


if __name__ == '__main__':
    input_file = str(
        sys.argv[1]
        if len(sys.argv) > 1
        else FileNotFoundError('Input file not specified')
    )
    with open(input_file) as f:
        fresh_IDs = []
        for line in f:
            if line == '\n':
                break
            else:
                IDs = [int(x) for x in line.split('-')]
                fresh_IDs.append(add_to_fresh_list_tuple(IDs))
    fresh_ingredient_IDs = count_fresh_IDs(fresh_IDs)
    print(f'Number of fresh ingredient IDs: {fresh_ingredient_IDs}')
