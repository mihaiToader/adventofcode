from l8_1_resonant_collinearity import find_directions, solve, is_in_map

LEVEL = '8.1'


def set_antinodes_on_direction(antinodes_map, antenna_coord, direction, diff):
    new_x = antenna_coord[0] + (direction[0] * diff[0])
    new_y = antenna_coord[1] + (direction[1] * diff[1])
    is_outside_of_map = True
    if is_in_map(antinodes_map, new_x, new_y):
        antinodes_map[new_x][new_y] = '#'
        is_outside_of_map = False

    return [new_x, new_y, is_outside_of_map]


def set_antinodes_continuously(antinodes_map, antenna_coords, direction, diff):
    new_coords = [antenna_coords[0], antenna_coords[1]]
    while True:
        [new_x, new_y, is_outside_of_map] = set_antinodes_on_direction(antinodes_map, new_coords, direction, diff)
        if is_outside_of_map:
            break
        new_coords = [new_x, new_y]


def set_antinodes_for_antenna_pair(antinodes_map, first_antenna, second_antenna):
    new_x_diff = abs(first_antenna[0] - second_antenna[0])
    new_y_diff = abs(first_antenna[1] - second_antenna[1])

    directions = find_directions(first_antenna, second_antenna)

    set_antinodes_continuously(antinodes_map, first_antenna, directions[0], [new_x_diff, new_y_diff])
    set_antinodes_continuously(antinodes_map, second_antenna, directions[1], [new_x_diff, new_y_diff])


def count_antinodes(antennas_map, antinodes_map):
    antinodes = 0
    for i in range(len(antinodes_map)):
        for j in range(len(antinodes_map[0])):
            if antinodes_map[i][j] == '#' or antennas_map[i][j] != '.':
                antinodes += 1
    return antinodes


if __name__ == "__main__":
    [antennas_map, antinodes_map] = solve(LEVEL, set_antinodes_for_antenna_pair)
    print(count_antinodes(antennas_map, antinodes_map))
