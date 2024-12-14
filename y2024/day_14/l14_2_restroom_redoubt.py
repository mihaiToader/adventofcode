import os

from l14_1_restroom_redoubt import get_input, move_robots

LEVEL = '14.1'


def print_robots(wide, tall, robots, seconds):
    robots_map = [[' '] * wide for _ in range(tall)]
    for [p, v] in robots:
        [j, i] = p
        if robots_map[i][j] == ' ':
            robots_map[i][j] = 'W'

    with open(f'./tree.txt', 'w') as f:
        f.writelines('\n'.join(
            [''.join([''.join(item) for item in row]) for row in robots_map]))
        f.writelines(str(seconds))
        f.writelines('\n-\n')


def are_robots_on_unique_position(robots):
    for i in range(len(robots) - 1):
        for j in range(i + 1, len(robots)):
            if robots[i][0] == robots[j][0]:
                return False
    return True


def solve():
    robots = get_input(LEVEL)
    # wide = 11
    # tall = 7
    # seconds = 6

    wide = 101
    tall = 103
    seconds = 0
    while True:
        move_robots(wide, tall, robots)
        seconds += 1

        if are_robots_on_unique_position(robots):
            print_robots(wide, tall, robots, seconds)
            print(seconds)
            break

        if seconds % 1000 == 0:
            print('aaaaa', seconds)


if __name__ == "__main__":
    solve()
