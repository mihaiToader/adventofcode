from y2024.input_output import read_level_input


LEVEL = '8.1'


def print_antennas_map(antenna_map):
    with open('map.txt', 'a') as f:
        f.writelines('\n'.join([''.join([''.join(item) if isinstance(item, list) else item for item in row]) for row in antenna_map]))
        f.writelines('\n\n')


def get_input(level):
    input_data = read_level_input(level)

    return [list(line) for line in input_data]


def find_similar_antennas_cords(antennas_map, x, y):
    coords = []
    for i in range(len(antennas_map)):
        for j in range(len(antennas_map[0])):
            if [i, j] == [x, y]:
                continue
            if antennas_map[x][y] == antennas_map[i][j]:
                coords.append([i, j])

    return coords


def is_in_map(the_map, x, y):
    return 0 <= x < len(the_map) and 0 <= y < len(the_map[0])


def find_directions(first_antenna, second_antenna):
    if first_antenna[0] == second_antenna[0]:
        return [[0, -1], [0, 1]]
    if first_antenna[1] == second_antenna[1]:
        return [[-1, 0], [1, 0]]
    if first_antenna[0] < second_antenna[0] and first_antenna[1] > second_antenna[1]:
        return [[-1, 1], [1, -1]]
    if first_antenna[0] < second_antenna[0] and first_antenna[1] < second_antenna[1]:
        return [[-1, -1], [1, 1]]


def set_antinodes_on_direction(antinodes_map, antenna_coord, direction, diff):
    new_x = antenna_coord[0] + (direction[0] * diff[0])
    new_y = antenna_coord[1] + (direction[1] * diff[1])

    if is_in_map(antinodes_map, new_x, new_y):
        antinodes_map[new_x][new_y] = '#'


def set_antinodes_for_antenna_pair(antinodes_map, first_antenna, second_antenna):
    new_x_diff = abs(first_antenna[0] - second_antenna[0])
    new_y_diff = abs(first_antenna[1] - second_antenna[1])

    directions = find_directions(first_antenna, second_antenna)
    set_antinodes_on_direction(antinodes_map, first_antenna, directions[0], [new_x_diff, new_y_diff])
    set_antinodes_on_direction(antinodes_map, second_antenna, directions[1], [new_x_diff, new_y_diff])


def set_antinodes(antinodes_map, antinodes_coords, set_antinodes_for_antenna_pair_func):
    for i in range(len(antinodes_coords) - 1):
        first_antenna = antinodes_coords[i]
        for j in range(i + 1, len(antinodes_coords)):
            second_antenna = antinodes_coords[j]
            set_antinodes_for_antenna_pair_func(antinodes_map, first_antenna, second_antenna)


def count_antinodes(antinodes_map):
    antinodes = 0
    for i in range(len(antinodes_map)):
        for j in range(len(antinodes_map[0])):
            if antinodes_map[i][j] == '#':
                antinodes += 1
    return antinodes


def solve(level, set_antinodes_for_antenna_pair_func):
    antennas_map = get_input(level)
    antinodes_map = [['.' for _ in range(len(antennas_map[0]))] for _ in range(len(antennas_map))]

    visited_antennas = set()
    for i in range(len(antennas_map)):
        for j in range(len(antennas_map[0])):
            if antennas_map[i][j] == '.':
                continue
            if antennas_map[i][j] in visited_antennas:
                continue

            similar_antennas_cords = [[i, j]] + find_similar_antennas_cords(antennas_map, i, j)
            set_antinodes(antinodes_map, similar_antennas_cords, set_antinodes_for_antenna_pair_func)
            visited_antennas.add(antennas_map[i][j])

    return [antennas_map, antinodes_map]


if __name__ == "__main__":
    [antennas_map, antinodes_map] = solve(LEVEL, set_antinodes_for_antenna_pair)
    print(count_antinodes(antinodes_map))
