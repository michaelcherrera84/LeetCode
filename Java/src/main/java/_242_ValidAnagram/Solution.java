package _242_ValidAnagram;

public class Solution {

    /**
     * Given two strings {@code s} and {@code t}, return {@code true} if
     * {@code t} is an anagram of {@code s}, and {@code false} otherwise.
     *
     * @param s the first string
     * @param t the second string
     * @return {@code true} is the strings are anagrams of one another, or
     * {@code false} otherwise
     */
    public boolean isAnagram(String s, String t) {

        // Strings of unequal length are not anagrams.
        if (s.length() != t.length()) {
            return false;
        }

        int[] sLetters = new int[26];    // count of letters in `s`
        int[] tLetters = new int[26];    // count of letters in `t`

        // Count each letter in both strings.
        for (int i = 0; i < s.length(); i++) {

            sLetters[s.charAt(i) - 'a']++;  // Add to count of current letter in `s`.
            tLetters[t.charAt(i) - 'a']++;  // Add to count of current letter in `t`.
        }

        // Compare the counts of the letters in both strings.
        for (int i = 0; i < sLetters.length; i++) {

            // If the counts are not equal, the stings are not anagrams.
            if (sLetters[i] != tLetters[i]) {
                return false;
            }
        }

        // If the previous loops does not return false, then the strings are anagrams.
        return true;
    }
}
