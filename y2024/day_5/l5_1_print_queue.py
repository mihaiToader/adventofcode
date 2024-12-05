from l5_0_print_queue import get_input, compute_rules_hash, is_valid_update

LEVEL = '5.1'


def solve():
    safety_manual = get_input(LEVEL)
    safety_manual['rules_hash'] = compute_rules_hash(safety_manual.get('rules'))

    middle_sum = 0
    for update in safety_manual.get('updates'):
        [is_valid, bad_page_i, bad_page_j] = is_valid_update(safety_manual, update)
        if is_valid:
            continue

        new_update = update[:]
        while True:
            new_update[bad_page_j], new_update[bad_page_i] = new_update[bad_page_i], new_update[bad_page_j]
            [is_valid, bad_page_i, bad_page_j] = is_valid_update(safety_manual, new_update)
            if is_valid:
                middle_sum += new_update[len(new_update) // 2]
                break

    print(middle_sum)


if __name__ == "__main__":
    solve()
