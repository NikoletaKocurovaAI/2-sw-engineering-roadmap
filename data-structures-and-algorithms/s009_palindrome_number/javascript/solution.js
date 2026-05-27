/**
 * Determine whether an integer is a palindrome.
 *
 * @param {number} x The integer to check for palindrome property.
 * @return {boolean} True if `x` is a palindrome, False otherwise.
 */
var isPalindrome = function(x) {
    // value: str = str(x)
    let value = String(x)

    // left, right = 0, len(value) - 1
    let [left, right] = [0, value.length - 1]

    while (left <= right) {
        if (value[left] != value[right]) {
            return false;
        }
        left++;
        right--;
    }
    return true;
};

export { isPalindrome };