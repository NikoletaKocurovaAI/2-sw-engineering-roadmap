import unittest

from solution import Solution  # type: ignore


class SolutionTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_valid_cases(self) -> None:
        valid_cases = [
            ("()" * 10000, True),
            ("()", True),
            ("()[]{}", True),
            ("([])", True),
            ("((()))", True),
        ]
        for case, expected in valid_cases:
            solution = Solution()

            with self.subTest(case=case):
                self.assertEqual(solution.isValid(case), expected)

    def test_invalid_cases(self) -> None:
        invalid_cases = [
            (")(){}", False),
            ("(()))", False),
            ("(" * 10000 + ")" * 9999, False),
            ("(((", False),
            ("]", False),
            ("(?{}{}{}", False),
            ("(", False),
            ("(]", False),
            ("{[(])}", False),
            ("", False),
        ]
        for case, expected in invalid_cases:
            solution = Solution()

            with self.subTest(case=case):
                self.assertEqual(solution.isValid(case), expected)
