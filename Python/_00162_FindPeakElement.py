from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        """
        A peak element is an element that is strictly greater than its neighbors.

        Given a **0-indexed** integer array `nums`, find a peak element, and
        return its index. If the array contains multiple peaks, return the index
        to **any of the peaks**.

        You may imagine that `nums[-1] = nums[n] = -∞`. In other words, an
        element is always considered to be strictly greater than a neighbor that
        is outside the array.

        You must write an algorithm that runs in `O(log n)` time.

        ## Constraints
        - `1 <= nums.length <= 1000`
        - `-2³¹ <= nums[i] <= 2³¹ - 1`
        - `nums[i] != nums[i + 1]` for all valid `i`

        Args:
            nums (List[int]): a list of integers containing a peak element

        Returns:
            int: the index of a peak element
        """

        left = 0
        right = len(nums) - 1

        # When left and right are the same, they are a peak element.
        while left < right:
            mid = left + (right - left) // 2

            # Determine the side of the list to continue the "search" in.
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1

        return left


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example1(self):
        nums = [1, 2, 3, 1]
        output = self.sol.findPeakElement(nums)
        self.assertIn(output, {2})

    def test_example2(self):
        nums = [1, 2, 1, 3, 5, 6, 4]
        output = self.sol.findPeakElement(nums)
        self.assertIn(output, {1, 5})

    def test_example3(self):
        nums = [6, 5, 4, 3, 2, 1]
        output = self.sol.findPeakElement(nums)
        self.assertIn(output, {0})

    def test_example4(self):
        nums = [7, 1, 2, 4, 5, 6] 
        output = self.sol.findPeakElement(nums)
        self.assertIn(output, {0, 5})


if __name__ == "__main__":
    unittest.main()
