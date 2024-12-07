from y2024.input_output import read_level_input


LEVEL = '6.1'


def get_input(level):
    input_data = read_level_input(level)
    return [list(line) for line in input_data]


def print_lab_map(lab_map):
    with open('map.txt', 'a') as f:
        f.writelines('\n'.join([''.join(['{:5}'.format(''.join(item)) if isinstance(item, list) else item for item in row]) for row in lab_map]))
        f.writelines('\n\n')


def find_guard_position(lab_map):
    for i in range(len(lab_map)):
        for j in range(len(lab_map[0])):
            if lab_map[i][j] == '^':
                return [i, j]
    return None


def go_straight(lab_map, position):
    row = position[0]
    col = position[1]
    guard = lab_map[row][col]

    if guard == '^':
        return [row - 1, col]
    if guard == '>':
        return [row, col + 1]
    if guard == 'v':
        return [row + 1, col]
    if guard == '<':
        return [row, col - 1]


def is_inside_of_map(lab_map, position):
    row = position[0]
    col = position[1]
    return 0 <= row < len(lab_map) and 0 <= col < len(lab_map[0])


def is_obstacle(lab_map, position):
    row = position[0]
    col = position[1]
    return lab_map[row][col] == '#'


def turn_90_degrees(lab_map, position):
    row = position[0]
    col = position[1]
    guard = lab_map[row][col]
    if guard == '^':
        lab_map[row][col] = '>'
    elif guard == '>':
        lab_map[row][col] = 'v'
    elif guard == 'v':
        lab_map[row][col] = '<'
    elif guard == '<':
        lab_map[row][col] = '^'
    return lab_map


def patrol(lab_map, position, distinct_steps):
    new_position = go_straight(lab_map, position)
    if not is_inside_of_map(lab_map, new_position):
        return [lab_map, new_position, distinct_steps + 1]

    if is_obstacle(lab_map, new_position):
        return [turn_90_degrees(lab_map, position), position, distinct_steps]

    row = new_position[0]
    col = new_position[1]

    new_distinct = distinct_steps
    if lab_map[row][col] != 'X':
        new_distinct = distinct_steps + 1

    lab_map[row][col] = lab_map[position[0]][position[1]]
    lab_map[position[0]][position[1]] = 'X'
    return [lab_map, new_position, new_distinct]


def solve():
    lab_map = get_input(LEVEL)
    guard_position = find_guard_position(lab_map)
    distinct_steps = 0
    while is_inside_of_map(lab_map, guard_position):
        # print_lab_map(lab_map)
        [lab_map, guard_position, distinct_steps] = patrol(lab_map, guard_position, distinct_steps)
    print(distinct_steps)


if __name__ == "__main__":
    solve()
