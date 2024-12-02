from red_nosed_reports_2_0 import get_input

LEVEL = '2.1'


def is_safe_report(report: list[int]):
    order = None
    unsafe_report = False
    for i in range(len(report) - 1):
        if report[i] == report[i + 1]:
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
    return not unsafe_report


def solve():
    reports = get_input(LEVEL)
    safe_reports = 0
    for report in reports:
        is_safe = is_safe_report(report)
        if is_safe:
            safe_reports += 1
            continue

        for index in range(len(report)):
            new_report = report[:index] + report[index+1:]
            is_safe = is_safe_report(new_report)
            if is_safe:
                safe_reports += 1
                break

    print(safe_reports)


if __name__ == "__main__":
    solve()
