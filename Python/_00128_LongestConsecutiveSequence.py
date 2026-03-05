from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """Given an unsorted array of integers `nums`, return *the length of the
        longest consecutive elements sequence*.

        Args:
            nums (List[int]): the unsorted array of integers

        Returns:
            int: the length of the longest consecutive elements sequence
        """

        res = 0

        # A set can be searched in O(1) time and will also remove duplicates.
        num_set = set(nums)

        # For each number in the set...
        for num in num_set:
            # only continue if the number is the beginning of a sequence.
            if num - 1 not in num_set:
                length = 0  # length of the current sequence
                current = num  # current number in the sequence

                # Count each number in the set that is part of this sequence.
                while current in num_set:
                    length += 1
                    current += 1

                # Update the result if this sequence is longer.
                res = max(res, length)

        return res


import unittest


class Test_Solution(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example1(self):
        nums = [100, 4, 200, 1, 3, 2]
        expected = 4
        actual = self.sol.longestConsecutive(nums)
        self.assertEqual(expected, actual)

    def test_example2(self):
        nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
        expected = 9
        actual = self.sol.longestConsecutive(nums)
        self.assertEqual(expected, actual)

    def test_example3(self):
        nums = [1, 0, 1, 2]
        expected = 3
        actual = self.sol.longestConsecutive(nums)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
