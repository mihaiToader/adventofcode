from y2024.input_output import read_level_input


LEVEL = '13.1'


def parse_button(button):
    return [int(b.split('+')[1]) for b in button.split(': ')[1].split(', ')]


def parse_prize(prize, multiplier):
    return [int(b.split('=')[1]) + multiplier for b in prize.split(': ')[1].split(', ')]


def parse_claw_machines(input_data, multiplier):
    machines = []
    line = 0
    while line < len(input_data):
        button_a = parse_button(input_data[line])
        button_b = parse_button(input_data[line + 1])
        prize = parse_prize(input_data[line + 2], multiplier)
        machines.append({
            'a': button_a,
            'b': button_b,
            'prize': prize
        })
        line += 4
    return machines


def get_input(level):
    return read_level_input(level)


def solve(level, multiplier):
    input_data = get_input(level)
    claw_machines = parse_claw_machines(input_data, multiplier)
    tokens = 0
    for machine in claw_machines:
        a = (machine['prize'][0] * machine['b'][1] - machine['b'][0] * machine['prize'][1]) / (machine['a'][0] * machine['b'][1] - machine['a'][1] * machine['b'][0])
        if not a.is_integer():
            continue

        b = (machine['prize'][1] - a * machine['a'][1]) / machine['b'][1]
        if not b.is_integer():
            continue

        tokens += a * 3 + b * 1

    print(int(tokens))


if __name__ == "__main__":
    solve(LEVEL, 0)
