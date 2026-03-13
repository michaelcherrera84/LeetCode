from typing import List
from collections import Counter, defaultdict


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        """You are given a string `s` and an array of strings `words`. All the
        strings of `words` are of **the same length**.

        A **concatenated string** is a string that exactly contains all the
        strings of any permutation of `words` concatenated.

        - For example, if `words = ["ab","cd","ef"]`, then `"abcdef"`,
        `"abefcd"`, `"cdabef"`, `"cdefab"`, `"efabcd"`, and `"efcdab"` are all
        concatenated stings. `"acdbef"` is not a concatenated string because it
        is not the concatenation of any permutation of `words`.

        Return an array of *the starting indices of all the concatenated
        substrings in `s`. You can return the answer in *any order*.

        Args:
            s (str): the string
            words (List[str]): the list of words

        Returns:
            List[int]: the indices of all the concatenated substings in `s`
        """

        word_len = len(words[0])  # the length of each word
        word_count = len(words)  # the total number of words
        word_freq = Counter(words)  # to number of times each word appears

        subs = []

        # Check all words in a path beggening with each letter in the length of
        # a word.
        for offset in range(word_len):
            left = offset
            seen_rate = defaultdict(int)
            seen_count = 0

            for right in range(left, len(s) - word_len + 1, word_len):
                curr_word = s[right : right + word_len]

                # If the current word is a valid word, keep a count the
                # occurances of this word in the current window.
                if curr_word in word_freq:
                    seen_rate[curr_word] += 1
                    seen_count += 1

                    # If the current word has been seen too many times, this
                    # window isn't a valid substring. Shrink the window until
                    # the window is valid.
                    while seen_rate[curr_word] > word_freq[curr_word]:
                        first_word = s[left : left + word_len]
                        seen_rate[first_word] -= 1
                        seen_count -= 1
                        left += word_len

                    # If count of words we've seen in this window is equal to
                    # the number of words we are looking for, we have found,
                    # a valid subtring. Add the left index to the result `subs`.
                    if seen_count == word_count:
                        subs.append(left)
                        # Shink the window only one word to account for possible
                        # overlaps.
                        first_word = s[left : left + word_len]
                        seen_rate[first_word] -= 1
                        seen_count -= 1
                        left += word_len

                # If the word isn't in words, this window this window is invalid.
                else:
                    seen_rate.clear()
                    seen_count = 0
                    left = right + word_len

        return subs


import unittest


class Test_Solution(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example1(self):
        s = "barfoothefoobarman"
        words = ["foo", "bar"]
        expected = [0, 9]
        actual = self.sol.findSubstring(s, words)
        self.assertEqual(expected, actual)

    def test_example2(self):
        s = "wordgoodgoodgoodbestword"
        words = ["word", "good", "best", "word"]
        expected = []
        actual = self.sol.findSubstring(s, words)
        self.assertEqual(expected, actual)

    def test_example3(self):
        s = "barfoofoobarthefoobarman"
        words = ["bar", "foo", "the"]
        expected = [6, 9, 12]
        actual = self.sol.findSubstring(s, words)
        self.assertEqual(expected, actual)

    def test_not_enough_letters(self):
        s = "a"
        words = ["a", "a"]
        expected = []
        actual = self.sol.findSubstring(s, words)
        self.assertEqual(expected, actual)

    def test_multiple_of_same_word(self):
        s = "aa"
        words = ["a", "a"]
        expected = [0]
        actual = self.sol.findSubstring(s, words)
        self.assertEqual(expected, actual)

    def test_overlap(self):
        s = "foobarfoo"
        words = ["foo", "bar"]
        expected = [0, 3]
        actual = self.sol.findSubstring(s, words)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
