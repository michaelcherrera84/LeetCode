package _383_RansomNote;

import java.util.HashMap;
import java.util.Map;

public class Solution {

    /**
     * Given two strings {@code ransomNote} and {@code magazine}, return
     * {@code true} <i>if</i> {@code ransomNote} <i>can be constructed by using
     * the letters from</i> {@code magazine} <i>and</i> {@code false}
     * <i>otherwise</i>.
     * <p>
     * Each letter in {@code magazine} can only be used once in
     * {@code ransomNote}.
     *
     * @param ransomNote the ransom note to be constucted
     * @param magazine the magazine from which the letters are obtained
     * @return {@code true} if {@code ransomNote} can be constructed from the
     * letters in {@code magazine}, or {@code false} otherwise
     */
    public boolean canConstruct(String ransomNote, String magazine) {

        if (ransomNote == null || magazine == null) {
            throw new IllegalArgumentException("parameters cannot be null");
        }

        if (ransomNote.isEmpty()) {
            return true;
        }
        if (magazine.isEmpty()) {
            return false;
        }

        // map of magazine letters and their counts
        Map<Character, Integer> letterCount = new HashMap<>();

        // Add each magazine letter, with the number of times it 
        // appears in the magazine, to the map.
        for (int i = 0; i < magazine.length(); i++) {
            char letter = magazine.charAt(i);
            letterCount.put(letter, letterCount.getOrDefault(letter, 0) + 1);
        }

        // Check the map for each letter required by the ransom note.
        for (int i = 0; i < ransomNote.length(); i++) {
            char letter = ransomNote.charAt(i);

            // If the letter was not in the magazine, or no more of this 
            // letter are left, then the ransom note cannot be constructed 
            // from the letters in the magazine. 
            if (letterCount.getOrDefault(letter, 0) == 0) {
                return false;
            } else {  // Otherwise, use a letter (reduce its ramining count).
                letterCount.put(letter, letterCount.get(letter) - 1);
            }
        }

        // If the loop completes without returning false, then the ransom
        // note has been successfully constructed.
        return true;
    }

    /**
     * Given two strings {@code ransomNote} and {@code magazine}, return
     * {@code true} <i>if</i> {@code ransomNote} <i>can be constructed by using
     * the letters from</i> {@code magazine} <i>and</i> {@code false}
     * <i>otherwise</i>.
     * <p>
     * Each letter in {@code magazine} can only be used once in
     * {@code ransomNote}.
     *
     * @param ransomNote the ransom note to be constucted
     * @param magazine the magazine from which the letters are obtained
     * @return {@code true} if {@code ransomNote} can be constructed from the
     * letters in {@code magazine}, or {@code false} otherwise
     */
    public boolean canConstruct1(String ransomNote, String magazine) {

        /* The Problem constraits guarantee the input will be valid
            
            if (ransomNote == null || magazine == null) {
                throw new IllegalArgumentException("parameters cannot be null");
            }

            if (ransomNote.isEmpty()) {
                return true;
            }
            if (magazine.isEmpty()) {
                return false;
            }
            
         */
        int[] letterCount = new int[26];

        // Store the count of each letter in the magazine in the array
        // where each index represents a letter of the alphabet.
        for (char letter : magazine.toCharArray()) {
            letterCount[letter - 'a']++;
        }

        // Check the array for each letter required by the ransom note.
        for (char letter : ransomNote.toCharArray()) {

            // If the letter was not in the magazine, or no more of this 
            // letter are left, then the ransom note cannot be constructed 
            // from the letters in the magazine. 
            if (letterCount[letter - 'a'] == 0) {
                return false;
            }

            // Otherwise, use a letter (reduce its ramining count).
            letterCount[letter - 'a']--;
        }

        // If the loop completes without returning false, then the ransom
        // note has been successfully constructed.
        return true;
    }
}
