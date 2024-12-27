# This is a sample Python script.
import encodings

from day01 import Day01


# Press ⌃F5 to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

def run_input_a():
    list_one, list_two = get_list_one_and_two('input_a.txt')

    day_01 = Day01()
    total_distance = day_01.total_list_diffs(list_one, list_two)
    return total_distance


def get_list_one_and_two(filename):
    list_one = []
    list_two = []
    with open(filename, "rt", encoding="utf_8") as f:
        for line in f:
            items = line.split('   ')
            list_one.append(int(items[0]))
            list_two.append(int(items[1]))
    return list_one, list_two


# Press the green button in the gutter to run the script.
def run_input_b():
    list_one, list_two = get_list_one_and_two('input_b.txt')

    day_01 = Day01()
    total_distance = day_01.calc_similarity_score(list_one, list_two)
    return total_distance


if __name__ == '__main__':
    print(run_input_a())
    print(run_input_b())
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
