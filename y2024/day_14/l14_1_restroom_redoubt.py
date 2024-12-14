from y2024.input_output import read_level_input

LEVEL = '14.1'


def get_input(level):
    input_data = read_level_input(level)
    res = []
    for line in input_data:
        [p, v] = line.split(' ')
        p = p.split('=')[1]
        p = p.split(',')
        p = [int(p[0]), int(p[1])]

        v = v.split('=')[1]
        v = v.split(',')
        v = [int(v[0]), int(v[1])]
        res.append([p, v])
    return res


def move_robots(wide, tall, robots):
    for [p, v] in robots:
        p[0] += v[0]
        p[1] += v[1]

        if p[0] < 0:
            p[0] = abs(wide + p[0])
        if p[0] >= wide:
            p[0] = abs(p[0] - wide)

        if p[1] < 0:
            p[1] = abs(tall + p[1])
        if p[1] >= tall:
            p[1] = abs(p[1] - tall)


def get_quadrants(wide, tall):
    return [
        [[0, 0], [wide // 2, tall // 2]],
        [[wide // 2 + 1, 0], [wide, tall // 2]],
        [[0, tall // 2 + 1], [wide // 2, tall]],
        [[wide // 2 + 1, tall // 2 + 1], [wide, tall]],
    ]


def count_quadrants_robots(wide, tall, robots):
    quadrants = get_quadrants(wide, tall)

    quadrants_robots = [0, 0, 0, 0]
    for x in range(len(quadrants)):
        limits = quadrants[x]
        count = 0
        for i in range(limits[0][0], limits[1][0]):
            for j in range(limits[0][1], limits[1][1]):
                for [p, v] in robots:
                    if p[0] == i and p[1] == j:
                        count += 1

        quadrants_robots[x] = count
    return quadrants_robots


def solve():
    robots = get_input(LEVEL)
    # wide = 11
    # tall = 7

    wide = 101
    tall = 103
    seconds = 100
    for i in range(seconds):
        move_robots(wide, tall, robots)

    quadrants_robots = count_quadrants_robots(wide, tall, robots)
    safety_factor = 1
    for robots in quadrants_robots:
        safety_factor *= robots

    print(safety_factor)


if __name__ == "__main__":
    solve()
