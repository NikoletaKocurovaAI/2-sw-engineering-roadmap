/**
 *  Linear search approach
 * 
 * @param {number[]} nums binary array
 * @return {number} the maximum number of consecutive 1's in the array
 */
var findMaxConsecutiveOnes = function(nums) {
    let maxConsecutive = 0;
    let currentConsecutive = 0;
    
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] == 1) {
            currentConsecutive ++;
            maxConsecutive = Math.max(maxConsecutive, currentConsecutive)
            continue;
        }
        currentConsecutive = 0;
    }
    return maxConsecutive;
};

export { findMaxConsecutiveOnes };