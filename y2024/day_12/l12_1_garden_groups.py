from y2024.input_output import read_level_input


LEVEL = '12.1'


def is_in_garden(garden, x, y):
    return 0 <= x < len(garden) and 0 <= y < len(garden[0])


def get_input(level):
    input_data = read_level_input(level)
    return [list(line) for line in input_data]


DIRECTIONS = [[-1, 0], [0, 1], [1, 0], [0, -1]]


def measure_crops(garden, row, column):
    area = 0
    perimeter = 0
    plant = garden[row][column]
    stack = [[row, column]]
    visited = plant + '-'
    while len(stack) > 0:
        [r, c] = stack.pop()

        if not is_in_garden(garden, r, c):
            perimeter += 1
            continue

        if garden[r][c] == visited:
            continue

        if garden[r][c] != plant:
            perimeter += 1
            continue

        area += 1
        garden[r][c] = visited
        for [row_direction, column_direction] in DIRECTIONS:
            stack.append([r + row_direction, c + column_direction])

    return [area, perimeter]


def solve():
    garden = get_input(LEVEL)

    fence_price = 0
    for row in range(len(garden)):
        for column in range(len(garden[0])):
            if '-' not in garden[row][column]:
                [crop_area, crop_perimeter] = measure_crops(garden, row, column)
                fence_price += crop_area * crop_perimeter

    print(fence_price)


if __name__ == "__main__":
    solve()
