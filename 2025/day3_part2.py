"""
Advent of Code 2025 - Day 3 part ii
"""
import sys


def find_max_joltage(bank: str, n_batteries: int) -> int:
    batteries = list(bank)
    if '\n' in batteries:
        batteries.remove('\n')
    jolts = []
    for number in range(1, n_batteries+1):
        if number == n_batteries:
            end_limit = len(batteries)
        else:
            end_limit = -n_batteries + number
        jolt = max(batteries[:end_limit])
        jolts.append(str(jolt))
        jolt_ind = batteries[:end_limit].index(jolt)
        batteries = batteries[jolt_ind+1:]
    return int(''.join(jolts))


if __name__ == '__main__':
    input_file = str(
        sys.argv[1]
        if len(sys.argv) > 1
        else FileNotFoundError("Input file not specified")
    )
    n_batteries = int(str(
        sys.argv[2]
        if len(sys.argv) > 2
        else FileNotFoundError("N batteries not specfied")
    ))
    with open(input_file) as f:
        bank_joltage = 0
        for bank in f:
            bank_joltage += find_max_joltage(bank, n_batteries)
    print(f'Total joltage = {bank_joltage}')
