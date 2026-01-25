package _00058_LengthOfLastWord;

public class Solution {

    /**
     * Given a string {@code s} consisting of words and spaces, return <i>
     * the length of the <b>last</b> word in the string.</i>
     * <p>
     * A <b>word</b> is a maximal substring consisting of non-space characters
     * only.
     *
     * @param s the string consisting of words and spaces
     * @return the length of the last word in the string
     */
    public int lengthOfLastWord(String s) {
        boolean foundWord = false;  // true once a letter is found
        int length = 0;             // the lenght of the final word

        // Traverse the string from the end. The string could end in spaces,
        // so foundWord is used to indicate we have located an actual word.
        for (int i = s.length() - 1; i >= 0; i--) {

            // If the character is not a space (' '), then the character
            // is a letter in the last word.
            if (s.charAt(i) != ' ') {
                foundWord = true;
                length++;
            }

            // Once a the last word is found, the next space marks the end
            // of the word. The loop can terminate.
            if (s.charAt(i) == ' ' && foundWord) {
                break;
            }
        }

        return length;
    }
}
