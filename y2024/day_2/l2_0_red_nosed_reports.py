from y2024.input_output import read_level_input

LEVEL = '2.1'


def get_input(level):
    input_data = read_level_input(level)
    data = []
    for report in input_data:
        data.append(list(map(lambda lvl: int(lvl), report.split(' '))))
    return data


def solve():
    reports = get_input(LEVEL)
    safe_reports = 0
    for report in reports:
        order = None
        unsafe_report = False
        for i in range(len(report) - 1):
            if report[i] == report[i+1]:
                unsafe_report = True
                break
            if report[i] > report[i + 1]:
                if not order:
                    order = 'desc'
                elif order == 'asc':
                    unsafe_report = True
                    break
            if report[i] < report[i + 1]:
                if not order:
                    order = 'asc'
                elif order == 'desc':
                    unsafe_report = True
                    break
            if abs(report[i] - report[i + 1]) > 3:
                unsafe_report = True
                break
        if not unsafe_report:
            safe_reports += 1
    print(safe_reports)


if __name__ == "__main__":
    solve()
