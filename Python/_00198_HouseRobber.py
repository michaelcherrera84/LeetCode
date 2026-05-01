from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        You are a professional robber planning to rob houses along a street. 
        Each house has a certain amount of money stashed, the only constraint 
        stopping you from robbing each of them is that adjacent houses have 
        security systems connected and **it will automatically contact the 
        police if two adjacent houses were broken into on the same night**.

        Given an integer array `nums` representing the amount of money of each 
        house, return *the maximum amount of money you can rob tonight **without 
        alerting the police***.

        Args:
            nums (List[int]): list of amounts of money at each house along a 
            street

        Returns:
            int: the maximum amount of money that can be robbed without alerting 
            the police
        """
        currMax = 0
        prevMax = 0

        # At every point along the street, we can determing which of two houses 
        # is the best to rob by keeping a running maximum of the best 
        # opportunities before these.
        for num in nums:
            prev = currMax
            currMax = max(currMax, prevMax + num)
            prevMax = prev
        
        return currMax
    

import unittest


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example1(self):
        nums = [1, 2, 3, 1]
        self.assertEqual(4, self.sol.rob(nums))

    def test_example2(self):
        nums = [2, 7, 9, 3, 1]
        self.assertEqual(12, self.sol.rob(nums))

    def test_example3(self):
        nums = [3, 1, 1, 3]
        self.assertEqual(6, self.sol.rob(nums))

if __name__ == "__main__":
    unittest.main()