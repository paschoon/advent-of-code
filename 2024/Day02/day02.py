from Day02.day02_enums import ReactorState


class RedNoseReactorReport:
    _report: list[int]

    def __init__(self , report):
        self._report = report
        self._current_reactor_state = ReactorState.START
        self._problem_count = 0


    def is_safe_report(self) -> bool:
        self._current_reactor_state = ReactorState.START

        unsafe_level_index = self._find_first_unsafe_level_index()

        if unsafe_level_index is None:
            return True

        return False

    def is_safe_report_with_dampener(self) -> bool:
        unsafe_level_index = self._find_first_unsafe_level_index()

        if unsafe_level_index is None:
            return True

        self._report.pop(unsafe_level_index)
        return self.is_safe_report()

    def _find_first_unsafe_level_index(self):
        if len(self._report) < 1:
            return None

        for i in range(len(self._report) - 1):
            current_item = self._report[i]
            next_item = self._report[i + 1]

            safe_level = self._is_single_level_safe(current_item, next_item)

            if not safe_level:
                return i

        return None

    def _is_single_level_safe(self, current_item, next_item):
        direction = self._get_reactor_state(current_item, next_item)
        safe_direction = self._is_safe_item_direction(self._current_reactor_state, direction)
        self._current_reactor_state = direction

        safe_diff = self._is_safe_item_difference(current_item, next_item)
        if safe_direction and safe_diff:
            return True

        return False


    @staticmethod
    def _is_safe_item_difference(current_item, next_item):
        x = abs(current_item - next_item)

        if x > 0 and x <= 3:
            return True

        return False

    @staticmethod
    def _is_safe_item_direction(current_direction, direction):
        if current_direction == ReactorState.START:
            return True

        if direction == ReactorState.NEUTRAL:
            return False

        if direction == current_direction:
            return True

        return False

    @staticmethod
    def _get_reactor_state(current_item, next_item) -> ReactorState:
        num = current_item - next_item

        if num > 0:
            return ReactorState.POSITIVE
        elif num < 0:
            return ReactorState.NEGATIVE
        else:
            return ReactorState.NEUTRAL


