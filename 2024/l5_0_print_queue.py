from input_output import read_level_input


LEVEL = '5.1'


def get_input(level):
    input_data = read_level_input(level)
    rules = []
    updates = []
    for line in input_data:
        if not line:
            continue
        if '|' in line:
            rules.append([int(page) for page in line.split('|')])
            continue
        if ',' in line:
            updates.append([int(page) for page in line.split(',')])
    return dict(rules=rules, updates=updates)


def compute_rules_hash(rules: list[list[int]]):
    rules_hash = dict()
    for rule in rules:
        if not rules_hash.get(rule[0]):
            rules_hash[rule[0]] = [rule[1]]
        else:
            rules_hash[rule[0]].append(rule[1])
    return rules_hash


def is_valid_update(safety_manual, update):
    for i in range(1, len(update)):
        page_i = update[i]
        page_i_rules = safety_manual['rules_hash'].get(page_i)
        if not page_i_rules:
            continue

        for j in range(i + 1, len(update)):
            page_j = update[j]
            if page_j not in page_i_rules:
                return [False, i, j]

        for j in range(0, i):
            page_j = update[j]
            if page_j in page_i_rules:
                return [False, i, j]

    return [True, None, None]


def solve():
    safety_manual = get_input(LEVEL)
    safety_manual['rules_hash'] = compute_rules_hash(safety_manual.get('rules'))

    middle_sum = 0
    for update in safety_manual.get('updates'):
        [is_valid, _, _] = is_valid_update(safety_manual, update)
        if is_valid:
            middle_sum += update[len(update) // 2]

    print(middle_sum)


if __name__ == "__main__":
    solve()
