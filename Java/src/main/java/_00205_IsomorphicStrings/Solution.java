package _00205_IsomorphicStrings;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

public class Solution {

    /**
     * Given two strings {@code s} and {@code t}, <i>determine if they are
     * isomorphic</i>.
     * <p>
     * The two strings are isomorphic if the characers in {@code s} can be
     * replced to get {@code t}.
     * <p>
     * All occurrences of a character must be replaced with another
     * character while preserving the order of characters. No two characters
     * may map to the same character, but a character may map to itself.
     *
     * @param s the first string
     * @param t the second string
     * @return {@code true} if {@code s} and {@code t} are isomorphic, or
     * {@code false} otherwise
     */
    @SuppressWarnings({"BoxedValueEquality", "NumberEquality"})
    public boolean isIsomorphic(String s, String t) {

        // mapping of letters from `s` to `t`.
        Map<Character, Character> letterMapping = new HashMap<>();

        // set of letter in `t`.
        Set<Character> tLetters = new HashSet<>();

        // Traverse `s`...
        for (int i = 0; i < s.length(); i++) {
            Character sLetter = s.charAt(i);  // current letter in s
            Character tLetter = t.charAt(i);  // current letter in t

            // If the current letter in `s` is already mapped to a letter in `t`.
            if (letterMapping.containsKey(sLetter)) {

                // If the mapping is not the same as the current letter in
                // `t`, then the strings are not isomorphic.
                if (letterMapping.get(sLetter) != tLetter) {
                    return false;
                }
            } else {
                // If the current letter in `s` is not mapped, but the 
                // current letter in `t` is already mapped, the strings
                // are not isomorphic.
                if (tLetters.contains(tLetter)) {
                    return false;
                }

                // Otherwise, add the mapping from the current letter in `s`
                // to the current letter in `t` and add the current letter
                // in `t` to the set of mapped letters from `t`.
                letterMapping.put(sLetter, tLetter);
                tLetters.add(tLetter);
            }
        }

        // If thet loop completes without returning false, the words are isomorphic.
        return true;
    }

    /**
     * Given two strings {@code s} and {@code t}, <i>determine if they are
     * isomorphic</i>.
     * <p>
     * The two strings are isomorphic if the characers in {@code s} can be
     * replced to get {@code t}.
     * <p>
     * All occurrences of a character must be replaced with another
     * character while preserving the order of characters. No two characters
     * may map to the same character, but a character may map to itself.
     *
     * @param s the first string
     * @param t the second string
     * @return {@code true} if {@code s} and {@code t} are isomorphic, or
     * {@code false} otherwise
     */
    public boolean isIsomorphic1(String s, String t) {

        /* The problem constraints guarantee this will not happen
        if (s.length() != t.length()) {
            return false;
        }
        */

        // Each index represents an ASCII character
        int[] sLetters = new int[256];  // indices of letters in `s`
        int[] tLetters = new int[256];  // indices of letters in `t` 

        // Traverse the strings together...
        for (int i = 0; i < s.length(); i++) {
            char sLetter = s.charAt(i);  // current letter in `s`
            char tLetter = t.charAt(i);  // current letter in `t`
            
            // If either array has a value other than 0 at the postion 
            // corresponding to the current letter, then that letter has already 
            // been mapped. If the values (indices in their respective strings) 
            // do not match, then the strings are not isomorphic.
            if (sLetters[sLetter] != tLetters[tLetter]) {
                return false;
            }

            // Add the current letter position to the appropriate character 
            // position of each array.
            sLetters[sLetter] = i + 1;
            tLetters[tLetter] = i + 1;
        }

        return true;
    }
}
