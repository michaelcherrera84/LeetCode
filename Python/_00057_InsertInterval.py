from typing import List
import bisect


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        """You are given an array of non-overlapping intervals `intervals` where
        `intervals[i] = [startᵢ, endᵢ]` represent the start and the end of the
        `iᵗʰ` interval and `intervals` is sorted in ascending order by `startᵢ`.
        You are also given an interval `newInterval = [start, end]` that
        represents the start and end of another interval.

        Insert `newInterval` into `intervals` such that `intervals` is still
        sorted in ascending order by `startᵢ` and `intervals` still does not
        have any overlapping intervals (merge overlapping intervals if
        necessary).

        Return `intervals` *after the insertion*.

        Args:
            intervals (List[List[int]]): the array of non-overlapping intervals
            newInterval (List[int]): the interval to be inserted

        Returns:
            List[List[int]]: an array with `newInterval` inserted
        """

        n = len(intervals)
        res = []

        # 1. Skip non-overlapping intervals before newInterval
        i = bisect.bisect_left(intervals, newInterval[0], key=lambda x: x[1])
        res.extend(intervals[:i])

        # 2. Merge all overlapping intervals
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        res.append(newInterval)

        # 3. Add the remaining non-overlapping intervals
        res.extend(intervals[i:])

        return res

import unittest


class Test_Solution(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example1(self):
        intervals = [[1, 3], [6, 9]]
        newInterval = [2, 5]
        expected = [[1, 5], [6, 9]]
        actual = self.sol.insert(intervals, newInterval)
        self.assertEqual(expected, actual)

    def test_example2(self):
        intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
        newInterval = [4, 8]
        expected = [[1, 2], [3, 10], [12, 16]]
        actual = self.sol.insert(intervals, newInterval)
        self.assertEqual(expected, actual)

    def test_intervals_empty(self):
        intervals = []
        newInterval = [1, 2]
        expected = [[1, 2]]
        actual = self.sol.insert(intervals, newInterval)
        self.assertEqual(expected, actual)

    def test_insert_at_beginning_overlap(self):
        intervals = [[2, 3], [4, 7]]
        newInterval = [0, 5]
        expected = [[0, 7]]
        actual = self.sol.insert(intervals, newInterval)
        self.assertEqual(expected, actual)

    def test_insert_at_beginning_no_overlap(self):
        intervals = [[4, 5], [6, 7]]
        newInterval = [0, 2]
        expected = [[0, 2], [4, 5], [6, 7]]
        actual = self.sol.insert(intervals, newInterval)
        self.assertEqual(expected, actual)

    def test_insert_at_end_overlap(self):
        intervals = [[2, 3], [4, 7]]
        newInterval = [5, 8]
        expected = [[2, 3], [4, 8]]
        actual = self.sol.insert(intervals, newInterval)
        self.assertEqual(expected, actual)

    def test_insert_at_end_no_overlap(self):
        intervals = [[2, 3], [4, 7]]
        newInterval = [8, 9]
        expected = [[2, 3], [4, 7], [8, 9]]
        actual = self.sol.insert(intervals, newInterval)
        self.assertEqual(expected, actual)

    def test_multiple_overlap(self):
        intervals = [[2, 4], [6, 7], [9, 11]]
        newInterval = [3, 10]
        expected = [[2, 11]]
        actual = self.sol.insert(intervals, newInterval)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
