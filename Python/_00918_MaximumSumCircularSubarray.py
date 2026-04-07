from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        """
        Given a **circular integer array** `nums` of length `n`, return *the
        maximum possible sum of a non-empty **subarray** of* `nums`.

        A **circular array** means the end of the array connects to the
        beginning of the array. Formally, the next element of `nums[i]` is
        `nums[(i + 1) % n]` and the previous element of `nums[i]` is
        `nums[(i - 1 + n) % n]`.

        A **subarray** may only include each element of the fixed buffer `nums`
        at most once. Formally, for a subarray
        `nums[i], nums[i + 1], ..., nums[j]`, there does not exist
        `i <= k1, k2 <= j` with `k1 % n == k2 % n`.

        Args:
            nums (List[int]): a circular integer array

        Returns:
            int: the maximum sum of a subarray
        """

        curr_max = 0
        max_sum = nums[0]
        curr_min = 0
        min_sum = nums[0]
        total = 0
        
        for num in nums:
            curr_max = max(curr_max + num, num)
            max_sum = max(max_sum, curr_max)
            curr_min = min(curr_min + num, num)
            min_sum = min(min_sum, curr_min)
            total += num

        # Since the maximum sum could be the result of a subarray that wraps
        # around back to the beginning of the array, the actual max is the 
        # larger of the maximum sequential sum and the total sum minus the sum
        # of the minimum subarray sum.
        return max_sum if max_sum <= 0 else max(max_sum, total - min_sum)

import unittest


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example1(self):
        nums = [1, -2, 3, -2]
        self.assertEqual(3, self.sol.maxSubarraySumCircular(nums))

    def test_example2(self):
        nums = [5, -3, 5]
        self.assertEqual(10, self.sol.maxSubarraySumCircular(nums))

    def test_example3(self):
        nums = [-3, -2, -3]
        self.assertEqual(-2, self.sol.maxSubarraySumCircular(nums))

if __name__ == "__main__":
    unittest.main()