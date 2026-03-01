class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """Given a string `s`, find the length of the *longest substring*
        without duplicate characters.

        Args:
            s (str): the string

        Returns:
            int: the length of the longest substring without duplicate characters
        """

        max_len = 0  # lengh of the longest substring
        lkp = {}  # last known position of each character
        left = 0

        # For each character in `s`, if the character is already in the current
        # substring, shrink the string from the left until the current character
        # is removed. Then, add the character to the right.
        for right in range(len(s)):
            # Shrink the window.
            if s[right] in lkp and lkp[s[right]] >= left:
                left = lkp[s[right]] + 1
                
            # Expand the window.
            lkp[s[right]] = right

            # Update the max length.
            max_len = max(max_len, right - left + 1)

        return max_len
    
import unittest

class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example1(self):
        s = "abcabccbb"
        expected = 3
        actual = self.sol.lengthOfLongestSubstring(s)
        self.assertEqual(expected, actual)

    def test_example2(self):
        s = "bbbbb"
        expected = 1
        actual = self.sol.lengthOfLongestSubstring(s)
        self.assertEqual(expected, actual)

    def test_example3(self):
        s = "pwwkew"
        expected = 3
        actual = self.sol.lengthOfLongestSubstring(s)
        self.assertEqual(expected, actual)

    def test_empty_string(self):
        s = ""
        expected = 0
        actual = self.sol.lengthOfLongestSubstring(s)
        self.assertEqual(expected, actual)

    def test_reverse_repeat(self):
        s = "abbae"
        expected = 3
        actual = self.sol.lengthOfLongestSubstring(s)
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()