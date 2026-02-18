from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """Given and integer array `nums`, rotate the array to the right by `k`
        steps, where `k` is non-negative.

        Args:
            nums (List[int]): integer array
            k (int): number of steps to rotate the array
        """

        n = len(nums)
        k = k % n  # Remove extra full rotations.

        def reverse(start, end):
            """Reverse an array or portion of an array

            Args:
                start (int): beginning index of sub-array
                end (int): ending index of sub-array
            """

            # If start is not less than end, all of the elements have been swapped.
            while start < end:
                # Swap the first and last elements.
                [nums[start], nums[end]] = [nums[end], nums[start]]
                start += 1
                end -= 1

        reverse(0, n - 1)  # Reverse the whole array.
        reverse(0, k - 1)  # Reverse the part of the array up to the shift.
        reverse(k, n - 1)  # Reverse the part of the array from the shift on.


import unittest


class TestSolution(unittest.TestCase):

    def setUp(self) -> None:
        self.sol = Solution()

    def test_example1(self):
        nums = [1, 2, 3, 4, 5, 6, 7]
        self.sol.rotate(nums, 3)
        self.assertEqual(nums, [5, 6, 7, 1, 2, 3, 4])


if __name__ == "__main__":
    unittest.main()
