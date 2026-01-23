package _14_LongestCommonPrefix;

public class Solution {

    /**
     * Find the longest common prefix string amongst an array of strings.
     *
     * @param strs the array of strings
     * @return the longest common prefix, or {@code ""} is no common prefix is
     * found
     */
    public String longestCommonPrefix(String[] strs) {

        if (strs == null) {
            throw new IllegalArgumentException("The array cannot be null.");
        }

        StringBuilder prefix = new StringBuilder(); // longest prefix between two strings
        String longestCommonPrefix = strs[0];       // longest prefix between all strings       

        // Traverse the array, comparing every string to the first string.
        for (int i = 1; i < strs.length; i++) {
            prefix.setLength(0);                    // resuse the StringBuilder

            // Compare letter for letter until reaching the end of either string or until
            // the letter are not matched. Add each matched letter to the prefix.
            int j = 0;
            while (j < strs[0].length()
                    && j < strs[i].length()
                    && strs[0].charAt(j) == strs[i].charAt(j)) {
                prefix.append(strs[0].charAt(j++));
            }

            // If the current prefix is shorter than the longest common prefix, then
            // the current prefix is the new longest common prefix.
            if (prefix.length() < longestCommonPrefix.length()) {
                longestCommonPrefix = prefix.toString();
            }
        }

        return longestCommonPrefix;
    }

    /**
     * Find the longest common prefix string amongst an array of strings.
     *
     * @param strs the array of strings
     * @return the longest common prefix, or {@code ""} is no common prefix is
     * found
     */
    public String longestCommonPrefix1(String[] strs) {

        if (strs == null || strs.length == 0) {
            return "";
        }

        StringBuilder lcp = new StringBuilder(strs[0]);  // longest common prefix

        // Compare each word to the current longest common prefix.
        for (int i = 1; i < strs.length; i++) {

            // If the current longest common prefix (lcp) is longer than the current
            // word or the complete lcp is not the prefix of the current word,
            // remove a letter from the lcp.
            while (lcp.length() > strs[i].length()
                    || !lcp.toString().equals(strs[i].substring(0, lcp.length()))) {
                lcp.setLength(lcp.length() - 1);
            }

            // If at any point the longest common prefix has no letter
            // we can terminate the loop and return the empty string.
            if (lcp.length() == 0) {
                break;
            }
        }

        return lcp.toString();
    }

    /**
     * Find the longest common prefix string amongst an array of strings.
     *
     * @param strs the array of strings
     * @return the longest common prefix, or {@code ""} is no common prefix is
     * found
     */
    public String longestCommonPrefix2(String[] strs) {

        if (strs == null || strs.length == 0) {
            return "";
        }

        String lcp = strs[0];  // longest common prefix

        // Compare each word to the current longest common prefix.
        for (int i = 1; i < strs.length; i++) {

            // If the current word doesn't start with the longest common prefix
            // (lcp) remove a letter from the lcp.
            while (strs[i].indexOf(lcp) != 0) {
                lcp = lcp.substring(0, lcp.length() - 1);
            }

            // If at any point the longest common prefix has no letter
            // we can terminate the loop and return the empty string.
            if (lcp.isEmpty()) {
                break;
            }
        }

        return lcp;
    }
}
