import unittest

from solution import Solution  # type: ignore


class SolutionTestCase(unittest.TestCase):
    def test_solution(self) -> None:
        solution = Solution()
        test_cases = [
            ("", 0),
            ("a", 1),
            ("ab", 2),
            ("aa", 1),
            ("aabcd", 4),
            ("abcchh", 3),
            ("abcabcbb", 3),
            ("bbbbb", 1),
            ("pwwkew", 3),
        ]

        for input_value, expected_result in test_cases:
            self.assertEqual(expected_result, solution.lengthOfLongestSubstring(input_value))
