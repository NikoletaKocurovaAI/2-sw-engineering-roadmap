import unittest

from .solution import Solution


class SolutionTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()
        self.test_cases = [("3[a]2[bc]", "aaabcbc"), ("3[a2[c]]", "accaccacc"), ("2[abc]3[cd]ef", "abcabccdcdcdef")]

    def test_solution_decode_string_iterative(self) -> None:
        for test_input, expected_result in self.test_cases:
            actual_result = self.solution.decode_string_iterative(test_input)

            self.assertEqual(actual_result, expected_result)
