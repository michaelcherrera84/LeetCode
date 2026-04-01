from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        Given a string containing digits from `2-9` inclusive, return all
        possible letter combinations that the number could represent. Return the
        answer in **any order**.

        A mapping of digits to letters (just like on the telephone buttons) is
        given below. Note that 1 does not map to any letters.

        ```
        1        2 abc    3 def
        4 ghi    5 jkl    6 mno
        7 pqrs   8 tuv    9 wxyz
                 0  ␣
        ```

        Args:
            digits (str): the string of digits from 2-9 inclusive

        Returns:
            List[str]: all possible letter combinations that the number could
            represent
        """

        if not digits:
            return []

        # map of digits to letters
        mapping = {
            "0": " ",
            "1": "",
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        combos = []

        def find_combinations(digits, i, combo):
            """
            Build the combonations list.

            Args:
                digits (str): the digits 
                i (int): index of the current digit
                combo (str): current combination
            """

            if i == len(digits):
                combos.append(combo)
                return

            # For each letter associated with this digit, append each possible
            # next letter recursively.
            for c in mapping[digits[i]]:
                find_combinations(digits, i + 1, combo + c)

        find_combinations(digits, 0, "")

        return combos


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example1(self):
        digits = "23"
        expected = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
        actual = self.sol.letterCombinations(digits)
        self.assertCountEqual(expected, actual)

    def test_example2(self):
        digits = "2"
        expected = ["a", "b", "c"]
        actual = self.sol.letterCombinations(digits)
        self.assertCountEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
