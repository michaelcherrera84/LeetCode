from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Given an integer array `nums`, find the subarray with the largest sum,
        and return *its sum*.

        Args:
            nums (List[int]): the integer array

        Returns:
            int: the subarray with the lastest sum
        """

        curr_sum = nums[0]
        max_sum = nums[0]

        for i in range(1, len(nums)):
            # If the current numer is larger than the current running sum, then
            # it's better to start a new running sum at this number.
            curr_sum = max(curr_sum + nums[i], nums[i])
            # Save the running sum anytime it's larger than the previous max.
            max_sum = max(max_sum, curr_sum)

        return max_sum


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example1(self):
        nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        self.assertEqual(6, self.sol.maxSubArray(nums))

    def test_example2(self):
        nums = [1]
        self.assertEqual(1, self.sol.maxSubArray(nums))

    def test_example3(self):
        nums = [5, 4, -1, 7, 8]
        self.assertEqual(23, self.sol.maxSubArray(nums))


if __name__ == "__main__":
    unittest.main()