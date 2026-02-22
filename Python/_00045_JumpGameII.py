from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        """Given an array of integers `nums`, start at position 0. Each element
        nums[i] represents the maximum length of a forward jump from index `i`.
        Return *the minimum number of jumps to reach the last index*.

        Args:
            nums (List[int]): array integers that represent the masimum length
            of a foward jump

        Returns:
            int: the minimum number of jumps needed to reach the end of the
            array
        """

        farthest = 0    # the farthest position that can be reached from an index
        jumps = 0       # the number of jumps made
        curr_end = 0     # the end of the possible range for the number of jumps

        for i in range(0, len(nums) - 1):
            farthest = max(farthest, i + nums[i])

            # If we reach the end of the range for the current number of jumps
            # we must jump again and establish a new range from the current
            # farthest reachable position.
            if i == curr_end:
                jumps += 1
                curr_end = farthest

        return jumps


import unittest


class TestSoluction(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.jump([2, 3, 1, 1, 4]), 2)

    def test_example2(self):
        self.assertEqual(self.sol.jump([2, 3, 0, 1, 4]), 2)

    def test_one_position_zero(self):
        self.assertEqual(self.sol.jump([0]), 0)

    def test_two_positions(self):
        self.assertEqual(self.sol.jump([1, 0]), 1)


if __name__ == "__main__":
    unittest.main()
