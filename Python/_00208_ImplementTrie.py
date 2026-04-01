class Trie:
    """
    A trie (pronounced as "try") or **prefix tree** is a tree data structure
    used to efficiently store and retrieve keys in a dataset of strings. There
    are various applications of this data structure, such as autocomplete and
    spellchecker.
    """

    class _TrieNode:
        """
        Node representing a character.

        Attributes:
            children (dict): list of characters that can immediately follow 
                this character
            isEndOfWord (bool): `True` is this character is the end of a word or
                `False` otherwise

        """
        def __init__(self):
            self.children: dict = {}
            self.isEndOfWord: bool = False


    def __init__(self):
        """
        Initialize the trie object.
        """
        self.root = Trie._TrieNode()

    def insert(self, word: str) -> None:
        """
        Insert the string `word` into the trie.

        Args:
            word (str): the string to insert
        """
        curr = self.root

        for c in word:
            if c not in curr.children:
                new_node = Trie._TrieNode()
                curr.children[c] = new_node

            curr = curr.children[c]

        curr.isEndOfWord = True

    def search(self, word: str) -> bool:
        """
        Returns `True` if the string `word` is in the trie (i.e., was inserted
        before), and `False` otherwise.

        Args:
            word (str): the string to search for

        Returns:
            bool: `True` if the string `word` is in the trie or `False` otherwise.
        """

        curr = self.root

        for c in word:
            if c not in curr.children:
                return False

            curr = curr.children[c]

        return curr.isEndOfWord

    def startsWith(self, prefix: str) -> bool:
        """
        Returns `True` if there is a previously inserted string `word` that has
        the prefix `prefix`, and `false` otherwise.

        Args:
            prefix (str): the string prefix to search for

        Returns:
            bool: `True` if there is a string with the `prefix` or `False`
            otherwise
        """

        curr = self.root

        for c in prefix:
            if c not in curr.children:
                return False

            curr = curr.children[c]

        return True


import unittest


class TestTrie(unittest.TestCase):
    def test_example1(self):
        trie = Trie()
        trie.insert("apple")
        self.assertTrue(trie.search("apple"))
        self.assertFalse(trie.search("app"))
        self.assertTrue(trie.startsWith("app"))
        trie.insert("app")
        self.assertTrue(trie.search("app"))

if __name__ == "__main__":
    unittest.main()
