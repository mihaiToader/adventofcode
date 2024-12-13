import copy

from y2024.input_output import read_level_input


LEVEL = '11.0'


def get_input(level):
    input_data = read_level_input(level)

    return [int(x) for x in input_data[0].split(' ')]


def transform_stone(stone):
    if stone == 0:
        return [1]

    if len(str(stone)) % 2 == 0:
        new_stone = str(stone)
        return [int(new_stone[:len(new_stone) // 2]), int(new_stone[len(new_stone) // 2:])]

    return [stone * 2024]


def transform_stones(stones):
    transformed_stones = []
    for stone in stones:
        transformed_stones += transform_stone(stone)
    return transformed_stones


def solve():
    stones = get_input(LEVEL)
    blinks = 75
    for blink in range(blinks):
        stones = transform_stones(stones)
        print(stones)

    print(len(stones))


if __name__ == "__main__":
    solve()
