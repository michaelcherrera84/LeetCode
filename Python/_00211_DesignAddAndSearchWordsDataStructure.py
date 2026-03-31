class WordDictionary:
    """
    A data structure that supports adding new words and finding if a string
    matches any previously added string.
    """

    class TrieNode:
        """
        Node that represents a letter in a word.
        """

        def __init__(self) -> None:
            """
            Initialize the TrieNode object
            """

            self.children: list[WordDictionary.TrieNode | None] = [None] * 26
            """Represents possible next letters after this letter"""
            self.is_end_of_word: bool = False
            """`True` is this letter is the end of a word or `False` otherwise"""

    def __init__(self):
        """
        Initialize the WordDictionary object
        """

        self.root = WordDictionary.TrieNode()
        """The root TrieNode whose children will be the beginning of words"""

    def addWord(self, word: str) -> None:
        """
        Add `word` to the data structure, it can be matched later.

        Args:
            word (str): the word to add
        """

        curr = self.root

        for c in word:
            child_index = ord(c) - ord("a")
            if curr.children[child_index] is None:
                curr.children[child_index] = WordDictionary.TrieNode()
            curr = curr.children[child_index]

        curr.is_end_of_word = True

    def search(self, word: str) -> bool:
        """
        Return `True` if there is any string in the data structure that matches
        `word` or `False` otherwise. `word` may contain dots `'.'` where dots
        can by matched with any letter.

        Args:
            word (str): the word to search for

        Returns:
            bool: `True` if the word is found or `False` otherwise
        """

        def dfs(node, i):
            """
            Search for a word letter by letter.

            Args:
                node (WordDictionary.TrieNode): the current letter
                i (int): the current letter of the word to search for

            Returns:
                bool: `True` if we find the word or `False` otherwise
            """

            if i == len(word):
                return node.is_end_of_word

            child_index = ord(word[i]) - ord("a")
            if word[i] == ".":
                return any(dfs(child, i + 1) for child in node.children if child)
            if node.children[child_index] is None:
                return False
            return dfs(node.children[child_index], i + 1)

        return dfs(self.root, 0)


import unittest


class TestWordDictionary(unittest.TestCase):
    def test_example1(self):
        wordDictionary = WordDictionary()
        wordDictionary.addWord("bad")
        wordDictionary.addWord("dad")
        wordDictionary.addWord("mad")
        self.assertFalse(wordDictionary.search("pad"))
        self.assertTrue(wordDictionary.search("bad"))
        self.assertTrue(wordDictionary.search(".ad"))
        self.assertTrue(wordDictionary.search("b.."))


if __name__ == "__main__":
    unittest.main()
