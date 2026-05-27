class Solution:
    @staticmethod
    def search_insert(nums: list[int], target: int) -> int:
        """
        Iterative Binary Search Approach

        :param nums: a sorted array of distinct integers
        :param target: value to be found
        :return: int: return the index if the target is found. If not, return the index where it would be if it were
        inserted in order.
        """
        # 3*O(1) = O(1)
        if target > nums[-1]:
            return len(nums)

        # 3*O(1) = O(1)
        if target < nums[0]:
            return 0

        # 4*O(1) = O(1)
        low_index, high_index = 0, len(nums) - 1

        # O(log N) for looping + O(1) for operations inside loop
        # Time complexity result: O(log N) + O(1) = O(log N)
        while low_index <= high_index:
            # 3*O(1) = O(1)
            mid_index = (low_index + high_index) // 2

            # 3*O(1) = O(1)
            if nums[mid_index] == target:
                return mid_index

            # 4*O(1) = O(1)
            elif target < nums[mid_index]:
                high_index = mid_index - 1

            # 2*O(1) = O(1)
            else:
                low_index = mid_index + 1

        # 1*O(1) = O(1)
        return low_index

        # Total search_insert() time complexity:
        # O(1) + O(1) + O(1) + O(log N) + O(1) = 4*O(1) + O(log N) = O(1) + O(log N) = O(log N)
