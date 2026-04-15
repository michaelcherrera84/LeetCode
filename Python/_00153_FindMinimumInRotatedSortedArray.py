from typing import List
import math


class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        Suppose an array of length `n` sorted in ascending order is **rotated** 
        between `1` and `n` times. For example, the array `nums = [0,1,2,4,5,6,7]` 
        might become:

        - `[4,5,6,7,0,1,2]` if it was rotated `4` times.
        - `[0,1,2,4,5,6,7]` if it was rotated `7` times.

        Notice that **rotating** an array `[a[0], a[1], a[2], ..., a[n-1]]` 1 
        time results in the array `[a[n-1], a[0], a[1], a[2], ..., a[n-2]]`.

        Given the sorted rotated array `nums` of **unique** elements, return 
        *the minimum element of this array*.

        You must write an algorithm that runs in `O(log n) time`.

        Args:
            nums (List[int]): sorted and rotated list of integers

        Returns:
            int: the minimum element in the list
        """

        left, right = 0, len(nums) - 1

        # Repeatedly discard the half of the list that cannot contain the 
        # minimum value until `left` finally lands on the minimum.
        while left < right:
            mid = left + (right - left) // 2

            # If the middle element is greater than the right element, the 
            # minimum element must be in the right half of the list.
            if nums[mid] > nums[right]:
                left = mid + 1
            # Otherwise the minimum element must be in the left half of the list.
            else:
                right = mid

        return nums[left]


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example1(self):
        nums = [3, 4, 5, 1, 2]
        output = self.sol.findMin(nums)
        self.assertEqual(1, output)

    def test_example2(self):
        nums = [4, 5, 6, 7, 0, 1, 2]
        output = self.sol.findMin(nums)
        self.assertEqual(0, output)

    def test_example3(self):
        nums = [11, 13, 15, 17]
        output = self.sol.findMin(nums)
        self.assertEqual(11, output)

    def test_single_value(self):
        nums = [1]
        output = self.sol.findMin(nums)
        self.assertEqual(1, output)

    def test_positive_and_negative(self):
        nums = [1, 2, 3, 4, -5000]
        output = self.sol.findMin(nums)
        self.assertEqual(-5000, output)

if __name__ == "__main__":
    unittest.main()
