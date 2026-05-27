import unittest

from solution import Solution  # type: ignore


class SolutionTestCase(unittest.TestCase):
    def test_solution(self) -> None:
        solution = Solution()

        test_cases = [
            ([1, 3, 5, 6], 5, 2),
            ([1, 3, 5, 6], 2, 1),
            ([1, 2, 4, 5, 6, 7], 3, 2),
            ([1, 2, 3, 4, 5, 7], 6, 5),
            ([1, 3, 5, 6], 7, 4),
            ([4, 9, 12], 2, 0),
        ]

        for nums, target, expected_result in test_cases:
            actual_result = solution.search_insert(nums, target)  # type: ignore
            self.assertEqual(expected_result, actual_result)
