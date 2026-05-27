import unittest

from solution import Solution  # type: ignore


class SolutionTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_two_sum_returns_empty_list_when_one_element_in_nums(self) -> None:
        actual = self.solution.two_sum(nums=[2], target=10)
        self.assertEqual(actual, [])

    def test_two_sum_returns_empty_list_when_nums_empty(self) -> None:
        actual = self.solution.two_sum(nums=[], target=10)
        self.assertEqual(actual, [])

    def test_two_sum_when_two_possible_answers(self) -> None:
        actual = self.solution.two_sum(nums=[1, 3, 5, 7], target=8)
        self.assertEqual(actual, [1, 2])

    def test_two_sum_when_target_not_found(self) -> None:
        actual = self.solution.two_sum(nums=[1, 3, 5, 7], target=22)
        self.assertEqual(actual, [])

    def test_two_sum_when_negative_element_in_nums(self) -> None:
        actual = self.solution.two_sum(nums=[1, -3, 5, 7], target=-2)
        self.assertEqual(actual, [0, 1])

    def test_two_sum_when_positive_elements_in_nums(self) -> None:
        test_cases = [
            ([2, 7, 11, 15], 9, [0, 1]),
            ([3, 2, 4], 6, [1, 2]),
            ([3, 3], 6, [0, 1]),
        ]

        for nums, target, expected in test_cases:
            with self.subTest(nums=nums, target=target, expected=expected):
                actual = self.solution.two_sum(nums, target)
                self.assertEqual(actual, expected)

    def test_two_sum_with_duplicates(self) -> None:
        actual = self.solution.two_sum(nums=[1, 1, 1, 1], target=2)
        self.assertEqual(actual, [0, 1])
