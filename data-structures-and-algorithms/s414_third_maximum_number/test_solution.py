import unittest

from .solution import Solution


class SolutionTestCase(unittest.TestCase):
    def test_solution(self) -> None:
        solution = Solution()

        test_cases = [([2, 2, 3, 1], 3)]

        for nums, expected_result in test_cases:
            actual_result = solution.third_max(nums)
            self.assertEqual(expected_result, actual_result)
