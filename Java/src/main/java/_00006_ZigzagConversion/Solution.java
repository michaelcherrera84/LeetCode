package _00006_ZigzagConversion;

public class Solution {

    /**
     * The string {@code "PAYPALISHIRING"} is written in a zigzag pattern on a
     * given number of rows like this:
     * <pre>
     * P   A   H   N
     * A P L S I I G
     * Y   I   R
     * </pre> And then read line by line: {@code "PAHNAPLSIIGYIR"} Write the
     * code that will take a string and make this converstion given a number of
     * rows.
     *
     * @param s the input string
     * @param numRows the number of rows
     * @return the converted string
     */
    public String convert(String s, int numRows) {
        var len = s.length();

        // If there is only one row, or there are as many rows as there are 
        // characters, then no zigzag is possible. 
        if (numRows == 1 || len <= numRows) {
            return s;
        }

        var res = new StringBuilder();
        // full cycle (first row to first row) in `s`
        var cycleLen = 2 * numRows - 2;

        // For earch row...
        for (int row = 0; row < numRows; row++) {
            // skip from character to character by advancing cycle lengths.
            for (int i = 0; i + row < len; i += cycleLen) {
                var pos = i + row;  // current position in `s`
                // Add the first character (current position in `s`) in this 
                // cycle to the result.
                res.append(s.charAt(pos));

                // If this is not the first or last row, then there are two
                // characters in this cycle.
                if (row != 0 && row != numRows - 1) {
                    pos = i + cycleLen - row;  // position of second character

                    // If we haven't reached the end of `s`
                    if (pos < len) {
                        res.append(s.charAt(pos));  // Add the second character
                    }
                }
            }
        }

        return res.toString();
    }
}
