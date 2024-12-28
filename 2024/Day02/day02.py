from Day02.day02_enums import ReactorState


class RedNoseReactor:

    def is_safe_report(self, report) -> bool:
        if len(report) < 1:
            return False

        current_direction = ReactorState.START

        for i in range(len(report) - 1):
            current_item = report[i]
            next_item = report[i + 1]

            direction = self._get_reactor_state(current_item, next_item)
            safe_direction = self._is_safe_item_direction(current_direction, direction)
            current_direction = direction

            safe_diff = self._is_safe_item_difference(current_item, next_item)
            if not safe_direction or not safe_diff:
                return False

        return True

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

