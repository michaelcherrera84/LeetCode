from typing import List
from collections import defaultdict


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        Given a string `s` and a dictionary of strings `wordDict`, return `true`
        if `s` can be segmented into a space-separated sequence of one or more
        dictionary words.

        **Note** that the same word in the dictionary may be reused multiple
        times in the segmentation.

        **Approach:** Trie + DP (right-to-left)
        - Build a Trie from wordDict for efficient prefix matching.
        - Use a DP array where dp[i] = True means s[i:] can be segmented.
        - Iterate right-to-left; at each index, walk the Trie over s[i:] and 
        mark dp[i] = True if we land on a complete word whose suffix is also 
        segmentable (dp[j+1] is True).

        Time:  O(n * max_len)  — n start positions, each walks at most max_len
                                 Trie edges.
        Space: O(W * L + n)    — Trie holds all characters of wordDict (W words,
                                 avg length L); DP array is length n + 1.

        Args:
            s (str): a string containing dictionary words
            wordDict (List[str]): the dictionary of words

        Returns:
            bool: `True` if `s` can be segmented into a space-separated sequence
            of one or more dictionary words.
        """

        class TrieNode:
            def __init__(self) -> None:
                """
                A single node in the Trie.

                Attributes:
                    is_word (bool): True if this node marks the end of a valid
                                    dictionary word.
                    child (defaultdict): Maps each character to the next TrieNode,
                                         auto-creating a node when a new character
                                         is first seen.
                """
                self.is_word = False
                self.child = defaultdict(TrieNode)

            def addWord(self, word: str) -> None:
                """
                Insert `word` into the Trie rooted at this node.
                Traverses (creating nodes as needed) one character at a time,
                then marks the final node as a complete word.
                """
                curr = self
                for c in word:
                    curr = curr.child[c]   # Advance to (or create) the child node for c
                curr.is_word = True        # Mark the terminal character of the word

        # Build the Trie from every word in the dictionary
        root = TrieNode()
        for word in wordDict:
            root.addWord(word)

        max_len = max(len(w) for w in wordDict)  # Caps inner loop; no word can exceed this
        n = len(s)

        # dp[i] = True means s[i:] can be fully segmented into dictionary words.
        # Base case: an empty suffix (i == n) is trivially segmentable.
        dp = [False] * (n + 1)
        dp[n] = True

        # Fill the DP table from right to left so that dp[j+1] is already
        # computed when we evaluate position i.
        for i in range(n - 1, -1, -1):
            curr = root  # Always start each search from the Trie root

            # Extend the current match one character at a time, but never
            # longer than the longest dictionary word (no match could exist).
            for j in range(i, min(i + max_len, n)):
                c = s[j]

                if c not in curr.child:
                    break             # No dictionary word continues with this character

                curr = curr.child[c]  # Descend into the Trie along character c

                # s[i..j] is a complete dictionary word AND the remainder s[j+1:]
                # is also segmentable — so s[i:] can be segmented.
                if curr.is_word and dp[j + 1]:
                    dp[i] = True
                    break

        # dp[0] tells us whether the entire string s[0:] is segmentable.
        return dp[0]

import unittest


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example1(self):
        s = "leetcode"
        wordDict = ["leet", "code"]
        self.assertTrue(self.sol.wordBreak(s, wordDict))

    def test_example2(self):
        s = "applepenapple"
        wordDict = ["apple", "pen"]
        self.assertTrue(self.sol.wordBreak(s, wordDict))

    def test_example3(self):
        s = "catsandog"
        wordDict = ["cats", "dog", "sand", "and", "cat"]
        self.assertFalse(self.sol.wordBreak(s, wordDict))


if __name__ == "__main__":
    unittest.main()
