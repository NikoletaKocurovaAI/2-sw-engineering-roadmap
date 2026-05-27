class Solution:
    @staticmethod
    def find_max_consecutive_ones(nums: list[int]) -> int:
        """
        Linear search approach

        :param nums: binary array
        :return: int: the maximum number of consecutive 1's in the array
        """
        # 2*O(1) = O(1)
        max_consecutive: int = 0
        current_consecutive: int = 0

        # O(N) * O(1) = O(N)
        for item in nums:
            # O(1)
            if item == 1:
                # 4*O(1) = O(1)
                current_consecutive += 1
                max_consecutive = max(max_consecutive, current_consecutive)
                continue

            # O(1)
            current_consecutive = 0

        # O(1)
        return max_consecutive

        # Total find_max_consecutive_ones() time complexity:
        # O(1) + O(N) + O(1) = 2*O(1) + O(N) = O(1) + O(N) = O(N)
