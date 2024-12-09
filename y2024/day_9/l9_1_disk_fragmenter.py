from y2024.input_output import read_level_input


LEVEL = '9.1'


def get_input(level):
    input_data = read_level_input(level)

    return list(input_data[0])


def create_memory_map(disk_map):
    memory_map = []
    file_id = 0
    for i in range(len(disk_map)):
        memory_block = int(disk_map[i])
        is_file = i % 2 == 0
        for j in range(memory_block):
            if is_file:
                memory_map.append(file_id)
            else:
                memory_map.append('.')
        if is_file:
            file_id += 1

    return memory_map


def solve():
    disk_map = get_input(LEVEL)
    memory_map = create_memory_map(disk_map)

    for i in range(len(memory_map) - 1):
        if memory_map[i] != '.':
            continue

        for j in range(len(memory_map) - 1, i, -1):
            if memory_map[j] == '.':
                continue
            memory_map[i], memory_map[j] = memory_map[j], memory_map[i]
            break

    checksum = 0
    for i in range(len(memory_map)):
        if memory_map[i] == '.':
            continue
        checksum += i * memory_map[i]
    print(checksum)


if __name__ == "__main__":
    solve()
