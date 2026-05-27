import unittest

from solution import Solution  # type: ignore


class SolutionTestCase(unittest.TestCase):
    def test_max_sub_array_raises_value_error_when_nums_empty(self) -> None:
        with self.assertRaises(ValueError):
            Solution(nums=[])

    def test_calculate_max_subarray(self) -> None:
        test_cases = [
            ([1], 1),
            ([5, 4, -1, 7, 8], 23),
            ([2, 3, -8, 7, -1, 2, 3], 11),
            ([-2, -4], -2),
            ([5, 4, 1, 7, 8], 25),
        ]

        for nums, expected in test_cases:
            solution = Solution(nums=nums)

            actual = solution.calculate_max_subarray(0, len(nums) - 1)
            self.assertEqual(actual, expected)
