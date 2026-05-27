import unittest

from solution import Solution


class SolutionTestCase(unittest.TestCase):
    def test_solution(self) -> None:
        solution = Solution()

        test_cases = [("abbaca", "ca"), ("azxxzy", "ay")]

        for case, expected_result in test_cases:
            actual_result = solution.remove_duplicates(case)
            self.assertEqual(actual_result, expected_result)
