import copy

from y2024.input_output import read_level_input


LEVEL = '11.0'


def get_input(level):
    input_data = read_level_input(level)
    input_data = [list(line) for line in input_data]
    return [[int(x) for x in line] for line in input_data]


def solve():
    topographic_map = get_input(LEVEL)
    print(topographic_map)


if __name__ == "__main__":
    solve()
