# This is a sample Python script.

from day01 import a_solve, b_solve


# Press ⌃F5 to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

def run_input_a():
    list_one = get_list('input_a.txt')

    pwd = a_solve(list_one)
    return pwd


def get_list(filename):
    list_one = []
    with open(filename, "rt", encoding="utf_8") as f:
        for line in f:
            list_one.append(line.strip())
    return list_one

def run_input_b():
    list_one = get_list('input_b.txt')

    pwd = b_solve(list_one)
    return pwd


if __name__ == '__main__':
    print(f'times landed on zero:[{run_input_a()}]')
    print(f'times past zero:[{run_input_b()}]')
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
