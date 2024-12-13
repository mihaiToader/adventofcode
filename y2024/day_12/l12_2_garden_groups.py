from l12_1_garden_groups import get_input, DIRECTIONS, is_in_garden

LEVEL = '12.0'


def compute_sides(outside_cords):
    sides = 1
    [r, c] = outside_cords[0]
    for i in range(1, len(outside_cords)):
        [row, col] = outside_cords[i]

        if [r, c] == [row, col]:
            [r, c] = [row, col]
            sides += 1
            continue

        if r == row and (c == col - 1 or c == col + 1):
            [r, c] = [row, col]
            continue

        if c == col and (r == row - 1 or r == row + 1):
            [r, c] = [row, col]
            continue

        sides += 1
        [r, c] = [row, col]

    return sides


def measure_crops(garden, row, column):
    area = 0
    perimeter = 0
    plant = garden[row][column]
    stack = [[row, column]]
    visited = plant + '-'
    outside_coords = []
    while len(stack) > 0:
        [r, c] = stack.pop()

        if not is_in_garden(garden, r, c):
            perimeter += 1
            outside_coords.append([r, c, perimeter])
            continue

        if garden[r][c] == visited:
            continue

        if garden[r][c] != plant:
            perimeter += 1
            outside_coords.append([r, c, perimeter])
            continue

        area += 1
        garden[r][c] = visited
        for [row_direction, column_direction] in DIRECTIONS:
            stack.append([r + row_direction, c + column_direction])

    print(plant)
    print(outside_coords)
    sides = compute_sides(outside_coords)
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
