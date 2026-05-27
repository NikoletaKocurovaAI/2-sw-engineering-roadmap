class Solution:
    @staticmethod
    def search(nums: list[int], target: int) -> int:
        # Time Complexity: 4*O(1) = O(1)
        # Space Complexity: 2*O(1) = O(1)
        low, high = 0, len(nums) - 1

        # Time Complexity: O(log N)
        # Space Complexity: O(1)
        while low <= high:
            mid = (low + high) // 2

            if target == nums[mid]:
                return mid

            elif target > nums[mid]:
                low = mid + 1

            else:
                high = mid - 1

        # Total search() Time Complexity: O(log N)
        # Total search() Space Complexity: O(1)
        return -1
