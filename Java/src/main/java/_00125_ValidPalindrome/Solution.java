package _00125_ValidPalindrome;

public class Solution {

    /**
     * Given a string {@code s}, return {@code true} <i>if it is a
     * <b>palindrome</b>, or</i> {@code false} <i>otherwise</i>.
     * <p>
     * A phrase is a <b>palindrome</b> if, after converting all uppercase
     * letters into lowecase letters and removing all non-alphanumeric
     * characters, it reads the same forward and backward. Alphanumeric
     * characters include letters and numbers.
     *
     * @param s the given string
     * @return {@code true} is {@code s} is a palindrome of {@code false} if
     * {@code s} is not a palindrome
     */
    public boolean isPalindrome(String s) {

        int i = 0;                  // point to the start of the string
        int j = s.length() - 1;     // point to the end of the string

        // Travese the string in both directions until pointer meet.
        while (i <= j) {

            /* 1. Skip spaces and non-alphanumeric characters */
            // If the character at i is not alphanumeric, advance i and continue.
            if (!Character.isLetterOrDigit(s.charAt(i))) {
                i++;
                continue;
            }
            // If the character at j is not alphanumeric, advance j and continue.
            if (!Character.isLetterOrDigit(s.charAt(j))) {
                j--;
                continue;
            }

            /* 2. Compare letters after skipping non-alphanumeric characters */
            // If the letters at i and j are not equal, the string is NOT a palindrome.
            if (Character.toLowerCase(s.charAt(i)) != Character.toLowerCase(s.charAt(j))) {
                return false;
            }

            i++;
            j--;
        }

        // If the loop completes without terminating early, the string is a palindrome.
        return true;
    }

    /**
     * Given a string {@code s}, return {@code true} <i>if it is a
     * <b>palindrome</b>, or</i> {@code false} <i>otherwise</i>.
     * <p>
     * A phrase is a <b>palindrome</b> if, after converting all uppercase
     * letters into lowecase letters and removing all non-alphanumeric
     * characters, it reads the same forward and backward. Alphanumeric
     * characters include letters and numbers.
     *
     * @param s the given string
     * @return {@code true} is {@code s} is a palindrome of {@code false} if
     * {@code s} is not a palindrome
     */
    public boolean isPalindrome1(String s) {

        // Normalse the string, removing non-alphanumeric characters, 
        // and lower casing what is left.
        String cleaString = s.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();

        // Traverse the normalized string from both ends. If at any point 
        // the letters don't match, the string is not a palindrome.
        for (int i = 0, j = cleaString.length() - 1; i <= j; i++, j--) {
            if (cleaString.charAt(i) != cleaString.charAt(j)) {
                return false;
            }
        }

        // If the loops completes without return false, the string 
        // is a palindrome.
        return true;
    }
}
