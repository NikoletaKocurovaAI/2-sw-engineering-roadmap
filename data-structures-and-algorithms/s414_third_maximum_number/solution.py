class Solution:
    @staticmethod
    def third_max(nums: list[int]) -> int:
        """
        Linear search approach

        Returns the third distinct maximum number in the list.
        If the third maximum does not exist, returns the maximum number.

        :param nums: List of integers.
        :type nums: list[int]
        :return: The third distinct maximum number if it exists, otherwise the maximum number.
        :rtype: int
        """
        # 2*O(N) = O(N)
        nums = list(set(nums))

        # 2*O(1) = O(1)
        first = second = third = float("-inf")

        # O(N) * O(1) = O(N)
        for num in nums:
            # O(1)
            if num > first:
                # 2*O(1) = O(1)
                second = first
                first = num
            # first > num and num > second
            # 3*O(1) = O(1)
            elif first > num > second:
                # 2*O(1) = O(1)
                third = second
                second = num
            # first > num and num > second
            # 3*O(1) = O(1)
            elif second > num > third:
                # O(1)
                third = num

        # O(1) for float("-inf")
        # O(1) for comparison third != float("-inf")
        # O(1) for if ... else
        # O(1) for return
        # Time complexity: 4*O(1) = O(1)
        return third if third != float("-inf") else first  # type: ignore

        # Total third_max() time complexity:
        # O(N) + O(1) + O(N) + O(1) = 2*O(N) + 2*O(1) = O(N) + O(1) = O(N)
