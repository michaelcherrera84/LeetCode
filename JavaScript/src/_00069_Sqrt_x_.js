/**
 * Given a non-negative integer `x`, return *the square root of* `x` *rounded
 * down to the nearest integer*.
 * @param {number} x non-negative integer
 * @returns {number} the square root of `x` rounded down to the nearest integer
 */
var mySqrt = function (x) {
    let sqrt = 0;
    // Brute force all possible roots until the desired value is found.
    while ((sqrt + 1) * (sqrt + 1) <= x) {
        sqrt++;
    }
    return Math.floor(sqrt);
};

/**
 * Given a non-negative integer `x`, return *the square root of* `x` *rounded
 * down to the nearest integer*.
 * @param {number} x non-negative integer
 * @returns {number} the square root of `x` rounded down to the nearest integer
 */
var mySqrt1 = function (x) {
    // Trivial cases: sqrt(0) = 0, sqrt(1) = 1
    if (x < 2) return x;

    // Start with an overestimate.
    // Using x itself guarantees guess >= true sqrt.
    let guess = x;

    // We stop when guess is no longer too large.
    // Instead of checking guess * guess > x (which may overflow),
    // we compare guess > x / guess.
    while (guess > Math.floor(x / guess)) {

        // Newton update step:
        // New guess is the average of:
        // 1) current guess
        // 2) x / current guess  (which would be exact if guess were correct)
        //
        // This pulls the estimate closer to the true root.
        guess = Math.floor((guess + Math.floor(x / guess)) / 2);
    }

    return guess;
};

module.exports = { mySqrt, mySqrt1 };
