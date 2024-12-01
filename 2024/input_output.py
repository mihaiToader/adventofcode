import os


def get_input_file(level: str) -> str:
    current_dir = os.path.dirname(os.path.realpath(__file__))
    input_dir = os.path.join(current_dir, 'input')
    return os.path.join(input_dir, f'{level}.txt')


def read_level_input(level: str) -> list[str]:
    filename = get_input_file(level)
    with open(filename) as f:
        data = f.read()
        return data.split('\n')


def get_output_file(level: str) -> str:
    current_dir = os.path.dirname(os.path.realpath(__file__))
    output_dir = os.path.join(current_dir, 'output')
    return os.path.join(output_dir, f'{level}.txt')


def write_level_output(level: str, data: list[str]):
    filename = get_output_file(level)
    data_new_line = list(map(lambda line: f'{line}\n', data))
    with open(filename, 'w') as f:
        f.writelines(data_new_line)
