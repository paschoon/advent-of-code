from Day02.day02 import RedNoseReactorReport


def get_reports(filename):
    set_of_reports = []
    with open(filename, "rt", encoding="utf_8") as f:
        for line in f:
            items = line.split(' ')
            report = [int(i) for i in items]
            set_of_reports.append(report)
    return set_of_reports

def run_input_a():
    reports = get_reports('input_a.txt')
    safe_count = 0
    for report in reports:
        if RedNoseReactorReport(report).is_safe_report():
            safe_count += 1

    print(f'ReadNoseReactorReports that are safe: {safe_count}')

def run_input_b():
    reports = get_reports('input_b.txt')
    safe_count = 0
    for report in reports:
        if RedNoseReactorReport(report).is_safe_report_with_dampener():
            safe_count += 1

    print(f'ReadNoseReactorReports with dampener that are safe: {safe_count}')


if __name__ == '__main__':
    print(run_input_a())
    print(run_input_b())
# See PyCharm help at https://www.jetbrains.com/help/pycharm/