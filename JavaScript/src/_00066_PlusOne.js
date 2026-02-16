/**
 * Given a *large integer* represented as an integer array `digits`, where each
 * `digits[i]` is the `ith` digit of the integer, the digits are ordered from
 * most significant to least significant in left-to-right order. The large
 * integer does not contain any leading `0`'s.
 *
 * Increment the large integer by one and return *the resulting array of digits*.
 * @param {number[]} digits large integer represented as an integer array
 * @returns {number[]} integer array representing the large integer incremented
 * by one
 */
var plusOne = function (digits) {
    // For each element of digits beginning with the last...
    for (let i = digits.length - 1; i >= 0; i--) {
        // If the digit is less than 9, add 1 to it and return digits.
        if (digits[i] < 9) {
            digits[i]++;
            return digits;
        }
        // Otherwise, the digit becomes 0 and carry the 1.
        digits[i] = 0;
    }

    // If the loop completes, the final carry must be added.
    digits.unshift(1);
    return digits;
};

module.exports = { plusOne };
