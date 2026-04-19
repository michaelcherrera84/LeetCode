from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        Given an integer array `nums` where every element appears **three
        times** except for one, which appears **exactly once**. *Find the single
        element and return it*.

        You must implement a solution with a linear runtime complexity and use
        only constant extra space.

        Args:
            nums (List[int]): list of integers where every element appears three
            times except for one

        Returns:
            int: the one integer that appears only once
        """

        ones = 0
        twos = 0

        for num in nums:
            ones ^= (num & ~twos)
            twos ^= (num & ~ones)

        return ones

import unittest


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example1(self):
        nums = [2, 2, 3, 2]
        expected = 3
        actual = self.sol.singleNumber(nums)
        self.assertEqual(expected, actual)

    def test_example2(self):
        nums = [0, 1, 0, 1, 0, 1, 99]
        expected = 99
        actual = self.sol.singleNumber(nums)
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()