import { describe, it, expect } from 'vitest';
import { isPalindrome } from './solution.js';

describe('Solution: 009 Palindrome number', () => {
    // test cases
    it.each([
        [121, true], [-121, false], [10, false],
    ])('Test is palindrome number', (inputValue, expectedResult) => {
        const actual = isPalindrome(inputValue);
        expect(actual).toBe(expectedResult);
    });
});
