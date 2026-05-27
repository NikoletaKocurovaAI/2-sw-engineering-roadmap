import unittest

from .solution import Solution


class SolutionTestCase(unittest.TestCase):
    def test_solution(self) -> None:
        solution = Solution()

        test_cases = [
            ("apa", "app", False),
            ("ap", "app", False),
            ("abc", "def", False),
            ("a", "a", True),
            ("a", "b", False),
            ("anagram", "nagaram", False),
        ]

        for source_to_compare, target, expected_result in test_cases:
            actual_result = solution.is_anagram(source_to_compare, target)

            self.assertEqual(expected_result, actual_result)
