class Solution:
    @staticmethod
    def remove_duplicates(input_value: str) -> str:
        """
        Remove all adjacent duplicates in a string.

        :param input_value: The input string from which to remove adjacent duplicates.
        :type input_value: str
        :return: The string after removing all adjacent duplicates.
        :rtype: str
        """
        stack: list[str] = []

        for char in input_value:
            if stack and char == stack[-1]:
                stack.pop()
            else:
                stack.append(char)

        return "".join(stack)
