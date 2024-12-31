import re

from Day03.day03_enums import ParsingState


class CorruptedMemoryScan:
    def __init__(self, memory_values):
        self._memoryValues = memory_values

    def salvage_memory(self):
        total_value = 0
        mul = "mul("
        positions = self._find_mul_positions(mul)
        for position in positions:
            nums = self._find_nums(position + len(mul))
            if nums is not None:
                first_num, second_num = nums
                print(f"Found 'mul(' at position {first_num},{second_num}")
                total_value += first_num * second_num
            else:
                print('nums not found')

        return total_value

    def salvage_memory_using_regex(self):
        total_value = 0

        regex = r'mul\((\d+),(\d+)\)'
        # regex = r'mul((\d{3}),(\d{3}))'
        matches = re.findall(regex, self._memoryValues)
        for match in matches:
            first_int, second_int = match
            total_value += int(first_int) * int(second_int)

        return total_value

    def salvage_memory_with_conditionals(self):
        total_value = 0

        regex = r'mul\((\d+),(\d+)\)'
        # regex = r'mul((\d{3}),(\d{3}))'
        matches = re.findall(regex, self._memoryValues)
        for match in matches:
            first_int, second_int = match
            total_value += int(first_int) * int(second_int)

        return total_value

    def _find_mul_positions(self, substring):
        text = self._memoryValues
        # substring = "mul("

        positions = [i for i in range(len(text)) if text.startswith(substring, i)]

        return positions
        # for position in positions:
        #     print(f"Found '{substring}' at position {position}")

    def _find_nums(self, start_position) -> (int, int):
        state = ParsingState.INIT
        first_num: str = ""
        second_num: str = ""

        for i in range(len(self._memoryValues) - start_position - 1):
            current_char = self._memoryValues[start_position + i]
            print(f'_find_nums:[{current_char}],current_state=[{state}]')
            if state == ParsingState.INIT:
                if current_char.isnumeric():
                    first_num += current_char
                    state = ParsingState.FIRST_NUM
                else:
                    return None

            elif state == ParsingState.FIRST_NUM:
                if current_char.isnumeric() and len(first_num) < 3:
                    first_num += current_char
                elif current_char == ',':
                    state = ParsingState.SECOND_NUM
                else:
                    return None

            elif state == ParsingState.SECOND_NUM:
                if current_char.isnumeric() and len(second_num) < 3:
                    second_num += current_char
                elif current_char == ')':
                    state = ParsingState.END
                else:
                    return None

            else:
                break

        if state == ParsingState.END:
            return int(first_num), int(second_num)

        return None
