import unittest

from .solution import Solution


class SolutionTestCase(unittest.TestCase):
    def test_solution(self) -> None:
        solution = Solution()

        test_cases = [
            ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
            ([0], [0]),
            ([1, 0], [1, 0]),
            ([0, 0, 1], [1, 0, 0]),
        ]

        for nums_to_process, expected in test_cases:
            # The "Shallow Copy" - new object in memory
            # A safe "backup" copy, because the move_zeroes() changes nums object
            nums_to_process_backup = list(nums_to_process)

            solution.move_zeroes(nums=nums_to_process)

            # Check if the mutated list matches the expected list
            with self.subTest(nums=list(nums_to_process_backup)):
                # nums_to_process is now changed object
                self.assertEqual(nums_to_process, expected, f"Failed for input: {nums_to_process_backup}")
