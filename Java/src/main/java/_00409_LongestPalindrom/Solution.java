package _00409_LongestPalindrom;

public class Solution {

    /**
     * Given a string {@code s} which consists of lowercase or uppercase letters,
     * return the length of the <b>longest</b> palindrome that can be built with
     * those letters.
     *
     * Letters are <b>case sensitive</b>, for example, {@code "Aa"} is not
     * considered a palindrome.
     * 
     * @param s the string
     * @return the length of the longest palindrome
     */
    public int longestPalindrome(String s) {

        int[] freq = new int[123];
        int res = 0; // lengh of the longest palindrom

        // Count the occurances of each letter in the string.
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            freq[c]++;
            // For every two occurances we can increment the result by two.
            if (freq[c] % 2 == 0)
                res += 2;
        }

        // If the result is less than the length of the string, then there is at
        // least one lone letter that can be at the center of the palindrome.
        if (res < s.length())
            res++;
        
        return res;
    }
}
