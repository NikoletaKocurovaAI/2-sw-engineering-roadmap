class Solution:
    @staticmethod
    def is_palindrome(x: int) -> bool:
        """
        Determine whether an integer is a palindrome.

        :param x: The integer to check for palindrome property.
        :type x: int
        :return: True if `x` is a palindrome, False otherwise.
        :rtype: bool
        """

        # Time complexity analysis:
        # O(N) for str(x) operation
        # O(N) for comparing each character
        # O(N) for str(x) operation and O(N) for slicing
        # Time complexity result: O(N) + O(N) + 2*O(N) = 4*O(N) = O(N)
        return str(x) == str(x)[::-1]

    @staticmethod
    def is_palindrome_manual_check(x: int) -> bool:
        # O(N)
        value: str = str(x)

        # 2*O(1) for 2 assignments
        # O(1) for len()
        # O(1) for substracting
        # Time complexity result: 4*O(1) = O(1)
        left, right = 0, len(value) - 1

        # O(N/2) for loop
        # O(1) work per iteration
        # Time complexity result: O(N/2) * O(1) = O(N)
        while left <= right:
            # O(1)
            if value[left] != value[right]:
                # O(1)
                return False

            # 2*O(1)
            left += 1
            right -= 1

        # O(1)
        return True
