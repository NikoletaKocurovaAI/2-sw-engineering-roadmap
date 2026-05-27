import unittest

from solution import Solution


class SolutionTestCase(unittest.TestCase):
    def test_solution(self) -> None:
        solution = Solution()

        test_cases = [([-1, 0, 3, 5, 9, 12], 9, 4), ([-1, 0, 3, 5, 9, 12], 2, -1), ([-1, 0, 3, 5, 9, 12], 0, 1)]

        for nums, target, expected_result in test_cases:
            actual_result = solution.search(nums, target)
            self.assertEqual(actual_result, expected_result)
