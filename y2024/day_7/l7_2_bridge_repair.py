from l7_1_bridge_repair import get_input, is_solution, is_valid_choice

LEVEL = '7.1'


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
