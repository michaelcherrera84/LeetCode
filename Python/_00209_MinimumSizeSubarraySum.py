from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """Given an array of posisitve integers `nums` and a positive integer
        `target`, return *the **minimal length** of a subarray whose sum is
        greater than or equal to* `target`. If there is such subarray, return
        `0` instead.

        Args:
            target (int): sum to search for
            nums (List[int]): the array of integers

        Returns:
            int: minimal length of a subarray whose sum is greater than or equal
            to `target` or `0` if there is no such subarray
        """

        n = len(nums)
        min_len = n + 1  # minimal length of subarray
        win_sum = 0  # running sum of subarray
        left = 0  # left edge of sliding window
        right = 0  # right edge of sliding window

        # For each value in the array...
        for right in range(n):
            win_sum += nums[right]  # Add the right value to the running sum.

            # While the running sum is greater than or equal to the target,
            # keep shrinking the window and update the minimal length.
            while win_sum >= target:
                # Update the minimal length.
                min_len = min(min_len, right - left + 1)
                # Shrink the window by subtracting the left value and advancing
                # the left pointer.
                win_sum -= nums[left]
                left += 1

        # If minLen is less than or equal to n, then there was a subarray found.
        return min_len if min_len <= n else 0


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example1(self):
        target = 7
        nums = [2, 3, 1, 2, 4, 3]
        expected = 2
        actual = self.sol.minSubArrayLen(target, nums)
        self.assertEqual(expected, actual)

    def test_example2(self):
        target = 4
        nums = [1, 4, 4]
        expected = 1
        actual = self.sol.minSubArrayLen(target, nums)
        self.assertEqual(expected, actual)

    def test_example3(self):
        target = 11
        nums = [1, 1, 1, 1, 1, 1, 1, 1]
        expected = 0
        actual = self.sol.minSubArrayLen(target, nums)
        self.assertEqual(expected, actual)

    def test_one_element_equal_target(self):
        target = 5
        nums = [5]
        expected = 1
        actual = self.sol.minSubArrayLen(target, nums)
        self.assertEqual(expected, actual)

    def test_one_element_not_equal_target(self):
        target = 5
        nums = [1]
        expected = 0
        actual = self.sol.minSubArrayLen(target, nums)
        self.assertEqual(expected, actual)

    def test_multiple_options_min_earlier(self):
        target = 7
        nums = [3, 4, 1, 2, 4, 1]
        expected = 2
        actual = self.sol.minSubArrayLen(target, nums)
        self.assertEqual(expected, actual)

    def test_all_number_sum_to_target(self):
        target = 15
        nums = [5, 4, 3, 2, 1]
        expected = 5
        actual = self.sol.minSubArrayLen(target, nums)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
