from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        Given an array of integers `nums` sorted in non-decreasing order, find
        the starting and ending position of a given `target` value.

        If `target` is not found in the array, return `[-1, -1]`.

        You must write an algorithm with `O(log n)` runtime complexity.

        Args:
            nums (List[int]): list of integers sorted in non-decreasing order
            target (int): integer to find in the list

        Returns:
            List[int]: starting and ending point of the target in the list or
            `[-1, -1]` if the target is not in the list
        """

        n = len(nums)

        def find_left():
            """
            Find the first element with the target value if it exists.

            Returns:
                int: the index of the first element with the target value or `-1`
                if the value is not in the list
            """

            left, right = 0, n - 1
            i = -1
            while left <= right:
                mid = left + (right - left) // 2

                # If the target is found, store the index and continue searching
                # to the left for the first element with the same target value.
                if nums[mid] == target:
                    i = mid
                    right = mid - 1  
                elif target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            return i

        def find_right():
            """
            Find the last element with the target value if it exists.

            Returns:
                int: the index of the last element with the target value or `-1`
                if the value is not in the list
            """

            left, right = 0, n - 1
            i = -1
            while left <= right:
                mid = left + (right - left) // 2

                # If the target is found, store the index and continue searching
                # to the right for the last element with the same target value.
                if nums[mid] == target:
                    i = mid
                    left = mid + 1  
                elif target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            return i

        return [find_left(), find_right()]


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_solution1(self):
        nums = [5, 7, 7, 8, 8, 10]
        target = 8
        expected = [3, 4]
        actual = self.sol.searchRange(nums, target)
        self.assertEqual(expected, actual)

    def test_solution2(self):
        nums = [5, 7, 7, 8, 8, 10]
        target = 6
        expected = [-1, -1]
        actual = self.sol.searchRange(nums, target)
        self.assertEqual(expected, actual)

    def test_solution3(self):
        nums = []
        target = 0
        expected = [-1, -1]
        actual = self.sol.searchRange(nums, target)
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()