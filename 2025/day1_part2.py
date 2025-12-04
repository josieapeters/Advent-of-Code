"""
Advent of Code 2025 - Day 1 part ii
"""

import sys
from day1_part1 import new_dial_pos


def passing_zeros(old_pos: int, new_pos: int, rotation: str) -> int:
    zero_counts = 0
    spins = int(rotation[1:])
    zero_counts += int(spins/100)
    if new_pos != 0 and old_pos != 0:
        if (
            (rotation[0] == 'R' and old_pos > new_pos)
            or (rotation[0] == 'L' and old_pos < new_pos)
        ):
            zero_counts += 1
    return zero_counts


if __name__ == '__main__':
    input_file = str(
        sys.argv[1]
        if len(sys.argv) > 1
        else FileNotFoundError("Input file not specified")
    )
    with open(input_file) as f:
        current_pos = 50
        counter = 0
        for line in f.readlines():
            old_pos = current_pos
            current_pos = new_dial_pos(current_pos, line)
            if current_pos == 0:
                counter += 1
            counter += passing_zeros(old_pos, current_pos, line)
        print(f'Password is {counter}')
