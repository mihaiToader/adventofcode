from l12_1_garden_groups import get_input, DIRECTIONS, is_in_garden

LEVEL = '12.0'


def compute_sides(garden, visited, corners):
    return 1


def measure_crops(garden, row, column):
    area = 0
    plant = garden[row][column]
    stack = [[row, column]]
    visited = plant + '-'
    corners = dict(
        min_row=row,
        max_row=row,
        min_column=column,
        max_column=column,
    )
    while len(stack) > 0:
        [r, c] = stack.pop()

        if not is_in_garden(garden, r, c):
            continue

        if garden[r][c] == visited:
            continue

        if garden[r][c] != plant:
            continue

        area += 1
        garden[r][c] = visited
        corners['min_row'] = min(corners['min_row'], r)
        corners['max_row'] = max(corners['max_row'], r)
        corners['min_column'] = min(corners['min_column'], c)
        corners['max_column'] = max(corners['max_column'], c)
        for [row_direction, column_direction] in DIRECTIONS:
            stack.append([r + row_direction, c + column_direction])

    print(corners)
    sides = compute_sides(garden, visited, corners)
    return [area, sides]


def solve():
    garden = get_input(LEVEL)
    fence_price = 0
    for row in range(len(garden)):
        for column in range(len(garden[0])):
            if '-' not in garden[row][column]:
                print(garden[row][column])
                [crop_area, crop_sides] = measure_crops(garden, row, column)
                print(crop_sides)
                print()
                fence_price += crop_area * crop_sides

    print(fence_price)


if __name__ == "__main__":
    solve()
