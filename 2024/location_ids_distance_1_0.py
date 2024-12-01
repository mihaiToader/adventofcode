from input_output import read_level_input


LEVEL = '1.1'


def get_input(level):
    input_data = read_level_input(level)
    data = [[], []]
    for line in input_data:
        [loc_id_1, loc_id_2] = list(filter(lambda el: len(el) > 0, line.split(' ')))
        data[0].append(int(loc_id_1))
        data[1].append(int(loc_id_2))
    return data


def sort_lists(input_data: list):
    return [
        list(sorted(input_data[0])),
        list(sorted(input_data[1])),
    ]


def solve():
    input_data = get_input(LEVEL)
    input_data = sort_lists(input_data)
    distance = 0
    for index in range(len(input_data[0])):
        distance += abs(input_data[0][index] - input_data[1][index])
    print(distance)


if __name__ == "__main__":
    solve()
