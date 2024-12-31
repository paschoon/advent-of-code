from Day03.day03 import CorruptedMemoryScan


def get_corrupted_memory_values(filename):
    memory_values: str
    with open(filename, "rt", encoding="utf_8") as f:
        memory_values = f.read()
    return memory_values


def run_input_a():
    memory_values = get_corrupted_memory_values('input_a.txt')
    # x = CorruptedMemoryScan('xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))')
    x = CorruptedMemoryScan(memory_values)
    return x.salvage_memory()


def run_input_b():

    x = CorruptedMemoryScan("xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))")
    # x = CorruptedMemoryScan(memory_values)
    return x.salvage_memory()


if __name__ == '__main__':
    print(run_input_a())
    print(run_input_b())
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
