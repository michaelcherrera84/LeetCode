from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        Given `n` pairs of parentheses, write a function to *generate all
        combinations of well-formed parentheses*.

        Args:
            n (int): number of pairs of parentheses to generate

        Returns:
            List[str]: list of all combinations of well-formed parentheses
        """

        res = []

        def find_combos(left, right, combo):
            """
            Find combos recursively.

            Args:
                left (int): the number of left parentheses in this combo
                right (int): the number of right parentheses in this combo
                combo (str): a parentheses combination
            """

            # If the combo has the correct number of parentheses, add the combo.
            if len(combo) == n * 2:
                res.append(combo)
                return

            # If there are still left parentheses to add, add one.
            if left < n:
                find_combos(left + 1, right, combo + "(")

            # If there are fewer right parentheses than left, add a right.
            if right < left:
                find_combos(left, right + 1, combo + ")")

        find_combos(0, 0, "")

        return res


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example1(self):
        n = 3
        expected = ["((()))", "(()())", "(())()", "()(())", "()()()"]
        actual = self.sol.generateParenthesis(n)
        self.assertCountEqual(expected, actual)

    def test_example2(self):
        n = 1
        expected = ["()"]
        actual = self.sol.generateParenthesis(n)
        self.assertCountEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
