/**
 * Reverse bits of a given 32 bits signed integer.
 * @param {number} n 32 bit signed integer
 * @returns {number} `n` with bits reversed
 */
var reverseBits = function (n) {
    let result;

    // For each bit of a 32 bit integer...
    for (let i = 0; i < 32; i++) {
        // Step 1. Sift result left by 1 bit. (e.g. 001 -> 0010)
        // Step 2. Extract LSB of n. (e.g. 0101 & 1 -> 1 or 1100 & 1 -> 0)
        // Step 3. Result is bitwise OR of Step 1 and Step 2.
        //         (e.g. 01010 | 1 -> 01011 or 01010 | 0 -> 01010)
        result = (result << 1) | (n & 1);
        // Shift n right one bit to remove the LSB
        n = n >>> 1; 
    }
    
    return result;
};

module.exports = { reverseBits };
