from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """Given an integer array `height` of length `n`. There are `n` vertical
        lines drawn such that the two endpoints of the `ith` line are `(i, 0)`
        and (`i, height[i])`.

        Find two lines that together with the x-axis from a container, such that
        the container contains the most water.

        Return *the maximum amount of water a container can store*.

        Args:
            height (List[int]): integer array of line heights

        Returns:
            int: the maximum amount of water a container can store
        """

        max_water = 0;  # the maximum amount of water a container can store

        left = 0
        right = len(height) - 1

        # While left is less than right, there are still heights to consider.
        while left < right:
            base = right - left  # the width of the container
            
            # The water for this container is the shorter height multiplied by
            # base. (area = height x base)
            water = min(height[left], height[right]) * base

            # If this container holds more water than the current max, update max.
            max_water = max(max_water, water)

            # Advance the pointer for the shorter height.
            if height[left] < height[right]:
                left += 1
            elif height[right] < height[left]:
                right -= 1
            else:
                left += 1
                right -= 1

        return max_water


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example1(self):
        height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
        expected = 49
        actual = self.sol.maxArea(height)
        self.assertEqual(expected, actual)

    def test_example2(self):
        height = [1, 1]
        expected = 1
        actual = self.sol.maxArea(height)
        self.assertEqual(expected, actual)

    def test_zeros(self):
        height = [0, 0, 0]
        expected = 0
        actual = self.sol.maxArea(height)
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()
