"""
Advent of Code 2025 - Day 3 part i
"""
import sys


def find_max_joltage(bank: str) -> int:
    batteries = list(bank)
    first_battery = str(max(batteries[:-2]))
    second_battery = str(max(batteries[batteries.index(first_battery)+1:]))
    return int(first_battery+second_battery)


if __name__ == '__main__':
    input_file = str(
        sys.argv[1]
        if len(sys.argv) > 1
        else FileNotFoundError("Input file not specified")
    )
    with open(input_file) as f:
        bank_joltage = 0
        for bank in f:
            bank_joltage += find_max_joltage(bank)
    print(f'Total joltage = {bank_joltage}')
