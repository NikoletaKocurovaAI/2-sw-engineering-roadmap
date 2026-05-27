from collections import Counter


class Solution:
    @staticmethod
    def is_anagram(s: str, t: str) -> bool:
        """
        Hashmap Approach

        Given two strings s and t, return true if t is an anagram of s, and false otherwise.

        :param s: The source string to compare.
        :type s: str
        :param t: The target string to check against.
        :type t: str
        :return: True if t is an anagram of s, False otherwise.
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        # object creation O(2n) -> O(n)
        # objects comparison - if both dictionaries have the same number of unique keys is O(1)

        # objects comparison - Key-Value Check. The no. of lowercase English letters is 26. Iterates through both
        # objects, so 2*O(26) -> 2*O(1) -> O(1)
        return Counter(s) == Counter(t)

        # Total time complexity: O(n) + O(1) + O(1) = O(n)
