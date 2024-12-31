import re

from Day03.day03_enums import NumberParsingState, MulParsingState


class CorruptedMemoryScan:
    def __init__(self, memory_values):
        self._memoryValues = memory_values

    def get_totals(self):
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

    def get_totals_using_regex(self):
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
        state = NumberParsingState.INIT
        first_num: str = ""
        second_num: str = ""

        for i in range(len(self._memoryValues) - start_position - 1):
            current_char = self._memoryValues[start_position + i]
            print(f'_find_nums:[{current_char}],current_state=[{state}]')
            if state == NumberParsingState.INIT:
                if current_char.isnumeric():
                    first_num += current_char
                    state = NumberParsingState.FIRST_NUM
                else:
                    return None

            elif state == NumberParsingState.FIRST_NUM:
                if current_char.isnumeric() and len(first_num) < 3:
                    first_num += current_char
                elif current_char == ',':
                    state = NumberParsingState.SECOND_NUM
                else:
                    return None

            elif state == NumberParsingState.SECOND_NUM:
                if current_char.isnumeric() and len(second_num) < 3:
                    second_num += current_char
                elif current_char == ')':
                    state = NumberParsingState.END
                else:
                    return None

            else:
                break

        if state == NumberParsingState.END:
            return int(first_num), int(second_num)

        return None

    def get_totals_with_conditionals(self):
        total_value = 0
        position = 0
        while position < len(self._memoryValues):
            position = self._find_next_mul_position_using_conditionals(position)
            if position is None:
                print("'mul(' not found")
                break

            print(f"'mul(' found at position {position}")
            nums = self._find_nums(position)
            if nums is not None:
                first_num, second_num = nums
                print(f"nums found {first_num},{second_num}")
                total_value += first_num * second_num
            else:
                print('nums not found')

        return total_value

    def _find_next_mul_position(self, start_position):
        state = MulParsingState.INIT

        for i in range(len(self._memoryValues) - start_position):
            char_value = self._memoryValues[start_position + i]
            print(f'_find_next_mul_position() - found char [{char_value}], state=[{state}]')

            if state == MulParsingState.INIT:
                if char_value == 'm':
                    state = MulParsingState.M
                else:
                    state = MulParsingState.INIT
            elif state == MulParsingState.M:
                if char_value == 'u':
                    state = MulParsingState.U
                else:
                    state = MulParsingState.INIT
            elif state == MulParsingState.U:
                if char_value == 'l':
                    state = MulParsingState.L
                else:
                    state = MulParsingState.INIT
            elif state == MulParsingState.L:
                if char_value == '(':
                    return start_position + i + 1
                else:
                    state = MulParsingState.INIT

        return None

    def _find_next_mul_position_using_conditionals(self, start_position):
        state = MulParsingState.INIT
        ignore_muls = False

        for i in range(len(self._memoryValues) - start_position):
            char_value = self._memoryValues[start_position + i]
            print(f'_find_next_mul_position() - found char [{char_value}], state=[{state}]')

            if state == MulParsingState.INIT:
                if char_value == 'm' and not ignore_muls:
                    state = MulParsingState.M
                elif char_value == 'd':
                    state = MulParsingState.D
                else:
                    state = MulParsingState.INIT
            elif state == MulParsingState.M:
                if char_value == 'u':
                    state = MulParsingState.U
                else:
                    state = MulParsingState.INIT
            elif state == MulParsingState.U:
                if char_value == 'l':
                    state = MulParsingState.L
                else:
                    state = MulParsingState.INIT
            elif state == MulParsingState.L:
                if char_value == '(':
                    return start_position + i + 1
                else:
                    state = MulParsingState.INIT
            elif state == MulParsingState.D:
                if char_value == 'o':
                    state = MulParsingState.O
                else:
                    state = MulParsingState.INIT
            elif state == MulParsingState.O:
                if char_value == '(':
                    state = MulParsingState.DO_PAREN
                elif char_value == 'n':
                    state = MulParsingState.N
                else:
                    state = MulParsingState.INIT
            elif state == MulParsingState.N:
                if char_value == "'":
                    state  = MulParsingState.SINGLE_QUOTE
                else:
                    state = MulParsingState.INIT
            elif state == MulParsingState.SINGLE_QUOTE:
                if char_value == 't':
                    state = MulParsingState.T
                else:
                    state = MulParsingState.INIT
            elif state == MulParsingState.T:
                if char_value == '(':
                    state = MulParsingState.DONT_PAREN
                else:
                    state = MulParsingState.INIT
            elif state == MulParsingState.DONT_PAREN:
                if char_value == ')':
                    state = MulParsingState.INIT
                    ignore_muls = True
                else:
                    state = MulParsingState.INIT
            elif state == MulParsingState.DO_PAREN:
                if char_value == ')':
                    state = MulParsingState.INIT
                    ignore_muls = False
                else:
                    state = MulParsingState.INIT

        return None
