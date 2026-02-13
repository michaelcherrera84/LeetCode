/**
 * Given a positive integer `n`, write a function that returns the number set
 * bits in it's binary representations (also known as the Hamming weight).
 * @param {number} n positive integer
 * @returns the number of set bits in the binary representation of `n`
 */
var hammingWeight = function (n) {
    let count = 0;

    // For each bit of n, extract the LSB of n and add it to count. Then shift 
    // n bits to the right by 1 to remove the counted bit.
    for(let i = 0; i < 32; i++) {
        count += (n & 1);
        n = n >>> 1;
    }

    return count;
};

module.exports = { hammingWeight };
