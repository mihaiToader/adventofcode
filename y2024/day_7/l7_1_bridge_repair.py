from y2024.input_output import read_level_input


LEVEL = '7.1'


def get_input(level):
    input_data = read_level_input(level)
    res = []
    for line in input_data:
        equation = dict()
        line_split = line.split(' ')
        equation['result'] = int(line_split[0].replace(':', ''))
        equation['values'] = [int(value) for value in line_split[1:]]
        res.append(equation)
    return res


def get_equation_result(equation, operators):
    result = equation['values'][0]
    for i in range(len(operators)):
        op = operators[i]
        x = equation['values'][i + 1]
        if op == '+':
            result += x
        if op == '*':
            result *= x
        if op == '||':
            result = int(str(result) + str(x))
    return result


def is_solution(equation, operators):
    if len(operators) != len(equation['values']) - 1:
        return False

    return get_equation_result(equation, operators) == equation['result']


def is_valid_choice(equation, operators, op):
    if len(operators) >= len(equation['values']) - 1:
        return False

    return get_equation_result(equation, operators[:] + [op]) <= equation['result']


def backtracking(equation, operators):
    if is_solution(equation, operators):
        return True

    for op in ['+', '*', '||']:
        if is_valid_choice(equation, operators, op):
            operators.append(op)
            result = backtracking(equation, operators)

            if result:
                return result
            operators.pop()
    return


def is_solvable_equation(equation):
    return backtracking(equation, [])


def solve():
    equations = get_input(LEVEL)

    res = 0
    for equation in equations:
        if is_solvable_equation(equation):
            res += equation['result']
    print(res)


if __name__ == "__main__":
    solve()
