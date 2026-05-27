import unittest

from .solution import Solution


class SolutionTestCase(unittest.TestCase):
    def test_solution(self) -> None:
        solution = Solution()
        test_cases = [
            ([0], 0),
            ([1], 1),
            ([1, 1, 0, 1, 1, 1], 3),
            ([1, 0, 1, 1, 0, 1], 2),
        ]

        for input_value, expected_result in test_cases:
            self.assertEqual(expected_result, solution.find_max_consecutive_ones(input_value))
