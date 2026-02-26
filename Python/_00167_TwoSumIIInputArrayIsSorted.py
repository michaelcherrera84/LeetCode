from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """Given a **1-indexed** array of integers `numbers` that is already
        ***sorted in non-decreasing order***, find two numbers such that they
        add up to a specific `target` number. Let these two numbers be
        `numbers[index~1~]`, and `numbers[index~2~]` where `1 <= index~1 <
        index~2~ <= numbers.length`.

        Return *the indices of the two numbers* `index~1~` *and* `index~2~`,
        *each incremented by one*, as an integer array `[index~1~, index~2~]
        *of length 2*.

        Args:
            numbers (List[int]): the array of integers
            target (int): the target sum

        Returns:
            List[int]: array including the indices of the two values that sum to
            the target
        """

        left = 0  # left pointer
        right = len(numbers) - 1  # right pointer

        # Because the array is sorted, if the right value is greater than the
        # complement of the left, the complement must be to the left of the
        # right value if it exists. If the right value is less than the
        # complement of the left, then the complement of the left does not exist.
        while left < right:
            # the value that sums to the targer when added to the left value
            complement = target - numbers[left]

            # If the right value is equal to the complement, then left and right
            # are the indices of the two values that sum to the target.
            if numbers[right] == complement:
                return [left + 1, right + 1]
            elif numbers[right] > complement:
                right -= 1  # Move the right pointer left.
            else:
                left += 1  # Move the left pointer right.

        # A single solution is guaranteed, so this should not happen.        
        return []


import unittest


class TestSolution(unittest.TestCase):

    def setUp(self) -> None:
        self.sol = Solution()

    def test_example1(self):
        numbers = [2, 7, 11, 15]
        target = 9
        expected = [1, 2]
        actual = self.sol.twoSum(numbers, target)
        self.assertEqual(expected, actual)

    def test_example2(self):
        numbers = [2, 3, 4]
        target = 6
        expected = [1, 3]
        actual = self.sol.twoSum(numbers, target)
        self.assertEqual(expected, actual)

    def test_example3(self):
        numbers = [-1, 0]
        target = -1
        expected = [1, 2]
        actual = self.sol.twoSum(numbers, target)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
