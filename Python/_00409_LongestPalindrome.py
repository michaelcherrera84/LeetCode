

from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        """Given a string `s` which consists of lowercase or uppercase letters, 
        return the length of the **longest** palindrome that can be built with 
        those letters.

        Letters are **case sensitive**, for example, `"Aa"` is not considered a 
        palindrome.

        Args:
            s (str): the string

        Returns:
            int: the length of the longest palindrome
        """

        # Count the frequency of each letter in the string.
        letter_freq = Counter(s)
        odd = False
        res = 0

        # Count doubles for each letter in the string.
        for freq in letter_freq.values():
            res += (freq // 2) * 2
            # There can be one lone letter in an odd length palindome, so we
            # note if there are any letters that have an odd count.
            if freq % 2:
                odd = True

        if odd:
            res += 1
        
        return res
    
import unittest

class Test_Solution(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example1(self):
        s = "abccccdd"
        expected = 7
        actual = self.sol.longestPalindrome(s)
        self.assertEqual(expected, actual)

    def test_example2(self):
        s = "a"
        expected = 1
        actual = self.sol.longestPalindrome(s)
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()