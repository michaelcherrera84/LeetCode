/**
 * Given two binary strings `a` and `b`, return *their sum as a binary string*.
 * @param {string} a first binary string
 * @param {string} b second binary string
 * @returns {string} the sum of the binary strings
 */
var addBinary = function (a, b) {
    let sum = "";

    let n = a.length > b.length ? a.length : b.length; // number of calculations
    let i = a.length - 1; // pointer to current place value in a
    let j = b.length - 1; // pointer to current place value in b

    let carry = "0"; // the carry over value from the previous calculations

    // To sum two binary numbers, begin with the rightmost (least significant)
    // bit of each number. Add the values according to the following rules:
    //      all zeros     = 0 with carry of 0
    //      a single one  = 1 with carry of 0
    //      two ones      = 0 with carry of 1
    //      three ones    = 1 with carry of 1
    while (n > 0 || carry === "1") {
        // If all of the values of either number have been summed, fill with
        // zeros until all values of both numbers have been summed.
        let aNum, bNum;
        aNum = a[i] ? a[i] : "0";
        bNum = b[j] ? b[j] : "0";

        if (carry === "1" && aNum === "1" && bNum === "1") {
            sum = "1" + sum;
        } else if (aNum === "1" && bNum === "1") {
            sum = "0" + sum;
            carry = "1";
        } else if (carry === "1") {
            if (aNum === "1" || bNum === "1") {
                sum = "0" + sum;
            } else {
                sum = "1" + sum;
                carry = "0";
            }
        } else if (aNum === "1" || bNum === "1") {
            sum = "1" + sum;
        } else {
            sum = "0" + sum;
        }

        n--;
        i--;
        j--;
    }

    return sum;
};

/**
 * Given two binary strings `a` and `b`, return *their sum as a binary string*.
 * @param {string} a first binary string
 * @param {string} b second binary string
 * @returns {string} the sum of the binary strings
 */
var addBinary1 = function (a, b) {
    let i = a.length - 1;   // pointer to current bit in a
    let j = b.length - 1;   // pointer to current bit in b
    let carry = 0;          // the carry over bit from the previous calculation
    let res = "";           // the resulting sum

    while (i >= 0 || j >= 0 || carry) {
        // If `i` or `j` is less than 0, all of the bits for `a` or `b` have been
        // summed. Add leading zeros until all bits for both numbers have been summed.
        const aBit = i >= 0 ? Number(a[i--]) : 0;
        const bBit = j >= 0 ? Number(b[j--]) : 0;

        // Add the bits to get the decimal value for this bit (0 - 3). Divide the
        // sum by two and round down to get the carry (0 or 1). The current result
        // bit is the remander after dividing the sum by 2.
        const sum = carry + aBit + bBit;
        carry = sum >> 1;
        res = (sum % 2) + res;
    }

    return res;
};

module.exports = { addBinary, addBinary1 };
