import unittest

from solution import Solution  # type: ignore


class SolutionTestCase(unittest.TestCase):
    def test_is_palindrome(self) -> None:
        solution = Solution()
        test_cases = [(121, True), (-121, False), (10, False)]

        for input_value, expected_result in test_cases:
            assert solution.is_palindrome(input_value) == expected_result
