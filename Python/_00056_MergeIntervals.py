from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """Given an array of `intervals` where `intervals[i] = [startᵢ, endᵢ]`,
        merge all overlapping intervals, and return *an array of the
        non-overlapping intervals that cover all of the intervals in the input*.

        Args:
            intervals (List[List[int]]): the array of intervals

        Returns:
            List[List[int]]: array of the non-overlapping intervals that cover
            all intervals in the input.
        """

        # If the intervals are sorted, then overlapping intervals will always be
        # adjacent to each other.
        intervals.sort()
        res = [intervals[0]]  # result array of non-overlapping intervals

        # Compare the beginning of each interval to the end of the last interval
        # in the result.
        for i in range(1, len(intervals)):
            # If this interval begins with a value that is less or equal to the 
            # end of the last interval, then the intervals overlap.
            if intervals[i][0] <= res[-1][1]:
                # If the end of this interval is greater than the end of the
                # last interval, then the end of this interval is the new end of
                # the last interval.
                res[-1][1] = max(res[-1][1], intervals[i][1])
            else:
                # If the intervals don't overlap, then this interval is a new
                # interval in the result.
                res.append(intervals[i])

        return res


import unittest


class Test_Solution(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example1(self):
        intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
        expected = [[1, 6], [8, 10], [15, 18]]
        actual = self.sol.merge(intervals)
        self.assertEqual(expected, actual)

    def test_example2(self):
        intervals = [[1, 4], [4, 5]]
        expected = [[1, 5]]
        actual = self.sol.merge(intervals)
        self.assertEqual(expected, actual)

    def test_example3(self):
        intervals = [[4, 7], [1, 4]]
        expected = [[1, 7]]
        actual = self.sol.merge(intervals)
        self.assertEqual(expected, actual)

    def test_first_interval_overlaps_all(self):
        intervals = [[1, 5], [2, 3]]
        expected = [[1, 5]]
        actual = self.sol.merge(intervals)
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()