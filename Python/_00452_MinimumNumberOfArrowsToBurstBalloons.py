from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        """There are some spherical ballons taped onto a flat wall that
        represents the XY-plane. The balloons are represented as a 2D integer
        array `points` where `points[i] = [x_start_, x_end_]` denotes a balloon
        whose **horizontal diameter** stretches between `x_start_` and `x_end_`.
        You do not know the exact y-coordinates of the balloons.

        Arrows can be shot up directly vertically (in the positive y-directions)
        from different points along the x-axis. A balloon with `x_start_` and
        `x_end_` is **burst** by an arrow shot at `x` if
        `x_start_ <= x <= x_end_`. There is **no limit** to the number of arrows
        that can be shot. A shot arrow keeps traveling up infinitely, bursting
        any ballons in its path.

        Given the array `points` return *the **minimum** number of arrows that
        must be shot to burst all balloons*.

        Args:
            points (List[List[int]]): the array representing the balloons

        Returns:
            int: the minimum number of arrows that must be shot to burst all
            balloons
        """

        # Sort the array in the order of the trailing edge balloons along the path.
        points.sort(key=lambda p: p[1])

        # At least one shot is required.
        shots = 1
        # the edge of the first ballon that has not been shot
        curr_dist = points[0][1]

        # For each balloon after the first balloon, check if the ballon can be
        # hit with the same arrow that will be shot at the first unshot balloon.
        for i in range(1, len(points)):
            # If the leading edge of this balloon is past the trailing edge of
            # the first unshot balloon, then we cannot hit this balloon with
            # that arrow. Another shot will be required to continue and the
            # trailing edge of this balloon will be the new tailing edge of the
            # first unshot balloon.
            if points[i][0] > curr_dist:
                curr_dist = points[i][1]
                shots += 1

        return shots


import unittest


class Test_Solution(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example1(self):
        points = [[10, 16], [2, 8], [1, 6], [7, 12]]
        expected = 2
        actual = self.sol.findMinArrowShots(points)
        self.assertEqual(expected, actual)

    def test_example2(self):
        points = [[1, 2], [3, 4], [5, 6], [7, 8]]
        expected = 4
        actual = self.sol.findMinArrowShots(points)
        self.assertEqual(expected, actual)

    def test_example3(self):
        points = [[1, 2], [2, 3], [3, 4], [4, 5]]
        expected = 2
        actual = self.sol.findMinArrowShots(points)
        self.assertEqual(expected, actual)

    def test_really_wide_first_balloon(self):
        points = [[1, 10], [2, 3], [3, 4], [9, 11]]
        expected = 2
        actual = self.sol.findMinArrowShots(points)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
