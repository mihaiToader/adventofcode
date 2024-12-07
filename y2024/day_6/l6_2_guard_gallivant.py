import copy

from l6_1_guard_gallivant import get_input, find_guard_position, is_inside_of_map, print_lab_map, is_obstacle, turn_90_degrees


LEVEL = '6.1'
PATROL = LEVEL.split('.')[1]


def print_map(lab_map):
    with open(f'./output/patrol_{PATROL}.txt', 'w') as f:
        f.writelines('\n'.join(
            [''.join([''.join(item) if isinstance(item, list) else item for item in row]) for row in
             lab_map]))
        f.writelines('\n-\n')


def print_patrol(guard_patrol):
    with open(f'./output/patrol_{PATROL}.txt', 'a') as f:
        f.writelines(','.join(['|'.join([str(coor[0]), str(coor[1])]) for coor in guard_patrol]))
        f.writelines('\n-\n')


def print_loops(path, obstacle):
    path_with_obstacle_first = [obstacle, *path]
    with open(f'./output/patrol_{PATROL}.txt', 'a') as f:
        f.writelines(','.join(['|'.join([str(coor[0]), str(coor[1])]) for coor in path_with_obstacle_first]))
        f.writelines('\n')


def make_step(lab_map, position):
    row = position[0]
    col = position[1]
    guard = lab_map[row][col]

    new_position = None
    if guard == '^':
        new_position = [row - 1, col]
    if guard == '>':
        new_position = [row, col + 1]
    if guard == 'v':
        new_position = [row + 1, col]
    if guard == '<':
        new_position = [row, col - 1]

    if is_inside_of_map(lab_map, new_position) and is_obstacle(lab_map, new_position):
        return make_step(turn_90_degrees(lab_map, position), position)
    return new_position


def patrol(lab_map, position):
    new_position = make_step(lab_map, position)
    if not is_inside_of_map(lab_map, new_position):
        lab_map[position[0]][position[1]] = 'X'
        return [lab_map, new_position]

    row = new_position[0]
    col = new_position[1]

    lab_map[row][col] = lab_map[position[0]][position[1]]
    lab_map[position[0]][position[1]] = 'X'
    return [lab_map, new_position]


def generate_patrol(lab_map):
    guard_position = find_guard_position(lab_map)

    visited = [guard_position]
    while is_inside_of_map(lab_map, guard_position):
        [lab_map, guard_position] = patrol(lab_map, guard_position)
        visited.append(guard_position)

    print_patrol(visited)
    return lab_map


def visit_space_hash(lab_map, position):
    guard_orientation = lab_map[position[0]][position[1]]
    return f'{position[0]}-{position[1]}-{guard_orientation}'


def is_loop_for_obstacle(lab_map, starting_position, obstacle_position):
    guard_position = copy.deepcopy(starting_position)
    loop_map = copy.deepcopy(lab_map)
    loop_map[obstacle_position[0]][obstacle_position[1]] = '#'
    visited = set()
    visited.add(visit_space_hash(loop_map, guard_position))
    path = [guard_position]
    while True:
        [loop_map, guard_position] = patrol(loop_map, guard_position)
        path.append(guard_position)
        if not is_inside_of_map(loop_map, guard_position):
            return False

        visit = visit_space_hash(loop_map, guard_position)
        if visit in visited:
            print_loops(path, obstacle_position)
            return True

        visited.add(visit)


# 41
def solve():
    lab_map = get_input(LEVEL)
    print_map(lab_map)

    guard_position = find_guard_position(lab_map)

    walked_map = copy.deepcopy(lab_map)
    generate_patrol(walked_map)

    steps = 0
    loops = 0
    for i in range(0, len(walked_map)):
        for j in range(0, len(walked_map[0])):
            if walked_map[i][j] == 'X' and [i, j] != guard_position:
                if is_loop_for_obstacle(lab_map, guard_position, [i, j]):
                    loops += 1
                steps += 1

    print(loops)


if __name__ == "__main__":
    solve()
