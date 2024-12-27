import unittest

from day01 import Day01


class Day01Tests(unittest.TestCase):

    def test_a_example(self):
        day_01_a = Day01()
        total_distance = day_01_a.total_list_diffs([3, 4, 2, 1, 3, 3], [4, 3, 5, 3, 9, 3])
        self.assertEqual(total_distance, 11)  # add assertion here

    def test_b_example(self):
        day_01_b = Day01()
        similarity_score = day_01_b.calc_similarity_score([3, 4, 2, 1, 3, 3], [4, 3, 5, 3, 9, 3])
        self.assertEqual(similarity_score, 31)

    def test_iterator(self):
        a = set([1, 2, 3, 3, 3, 4])
        a.update([4, 3, 5, 3, 9, 3])
        b = {item: 0 for item in a}
        self.assertEqual(b, {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 9: 0})


if __name__ == '__main__':
    unittest.main()
