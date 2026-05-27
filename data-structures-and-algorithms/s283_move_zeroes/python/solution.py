class Solution:
    @staticmethod
    def move_zeroes(nums: list[int]) -> None:
        """
        Two Pointers Approach (Slow & Fast)

        Solution modifies list in-place.

        :param nums: The array of integers to be processed.
        :type nums: list[int]
        :return: None. The input list is modified in-place.
        :rtype: None
        """
        last_non_zero: int = 0

        for idx, _ in enumerate(nums):
            if nums[idx] != 0:
                nums[last_non_zero], nums[idx] = nums[idx], nums[last_non_zero]

                last_non_zero += 1
