/**
 * Given an integer `x`, return `true` *if* `x` *is a palindrome, and* `false`
 * *otherwise*.
 * @param {number} x and integer
 * @returns {boolean} `true` is `x` is a palindrome, and `false` otherwise
 */
var isPalindrome = function(x) {
    if (x < 0) return false;

    let original = x;
    let reversed = 0;  // x backwards

    while (x > 0) {
        // Multiply reversed by 10 to add a new 0 as the least significant digit.
        // Then add to it the result of x modulus 10 (lsd of x).
        reversed = 10 * reversed + x % 10;
        // Divide x by 10 and round down to remove the least significant digit.
        x = Math.floor(x / 10);
    }

    // If the original and the reversed are the same, the number is a palindrome.
    return original === reversed;
};

module.exports = { isPalindrome };