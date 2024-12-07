import copy

from l6_1_guard_gallivant import get_input, find_guard_position, is_inside_of_map, print_lab_map

LEVEL = '6.1'


def last_from_lab_map_coord(lab_map, row, col) -> str:
    el = lab_map[row][col]
    return el[len(el) - 1]


def last_from_lab_map(lab_map, position) -> str:
    row = position[0]
    col = position[1]
    return last_from_lab_map_coord(lab_map, row, col)


def is_obstacle(lab_map, position):
    return last_from_lab_map(lab_map, position) in ['0', '#']


def go_straight(lab_map, position):
    row = position[0]
    col = position[1]
    guard = last_from_lab_map_coord(lab_map, row, col)
    if guard == '^':
        return [row - 1, col]
    if guard == '>':
        return [row, col + 1]
    if guard == 'v':
        return [row + 1, col]
    if guard == '<':
        return [row, col - 1]


def turn_90_degrees(lab_map, position):
    row = position[0]
    col = position[1]
    guard = last_from_lab_map_coord(lab_map, row, col)

    new_position = None
    if guard == '^':
        new_position = '>'
    elif guard == '>':
        new_position = 'v'
    elif guard == 'v':
        new_position = '<'
    elif guard == '<':
        new_position = '^'

    lab_map[row][col][len(lab_map[row][col]) - 1] = new_position
    return lab_map


def patrol(lab_map, position):
    new_position = go_straight(lab_map, position)
    if not is_inside_of_map(lab_map, new_position):
        return [lab_map, new_position, False, False]

    if is_obstacle(lab_map, new_position):
        return [turn_90_degrees(lab_map, position), position, True, False]

    row = new_position[0]
    col = new_position[1]

    if last_from_lab_map(lab_map, new_position) == '.':
        lab_map[row][col] = [last_from_lab_map(lab_map, position)]
    elif last_from_lab_map(lab_map, position) in lab_map[row][col]:
        return [lab_map, new_position, False, True]
    else:
        lab_map[row][col].append(last_from_lab_map(lab_map, position))

    return [lab_map, new_position, False, False]


def is_loop(lab_map, guard_position, obstacle_position):
    new_lab_map = copy.deepcopy(lab_map)
    new_lab_map[obstacle_position[0]][obstacle_position[1]] = ['0']
    new_lab_map = turn_90_degrees(new_lab_map, guard_position)

    while is_inside_of_map(new_lab_map, guard_position):
        [new_lab_map, guard_position, _, is_loop_here] = patrol(new_lab_map, guard_position)
        if is_loop_here:
            print_lab_map(new_lab_map)
            return True

        if not is_inside_of_map(new_lab_map, guard_position):
            return False

    return False


def make_lab_map_elements_lists(lab_map):
    return [[[el] for el in row] for row in lab_map]


#495 too low
#2094 too high
#5331 1812 the answer
def solve():
    lab_map = get_input(LEVEL)
    guard_position = find_guard_position(lab_map)

    lab_map = make_lab_map_elements_lists(lab_map)
    distinct_obstructions = 0
    while is_inside_of_map(lab_map, guard_position):
        if guard_position[0] % 10 == 0:
            print(guard_position)
        [lab_map, obstacle_position, rotate_guard, _] = patrol(lab_map, guard_position)
        if not is_inside_of_map(lab_map, obstacle_position):
            break

        if rotate_guard:
            continue

        if is_loop(lab_map, guard_position, obstacle_position):
            distinct_obstructions += 1
        guard_position = obstacle_position

    print(distinct_obstructions)


if __name__ == "__main__":
    solve()
