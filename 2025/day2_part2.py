"""
Advent of Code 2025 - Day 2 part ii
"""

import sys
import csv


def find_fake_ids(id_range: str) -> list[int]:
    lower, upper = [int(x) for x in id_range.split('-')]
    fake_ids = []
    for id in range(lower, upper+1):
        id_length = int(len(str(id)))
        for rep_length in range(1, int(id_length/2)+1):
            if str(id) == (str(id)[0:rep_length] * int(id_length/rep_length)):
                fake_ids.append(id)
    return fake_ids


if __name__ == '__main__':
    input_file = str(
        sys.argv[1]
        if len(sys.argv) > 1
        else FileNotFoundError("Input file not specified")
    )
    with open(input_file) as f:
        reader = csv.reader(f)
        for row in reader:
            ranges = row
        fake_ids = []
        for id_range in ranges:
            temp_ids = list(set(find_fake_ids(id_range)))
            for x in temp_ids:
                fake_ids.append(x)
        print(f'Total sum of invalid IDs is: {sum(fake_ids)}')
