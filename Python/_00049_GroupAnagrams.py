from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """Given an array of strings `strs`, group the anagrams together.

        Args:
            strs (List[str]): the array of strings

        Returns:
            List[List[str]]: array containing arrays of anagrams
        """

        groups = defaultdict(list)

        # Add each string in `strs` to the appropriate list. 
        for str in strs:
            # Sort the letters in the string to use as the key for the 
            # anagram group.
            letters = "".join(sorted(str))
            groups[letters].append(str)

        return list(groups.values())


import unittest


class Test_Solution(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def normalize(self, groups):
        """
        Convert list-of-lists into a sorted structure
        so order does not matter.
        """
        return sorted([sorted(group) for group in groups])

    def test_example1(self):
        strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
        expected = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
        actual = self.sol.groupAnagrams(strs)
        self.assertEqual(self.normalize(expected), self.normalize(actual))

    def test_example2(self):
        strs = [""]
        expected = [[""]]
        actual = self.sol.groupAnagrams(strs)
        self.assertEqual(self.normalize(expected), self.normalize(actual))

    def test_example3(self):
        strs = ["a"]
        expected = [["a"]]
        actual = self.sol.groupAnagrams(strs)
        self.assertEqual(self.normalize(expected), self.normalize(actual))

if __name__ == "__main__":
    unittest.main()
