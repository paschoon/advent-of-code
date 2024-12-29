import re


class CorruptedMemoryScan:
    def __init__(self, memory_values):
        self._memoryValues = memory_values

    def salvage_memory(self):
        total_value = 0

        regex = r'mul\((\d+),(\d+)\)'
        # regex = r'mul((\d{3}),(\d{3}))'
        matches = re.findall(regex, self._memoryValues)
        for match in matches:
            first_int, second_int = match
            total_value += int(first_int) * int(second_int)

        return total_value