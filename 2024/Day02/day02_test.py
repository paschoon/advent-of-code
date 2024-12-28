import unittest

from Day02.day02 import RedNoseReactorReport
from Day02.day02_enums import ReactorState


class Day02Tests(unittest.TestCase):
    def test_day02a_example_01(self):
        report = [7, 6, 4, 2, 1]
        safe = RedNoseReactorReport(report).is_safe_report()
        self.assertEqual(safe, True)

    def test_day02a_example_02(self):
        report = [1, 2, 7, 8, 9]
        safe = RedNoseReactorReport(report).is_safe_report()
        self.assertEqual(safe, False)

    def test_day02a_example_03(self):
        report = [9, 7, 6, 2, 1]
        safe = RedNoseReactorReport(report).is_safe_report()
        self.assertEqual(safe, False)

    def test_day02a_example_04(self):
        report = [1, 3, 2, 4, 5]
        safe = RedNoseReactorReport(report).is_safe_report()
        self.assertEqual(safe, False)

    def test_day02a_example_05(self):
        report = [8, 6, 4, 4, 1]
        safe = RedNoseReactorReport(report).is_safe_report()
        self.assertEqual(safe, False)

    def test_day02a_example_06(self):
        report = [1, 3, 6, 7, 9]
        safe = RedNoseReactorReport(report).is_safe_report()
        self.assertEqual(safe, True)

    def test_day02b_example_01(self):
        report = [7, 6, 4, 2, 1]
        safe = RedNoseReactorReport(report).is_safe_report_with_dampener()
        self.assertEqual(safe, True)

    def test_day02b_example_02(self):
        report = [1, 2, 7, 8, 9]
        safe = RedNoseReactorReport(report).is_safe_report_with_dampener()
        self.assertEqual(safe, False)

    def test_day02b_example_03(self):
        report = [9, 7, 6, 2, 1]
        safe = RedNoseReactorReport(report).is_safe_report_with_dampener()
        self.assertEqual(safe, False)

    def test_day02b_example_04(self):
        report = [1, 3, 2, 4, 5]
        safe = RedNoseReactorReport(report).is_safe_report_with_dampener()
        self.assertEqual(safe, True)

    def test_day02b_example_05(self):
        report = [8, 6, 4, 4, 1]
        safe = RedNoseReactorReport(report).is_safe_report_with_dampener()
        self.assertEqual(safe, True)

    def test_day02b_example_06(self):
        report = [1, 3, 6, 7, 9]
        safe = RedNoseReactorReport(report).is_safe_report_with_dampener()
        self.assertEqual(safe, True)

    def test_reactor_difference_safe(self):
        safe = RedNoseReactorReport._is_safe_item_difference(7, 6)
        self.assertEqual(safe, True)

    def test_day02_reactor_difference_too_big(self):
        safe = RedNoseReactorReport._is_safe_item_difference(6, 2)
        self.assertEqual(safe, False)

    def test_day02_reactor_difference_same(self):
        safe = RedNoseReactorReport._is_safe_item_difference(6, 6)
        self.assertEqual(safe, False)

    def test_day02_reactor_direction_unsafe_neutral(self):
        for state in [ ReactorState.NEGATIVE, ReactorState.POSITIVE]:
            safe = RedNoseReactorReport._is_safe_item_direction(state, ReactorState.NEUTRAL)
            self.assertEqual(safe, False)

    def test_day02_reactor_direction_unsafe_positive_then_negative(self):
        safe = RedNoseReactorReport._is_safe_item_direction(ReactorState.POSITIVE, ReactorState.NEGATIVE)
        self.assertEqual(safe, False)

    def test_day02_reactor_direction_unsafe_negative_then_positive(self):
        safe = RedNoseReactorReport._is_safe_item_direction(ReactorState.NEGATIVE, ReactorState.POSITIVE)
        self.assertEqual(safe, False)

    def test_day02_reactor_direction_safe_positive_then_positive(self):
        safe = RedNoseReactorReport._is_safe_item_direction(ReactorState.POSITIVE, ReactorState.POSITIVE)
        self.assertEqual(safe, True)

    def test_day02_reactor_direction_start_state_always_safe(self):
        for state in [ReactorState.NEUTRAL, ReactorState.NEGATIVE, ReactorState.POSITIVE]:
            safe = RedNoseReactorReport._is_safe_item_direction(ReactorState.START, state)
            self.assertEqual(safe, True)

if __name__ == '__main__':
    unittest.main()
