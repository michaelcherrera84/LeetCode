package _00028_FindTheIndexOfTheFirstOccurrenceInAString;

public class Solution {

    /**
     * Given two strings {@code needle} and {@code haystack}, return the index
     * of the first occurrence of {@code needle} in {@code haystack}, or
     * {@code -1} if {@code needle} is not part of {@code haystack}.
     *
     * @param haystack the string to search
     * @param needle the string to seach for
     * @return the index of {@code needle} in {@code haystack}, or -1 if
     * {@code needle} is not in {@code haystack}
     */
    public int strStr(String haystack, String needle) {

        if (haystack.isEmpty() || needle.isEmpty()) {
            return -1;
        }

        int[] lps = longestPrefixSuffix(needle);

        // For each letter in haystrack, beginning at the start of both strings...
        for (int i = 0, j = 0; i < haystack.length(); i++) {

            // if the current letters match, advance to the next letter
            // of both strings.
            if (haystack.charAt(i) == needle.charAt(j)) {
                // If we reach the end of needle, return the position in
                // haystack found by subtracting the length of needle from
                // the next position in haystack. 
                if (++j == needle.length()) {
                    return i + 1 - j;
                }
            } else {
                // Otherwise, if not on the first letter of needle, refer to 
                // the lps array to see how far back in needle we can jump 
                // without missing potential matches. 
                if (j != 0) {
                    j = lps[j - 1];
                    i--;
                }
            }
        }

        return -1;
    }

    /**
     * Contruct an array where each index represets the a position in a given
     * string. Each element stores the length of a prefix that is also a suffix
     * of the substring ending at that position.
     *
     * @param s the given string
     * @return an array of longest prefixes that are also suffixes of substrings
     * that end at the corresponding index in {@code s};
     */
    public int[] longestPrefixSuffix(String s) {
        int[] lps = new int[s.length()];
        lps[0] = 0;  // the first 1-letter substring has no prefix/suffix.

        // For each letter in the string s beginning at the second letter...
        for (int i = 1, j = 0; i < s.length(); i++) {

            // if the current letter (a position in a suffix) is equal to
            // the corresponding letter in the prefix increment the prefix
            // length and store the lenth at this position in the array.
            if (s.charAt(i) == s.charAt(j)) {
                lps[i] = ++j;
            } else {
                // otherwise, if we are not on the first letter of the prefix
                // (length > 0), reduce the lengh of the prefix by 1 and check,
                // the current suffix position again to see if it matches a
                // shorter prefix.
                if (j != 0) {
                    j = lps[j - 1];
                    i--;
                } //If it is the first letter of the pefix that does not, store 
                // a 0 for this position and continue to the next position.
                else {
                    lps[i] = 0;
                }
            }
        }

        return lps;
    }
}
