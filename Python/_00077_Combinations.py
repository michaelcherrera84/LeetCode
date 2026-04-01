from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        """
        Given two integers `n` and `k`, return *all possible combinations of*
        `k` *numbers chosen from the range* `[1, n]`.

        Return the answer in **any order**.

        Args:
            n (int): upper end of the combination range
            k (int): combination size

        Returns:
            List[List[int]]: a list of all possible combination lists
        """

        res = []

        def find_combos(start, combo):
            """
            Build the combination list but appending numbers until the desired
            length is reached and then backtracking to the previous length to
            appeand the rest of the possible numbers.

            Args:
                start (int): the start number for each loop
                combo (list[int]): the current combination
            """

            # If a combination is the desired length, append it to the result
            # list and return to the previous length.
            if len(combo) == k:
                res.append(combo[:])
                return
            
            for num in range(start, n + 1):
                combo.append(num)
                find_combos(num + 1, combo)
                combo.pop()

        find_combos(1, [])

        return res


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example1(self):
        n = 4
        k = 2
        expected = [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
        actual = self.sol.combine(n, k)
        self.assertEqual(set(map(tuple, expected)), set(map(tuple, actual)))

    def test_example2(self):
        n = 1
        k = 1
        expected = [[1]]
        actual = self.sol.combine(n, k)
        self.assertEqual(set(map(tuple, expected)), set(map(tuple, actual)))

if __name__ == "__main__":
    unittest.main()
