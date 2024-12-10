import copy

from y2024.input_output import read_level_input


LEVEL = '10.0'


def is_in_map(the_map, x, y):
    return 0 <= x < len(the_map) and 0 <= y < len(the_map[0])

def get_input(level):
    input_data = read_level_input(level)
    input_data = [list(line) for line in input_data]
    return [[int(x) for x in line] for line in input_data]


DIRECTIONS = [[-1, 0], [0, 1], [1, 0], [0, -1]]


def walk(topographic_map, col, row, use_visited):
    stack = [[col, row]]
    hilltops = []
    visited = copy.deepcopy(topographic_map)
    visited[col][row] = 'v'
    while len(stack) > 0:
        [x, y] = stack.pop()
        for direction in DIRECTIONS:
            new_x = x + direction[0]
            new_y = y + direction[1]
            if is_in_map(topographic_map, new_x, new_y) and topographic_map[new_x][new_y] == topographic_map[x][y] + 1:
                if use_visited and visited[new_x][new_y] == 'v':
                    continue
                if topographic_map[new_x][new_y] == 9:
                    hilltops.append([new_x, new_y])
                if use_visited:
                    visited[new_x][new_y] = 'v'
                stack.append([new_x, new_y])
    return hilltops

def solve(use_visited, level):
    topographic_map  = get_input(level)
    scores = 0
    for i in range(len(topographic_map)):
        for j in range(len(topographic_map[0])):
            if topographic_map[i][j] == 0:
                hilltops = walk(topographic_map, i, j, use_visited)
                scores += len(hilltops)

    print(scores)

if __name__ == "__main__":
    solve(True, LEVEL)
