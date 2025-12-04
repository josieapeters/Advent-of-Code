"""
Advent of Code 2025 - Day 1 part i
"""

import sys


def new_dial_pos(old_pos: int, rotation: str) -> int:
    # Modulo 100 to remove any full rotations
    change = int(rotation[1:]) % 100
    if rotation[0] == 'L':
        change *= -1
    new_pos = old_pos + change
    # Subtracting and adding 1 to account for the fact that 0 is a position
    if new_pos > 99:
        return (new_pos % 99) - 1
    elif new_pos < 0:
        return 99 + 1 + new_pos
    else:
        return new_pos


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
            current_pos = new_dial_pos(current_pos, line)
            if current_pos == 0:
                counter += 1
        print(f'Password is {counter}')
