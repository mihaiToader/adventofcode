import re

from input_output import read_level_input
from l3_0_mull_it_over import compute_mul

LEVEL = '3.1'


def get_input(level):
    return read_level_input(level)


# 107468007
def solve():
    instructions = get_input(LEVEL)
    regex = re.compile(r"(mul\([0-9]{1,3},[0-9]{1,3}\))|(don't\(\))|(do\(\))")
    res = 0
    is_mul_enabled = True

    for instruction in instructions:
        valid_instructions = regex.findall(instruction)
        for valid_instruction in valid_instructions:
            mul, dont, do = valid_instruction
            if dont and is_mul_enabled:
                is_mul_enabled = False
                continue

            if do and not is_mul_enabled:
                is_mul_enabled = True

            if not is_mul_enabled:
                continue

            if mul:
                res += compute_mul(mul)

    print(res)


if __name__ == "__main__":
    solve()
