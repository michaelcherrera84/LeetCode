from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        There is an integer array `nums` sorted in ascending order (with
        **distinct** values).

        Prior to being passed to your function, `nums` is **possibly left
        rotated** at an unknown index `k` (`1 <= k < nums.length`) such that the
        resulting array is...
        `[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]`
        (**0-indexed**). For example, `[0,1,2,4,5,6,7]` might be left rotated by
        `3` indices and become `[4,5,6,7,0,1,2]`.

        Given the array `nums` after the possible rotation and an integer
        `target`, return *the index of* `target` *if it is in* `nums`, *or* `-1`
        *if it is not in* `nums`.

        You must write an algorithm with `O(log n)` runtime complexity.

        Args:
            nums (List[int]): a list of integers
            target (int): the integer to search for

        Returns:
            int: the index of the integer if found or `-1` if not
        """

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid

            # If the left side of the array is sorted...
            if nums[left] <= nums[mid]:
                # If the target fits in the left side, discard the right side.
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                # If the target does not fit in the left side, discard the left.
                else:
                    left = mid + 1
            # If the right side of the array is sorted...
            else:
                # If the target fits in the right side, discard the left side.
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                # If the target does not fit in the right side, discard the right.
                else:
                    right = mid - 1

        return -1


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example1(self):
        nums = [4, 5, 6, 7, 0, 1, 2]
        self.assertEqual(4, self.sol.search(nums, 0))

    def test_example2(self):
        nums = [4, 5, 6, 7, 0, 1, 2]
        self.assertEqual(-1, self.sol.search(nums, 3))

    def test_example3(self):
        nums = [1]
        self.assertEqual(-1, self.sol.search(nums, 0))

    def test_example4(self):
        nums = [4, 5, 0, 1, 2, 3]
        self.assertEqual(0, self.sol.search(nums, 4))

    def test_example5(self):
        nums = [1, 2, 4, 5, 6, 7, 0]
        self.assertEqual(6, self.sol.search(nums, 0))

    def test_example6(self):
        nums = [4, 5, 6, 7, 0, 1, 2]
        self.assertEqual(6, self.sol.search(nums, 2))

    def test_example7(self):
        nums = [5, 1, 3]
        self.assertEqual(2, self.sol.search(nums, 3))


if __name__ == "__main__":
    unittest.main()
