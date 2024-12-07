from y2024.input_output import read_level_input


LEVEL = '8.0'


def get_input(level):
    input_data = read_level_input(level)

    return input_data


def solve():
    input_data = get_input(LEVEL)
    print(input_data)


if __name__ == "__main__":
    solve()
