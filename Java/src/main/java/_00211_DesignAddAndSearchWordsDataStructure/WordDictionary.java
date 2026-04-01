package _00211_DesignAddAndSearchWordsDataStructure;

/**
 * A data structure that supports adding new words and finding if a string
 * matches any previously added string.
 */
public class WordDictionary {

    /** The root TrieNode whose children will be the beginning of words. */
    TrieNode root;

    /**
     * Node that represents a letter in a word.
     */
    private class TrieNode {
        /** Possible next letters after this letter. */
        TrieNode[] children = new TrieNode[26];
        /**
         * {@code true} if this letter is the end of a word or {@code false} otherwise
         */
        boolean isEndOfWord = false;
    }

    /**
     * Initialize the WordDictionary object.
     */
    public WordDictionary() { root = new TrieNode(); }

    /**
     * Add {@code word} to the data structure, it can be matched later.
     * 
     * @param word the word to add
     */
    public void addWord(String word) {
        TrieNode curr = root;

        for (int i = 0; i < word.length(); i++) {
            int childIndex = word.charAt(i) - 'a';
            if (curr.children[childIndex] == null)
                curr.children[childIndex] = new TrieNode();
            curr = curr.children[childIndex];
        }

        curr.isEndOfWord = true;
    }

    /**
     * Return {@code true} if there is any string in the data structure that matches
     * {@code word} or {@code false} otherwise. {@code word} may contain dots
     * {@code '.'} where dots can be matched with any letter.
     * 
     * @param word the word to search for
     * @return {@code true} if the word is found or {@code false} otherwise
     */
    public boolean search(String word) { return search(word, root, 0); }

    /**
     * Search for a word recursively letter by letter.
     * 
     * @param word      the word to search for
     * @param node      the current "letter" that was found
     * @param wordIndex the index of the current letter of the word to find
     * @return {@code true} if the end of the word is found or {@code false}
     *         otherwise
     */
    private boolean search(String word, TrieNode node, int wordIndex) {
        if (wordIndex == word.length()) {
            return node.isEndOfWord;
        }

        int childIndex = word.charAt(wordIndex) - 'a';

        if (word.charAt(wordIndex) == '.') {
            boolean isChild = false;
            for (TrieNode child : node.children) {
                if (child == null)
                    continue;
                isChild = search(word, child, wordIndex + 1);
                if (isChild)
                    return isChild;
            }
            return isChild;
        }

        if (node.children[childIndex] == null)
            return false;

        return search(word, node.children[childIndex], wordIndex + 1);
    }
}
