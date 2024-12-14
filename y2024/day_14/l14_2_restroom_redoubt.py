import os

from l14_1_restroom_redoubt import get_input, move_robots

LEVEL = '14.1'


def print_robots(wide, tall, robots, seconds):
    robots_map = [[' '] * wide for _ in range(tall)]
    for [p, v] in robots:
        [j, i] = p
        if robots_map[i][j] == ' ':
            robots_map[i][j] = 'W'

    with open(f'./map.txt', 'a') as f:
        f.writelines('\n'.join(
            [''.join([''.join(item) for item in row]) for row in robots_map]))
        f.writelines(str(seconds))
        f.writelines('\n-\n')



def is_bottom_line_full(wide, tall, robots):
    count = 0
    bottom_line = set()
    for [p, v] in robots:
        if p[1] == tall - 1:
            bottom_line.add(p[0])
    return len(bottom_line) == wide


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
        # print_robots_console(wide, tall, robots)
        print_robots(wide, tall, robots, seconds)
        if is_bottom_line_full(wide, tall, robots):
            print_robots(wide, tall, robots, seconds)
            print(seconds)
            break

        if seconds % 1000 == 0:
            print('aaaaa', seconds)


if __name__ == "__main__":
    solve()
