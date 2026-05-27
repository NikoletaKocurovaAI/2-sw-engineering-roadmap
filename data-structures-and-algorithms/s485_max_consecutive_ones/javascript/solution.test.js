import { describe, it, expect } from 'vitest';
import { findMaxConsecutiveOnes } from './solution.js';

describe('Solution: 485 Max consecutive ones', () => {
    // test cases
    it.each([
        [[0], 0], [[1], 1], [[1, 1, 0, 1, 1, 1], 3], [[1, 0, 1, 1, 0, 1], 2],
    ])('Test solution', (inputValue, expectedResult) => {
        const actual = findMaxConsecutiveOnes(inputValue);
        expect(actual).toBe(expectedResult);
    });
});