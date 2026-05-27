class Solution:
    @staticmethod
    def peak_index_in_mountain_array(arr: list[int]) -> int:
        low_index, high_index = 0, len(arr) - 1

        while low_index < high_index:
            mid_index = (low_index + high_index) // 2

            if arr[mid_index] > arr[mid_index + 1]:
                high_index = mid_index
            else:
                low_index = mid_index + 1

        return low_index
