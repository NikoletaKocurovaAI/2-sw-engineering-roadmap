import sys


class Solution:
    def __init__(self, nums: list[int]) -> None:
        if not nums:
            raise ValueError("Empty input array.")

        self.nums: list[int] = nums

    def calculate_max_subarray(self, left_idx: int = 0, right_idx: int = 0) -> int:
        """

        :param left_idx: int: The left index of the current subarray.
        :param right_idx: int: The right index of the current subarray.
        :return: int: The maximum subarray sum in the range [left_idx, right_idx].
        """
        if left_idx == right_idx:
            return self.nums[left_idx]

        mid: int = (left_idx + right_idx) // 2

        left_max: int = self.calculate_max_subarray(left_idx=left_idx, right_idx=mid)
        right_max: int = self.calculate_max_subarray(left_idx=mid + 1, right_idx=right_idx)

        left_cross_max: int = self._calculate_max_sum_in_range(start=mid, stop=left_idx - 1, step=-1)
        right_cross_max: int = self._calculate_max_sum_in_range(start=mid + 1, stop=right_idx + 1)
        cross_max: int = left_cross_max + right_cross_max

        return max(left_max, right_max, cross_max)

    def _calculate_max_sum_in_range(self, start: int, stop: int, step: int = 1) -> int:
        max_sum: int = -sys.maxsize
        current_sum: int = 0

        for i in range(start, stop, step):
            current_sum += self.nums[i]
            max_sum: int = max(max_sum, current_sum)  # type: ignore

        return max_sum
