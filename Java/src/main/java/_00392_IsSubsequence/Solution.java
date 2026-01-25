package _00392_IsSubsequence;

public class Solution {

    /**
     * Given two strings {@code s} and {@code t}, return {@code true}
     * <i>if</i> {@code s} <i>is a <b>subsequence</b> of</i> {@code t},
     * <i>or</i> {@code false} <i>otherwise</i>.
     *
     * @param s the proposed subsequence
     * @param t the text
     * @return true if {@code s} is a subsequence of {@code t}, or {@code false}
     * otherwise
     */
    public boolean isSubsequence(String s, String t) {

        int i = 0;  // point to the start of s
        int j = 0;  // point to the start of t

        // Treverse both strings together.
        while (i < s.length() && j < t.length()) {

            // If the current letters are equal, advance to the next letter 
            // in the proposed subsequence (i).
            if (s.charAt(i) == t.charAt(j)) {
                i++;
            }
            // Always advance to the next letter of the text (j).
            j++;
        }

        // If I has reached the end of the proposed subsequence, then the 
        // subsequence is confirmed.
        return i == s.length();
    }
}
