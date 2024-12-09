from l9_1_disk_fragmenter import get_input, create_memory_map

LEVEL = '9.1'


def solve():
    disk_map = get_input(LEVEL)
    memory_map = create_memory_map(disk_map)

    k = len(memory_map) - 1
    while k >= 0:
        if memory_map[k] == '.':
            k -= 1
            continue

        start_of_file = k
        j = k-1
        while j >= 0:
            if memory_map[j] != memory_map[k]:
                start_of_file = j
                break
            j -= 1

        if j == -1:
            start_of_file = j

        file_size = k - start_of_file

        i = 0
        while i <= k:
            if memory_map[i] != '.':
                i += 1
                continue

            end_of_free_space = i
            j = i + 1
            while j < len(memory_map):
                if memory_map[j] != '.':
                    end_of_free_space = j
                    break
                j += 1
            if j == len(memory_map):
                end_of_free_space = j

            free_space_size = end_of_free_space - i

            if free_space_size >= file_size:
                i2 = i
                k2 = k
                while k2 > start_of_file:
                    memory_map[i2], memory_map[k2] = memory_map[k2], memory_map[i2]
                    i2 += 1
                    k2 -= 1
                break

            i += free_space_size
        k -= file_size


    checksum = 0
    for i in range(len(memory_map)):
        if memory_map[i] == '.':
            continue
        checksum += i * memory_map[i]
    print(checksum)


if __name__ == "__main__":
    solve()
