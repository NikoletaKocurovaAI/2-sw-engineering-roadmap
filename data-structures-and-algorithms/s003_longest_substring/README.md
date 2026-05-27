# 3 Longest Substring Without Repeating Characters

Leet Code reference: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

Topic: Hash table, String, Sliding window

## Description

Given a string s, find the length of the longest substring without duplicate characters.

Example 1:

    Input: s = "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3.

Example 2:

    Input: s = "bbbbb"
    Output: 1
    Explanation: The answer is "b", with the length of 1.

Example 3:

    Input: s = "pwwkew"
    Output: 3
    Explanation: The answer is "wke", with the length of 3.
    Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:

- 0 <= s.length <= 5 * 10^4
- s consists of English letters, digits, symbols and spaces.

## Additional notes

Input analysis:

- Type: string, builtin DS, and immutable collection
- Range: 
  - English letters, digits, symbols and spaces
  - length 0
- Uniqueness: elements are not unique
- Order: unsorted

**Algorithm’s DS:** 
- dict

**Algorithm’s approach:**
- sliding window
