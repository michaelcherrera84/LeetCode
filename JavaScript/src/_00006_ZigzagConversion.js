/**
 * The string `"PAYPALISHIRING"` is written in a zigzag pattern on a given
 * number of rows like this:
 * ```
 * P   A   H   N
 * A P L S I I G
 * Y   I   R
 * ```
 * And then read line by line: `"PAHNAPLSIIGYIR"`
 * Write the code that will take a string and make this converstion given a
 * number of rows.
 * @param {string} s the input string
 * @param {number} numRows the number of rows
 * @return {string} the converted string
 */
var convert1 = function (s, numRows) {
    // If there is only 1 row, or as many rows as characters, then there is no
    // zigzag. The string does not need to be converted.
    if (numRows === 1 || numRows >= s.length) return s;

    // an array (rows) of arrays (characters)
    const rows = Array.from({ length: numRows }, () => []);

    let direction = false; // true = down, false = up
    // For each character in the string, add it to it proper row.
    for (let i = 0, j = 0; i < s.length; i++) {
        // If we're on the first or last row, change directions.
        if (j === 0 || j === numRows - 1) direction = !direction;

        rows[j].push(s[i]); // Push the character into the current row's array.

        // Move up or down.
        if (direction) j++;
        else j--;
    }

    // Map off the rows to join the inner arrays, the join the rows.
    return rows.map((row) => row.join("")).join("");
};

/**
 * The string `"PAYPALISHIRING"` is written in a zigzag pattern on a given
 * number of rows like this:
 * ```
 * P   A   H   N
 * A P L S I I G
 * Y   I   R
 * ```
 * And then read line by line: `"PAHNAPLSIIGYIR"`
 * Write the code that will take a string and make this converstion given a
 * number of rows.
 * @param {string} s the input string
 * @param {number} numRows the number of rows
 * @return {string} the converted string
 */
var convert = function (s, numRows) {
    // If there is only 1 row, or as many rows as characters, then there is no
    // zigzag. The string does not need to be converted.
    if (numRows === 1 || numRows >= s.length) return s;

    let res = "";
    const cycleLen = 2 * numRows - 2; // length of a full cycle top to top.

    // For each row...
    for (let row = 0; row < numRows; row++) {
        // Find the characters by skipping through the string by the cycle length.
        for (let i = 0; i + row < s.length; i += cycleLen) {
            let sPos = i + row; // current postion in the string

            // Add the first character at the current position for this cycle.
            res += s[sPos]; 

            // If the current row is not the top or bottom row, then there are
            // two chacters per cycle.
            if (row !== 0 && row !== numRows - 1) {
                sPos = i + cycleLen - row;

                // If we haven't reached the end of the string, add the second 
                // character at the current position for this cycle.
                if (sPos < s.length) {
                    res += s[sPos];
                }
            }
        }
    }

    return res;
};

module.exports = convert;
