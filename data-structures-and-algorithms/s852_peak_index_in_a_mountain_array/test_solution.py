import unittest

from .solution import Solution


class SolutionTestCase(unittest.TestCase):
    def test_solution(self) -> None:
        solution = Solution()

        test_cases = [([0, 10, 15, 20, 8, 5, 2], 3)]

        for array, expected_result in test_cases:
            result = solution.peak_index_in_mountain_array(array)
            self.assertEqual(expected_result, result)
