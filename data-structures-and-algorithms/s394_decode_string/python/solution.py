class Solution:
    def decode_string_iterative(self, s: str) -> str:
        """
        Iterative approach to decode a string

        :param s: string: the string to decode. Input example: "2[abc]3[cd]ef".
        :return: string: the decoded string
        """
        # N - the length of the input
        # L - the length of the final decoded output string
        # K - the length of the new string being created
        # M - the maximum depth of the nesting

        # Time Complexity: 2x O(1) = O(1)
        stack: list[tuple[str, int]] = []
        multiplier: int = 0

        # Between iterations, variable holds substring to multiply
        # At the end, variable holds decoded string result
        # Time Complexity: O(1)
        current_result: str = ""

        # While the loop runs N times, the total work is dominated by string building
        # Time Complexity is not O(N)
        # Time Complexity: O(L)
        for char in s:
            # Time Complexity: O(1)
            if char.isdigit():
                # Time Complexity: 4 x O(1) = O(1)
                multiplier = multiplier * 10 + int(char)  # 'multiplier * 10' is used in case the s = 100[a]

            # Time Complexity: O(1)
            elif char == "[":
                # Time Complexity: O(1)
                stack.append((current_result, multiplier))

                # Time Complexity: 2x O(1) = O(1)
                current_result = ""
                multiplier = 0

            # Time Complexity: O(1)
            elif char == "]":
                # Time Complexity: 3 x O(1) = O(1)
                previous_result, next_sequence_multiplier = stack.pop()

                # Time Complexity: 2 x O(1) + O(K) = O(1) + O(K) = O(K)
                # K - the length of the new string being created
                # Python must allocate memory and copy characters to create the new string
                current_result = previous_result + (next_sequence_multiplier * current_result)

            # Time Complexity: O(1)
            else:
                # Time Complexity: O(K)
                # K - the length of the new string being created
                current_result += char

        # Time Complexity: O(1)
        return current_result

        # Total decode_string_iterative() Time Complexity: O(L)
        # Total decode_string_iterative() Space Complexity: O(L + M)
        # L - the length of the final decoded output string
        # M - the maximum depth of the nesting

    def decode_string_recursive(self, s: str) -> str:
        """
        Recursive approach to decode a string

        :param s: string: the string to decode
        :return: string: the decoded string
        """
        index: list[int] = [0]

        def decode() -> str:
            result: str = ""
            multiplier: int = 0

            while index[0] < len(s):
                char = s[index[0]]

                if char.isdigit():
                    multiplier = multiplier * 10 + int(char)  # 'multiplier * 10' is used in case the s = 100[a]

                elif char == "[":
                    index[0] += 1
                    decoded_inner = decode()

                    result += multiplier * decoded_inner
                    multiplier = 0

                elif char == "]":
                    return result

                else:
                    result += char

                index[0] += 1

            return result

        return decode()
