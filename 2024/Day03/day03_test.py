import unittest

from Day03.day03 import CorruptedMemoryScan


class Day03Test(unittest.TestCase):
    def test_get_totals_with_regex(self):
        x = CorruptedMemoryScan('xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))')
        total = x.get_totals_using_regex()
        self.assertEqual(total, 161)  # add assertion here

    def test_get_totals_without_regex(self):
        x = CorruptedMemoryScan('xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))')
        total = x.get_totals()
        self.assertEqual(total, 161)  # add assertion here

    def test_get_totals_with_extra_conditionals(self):
        x = CorruptedMemoryScan("xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))")
        total = x.get_totals_with_conditionals()
        self.assertEqual(total, 48)

if __name__ == '__main__':
    unittest.main()
