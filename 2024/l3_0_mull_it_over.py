import re

from input_output import read_level_input

LEVEL = '3.1'


def get_input(level):
    return read_level_input(level)


def compute_mul(instruction):
    numbers = instruction.split('mul(')[1].split(')')[0].split(',')
    numbers = [int(nr) for nr in numbers]
    return numbers[0] * numbers[1]


# 34873487
def solve():
    instructions = get_input(LEVEL)
    regex = re.compile(r"mul\([0-9]{1,3},[0-9]{1,3}\)")
    res = 0

    for instruction in instructions:
        valid_instructions = regex.findall(instruction)

        for valid_instruction in valid_instructions:
            numbers = valid_instruction.split('mul(')[1].split(')')[0].split(',')
            numbers = [int(nr) for nr in numbers]
            res += numbers[0] * numbers[1]

    print(res)


if __name__ == "__main__":
    solve()
