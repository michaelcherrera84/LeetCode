package _290_WordPattern;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

public class Solution {

    /**
     * Given a {@code pattern} and a string {@code s}, find if {@code s} follows
     * the same pattern.
     * <p>
     * Here <b>follow</b> means a full match, such that there is a bijection
     * between a letter in {@code pattern} and a <b>non-empty</b> word in
     * {@code s}.
     * <p>
     * Specifically:
     * <ul>
     * <li>Each letter in {@code pattern} maps to <b>exactly</b> one unique word
     * in {@code s}.</li>
     * <li>Each unique word in {@code s} maps to <b>exactly</b> one letter in
     * {@code pattern}.</li>
     * <li>No two letters map to the same word, and no two words map to the same
     * letter.</li>
     * </ul>
     *
     * @param pattern the pattern
     * @param s the string to check for a patter match
     * @return {@code true} if {@code s} follows the {@code pattern}, or
     * {@code false} otherwise
     */
    public boolean wordPattern(String pattern, String s) {
        String[] sWords = s.split(" ");  // array of words in `s`

        // If the number of letters in `pattern` is not equal to the number of 
        // words in `s`, the string does not follow the pattern.
        if (pattern.length() != sWords.length) {
            return false;
        }

        // mapping of letters in `pattern` to the corresponding words in `s`
        Map<Character, String> letterWordMap = new HashMap<>();

        // set of mapped words in `s` (note: this is faster to search than 
        // searching values in the map)
        Set<String> usedWords = new HashSet<>();

        // Check the mappings for each letter in `pattern` and word in `s`.
        for (int i = 0; i < pattern.length(); i++) {
        
            Character patterLetter = pattern.charAt(i); // current letter in `pattern`
            String sWord = sWords[i];                   // current word in `s`

            // If the current letter in `pattern` is already mapped...
            if (letterWordMap.containsKey(patterLetter)) {
                
                // If the letter is not mapped to the current word in `s`, then 
                // the string does not follow the pattern.
                if (!letterWordMap.get(patterLetter).equals(sWord)) {
                    return false;
                }
            } else {  // the current letter in 'pattern' is not mapped.

                // If the currenet word in `s` is mapped, then the string does 
                // not follow the pattern.
                if (usedWords.contains(sWord)) {
                    return false;
                }

                // Add the letter to word mapping.
                letterWordMap.put(patterLetter, sWord);

                // Add the word to the already used words.
                usedWords.add(sWord);
            }
        }

        // If the loop completes without returning false, then the string 
        // follows the pattern.
        return true;
    }
}
