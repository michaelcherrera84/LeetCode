from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Given an array of **distinct** integers `candidates` and a target
        integer `target`, return *a list of all **unique combinations** of*
        `candidates` *where the chosen numbers sum to* `target`. You may return
        the combinations in **any order**.

        The **same** number may be chosen from `candidates` an **unlimited
        number of times**. Two combinations are unique if the frequency of at
        least one of the chosen numbers is different.

        The test cases are generated such that the number of unique combinations
        that sum up to `target` is less than `150` combinations for the given
        input.

        Args:
            candidates (List[int]): "array" of distinct integers to use to find
                sums to the targer
            target (int): the interger to sum to

        Returns:
            List[List[int]]: list of all unique combinations of candidates where
                the chosen numbers sum to `target`
        """

        res = []

        def find_combinations(start, combination, remaining):
            """
            Find combinations by adding valid candidates to a combination and
            then backtracking when a combination is found.

            Args:
                start (int): the index of the candidate to start with
                combination (List[int]): the current combination
                remaining (int): the portion of the target not accounted for
            """

            # If there is no portion of the target remaining, a combination has
            # been found. 
            if remaining == 0:
                res.append(combination[:])
                return

            for i in range(start, len(candidates)):
                # We do not need to explore this path if this candidate added to
                # the combination would result in a sum greater than the target.
                if candidates[i] > remaining:
                    break
                combination.append(candidates[i])
                find_combinations(i, combination, remaining - candidates[i])
                combination.pop()

        find_combinations(0, [], target)

        return res


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example1(self):
        candidates = [2, 3, 6, 7]
        target = 7
        expected = [[2, 2, 3], [7]]
        actual = self.sol.combinationSum(candidates, target)
        self.assertEqual(set(map(tuple, expected)), set(map(tuple, actual)))

    def test_example2(self):
        candidates = [2, 3, 5]
        target = 8
        expected = [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
        actual = self.sol.combinationSum(candidates, target)
        self.assertEqual(set(map(tuple, expected)), set(map(tuple, actual)))

    def test_example3(self):
        candidates = [2]
        target = 1
        expected = []
        actual = self.sol.combinationSum(candidates, target)
        self.assertEqual(set(map(tuple, expected)), set(map(tuple, actual)))


if __name__ == "__main__":
    unittest.main()
