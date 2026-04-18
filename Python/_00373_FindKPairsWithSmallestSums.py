from typing import List
import heapq


class Solution:
    def kSmallestPairs(
        self, nums1: List[int], nums2: List[int], k: int
    ) -> List[List[int]]:
        """
        You are given two integer arrays `nums1` and `nums2` sorted in
        **non-decreasing order** and an integer `k`.

        Define a pair `(u, v)` which consists of one element from the first
        array and one element from the second array.

        Return *the* `k` *pairs* `(u1, v1), (u2, v2), ..., (uk, vk)` *with the
        smallest sums*.

        Args:
            nums1 (List[int]): first integer array
            nums2 (List[int]): second integer array
            k (int): number of pairs to return

        Returns:
            List[List[int]]: the `k` pairs with the smallest sums
        """

        pq = []  # queue of lists containing sums and indices
        pairs = []

        # Add the smallest sum and its indices for each value in `nums1`
        # (max k values) to the queue.
        for i in range(k if k < len(nums1) else len(nums1)):
            heapq.heappush(pq, [nums1[i] + nums2[0], i, 0])

        while len(pq) > 0 and len(pairs) < k:
            pair = heapq.heappop(pq)
            i, j = pair[1], pair[2]

            # Add the next smallest pair to the result list.
            pairs.append([nums1[i], nums2[j]])

            # Add the next smallest sum and its indices from the nums2 values
            # to the queue.
            if j + 1 < len(nums2):
                heapq.heappush(pq, [nums1[i] + nums2[j + 1], i, j + 1])

        return pairs


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example1(self):
        nums1 = [1, 7, 11]
        nums2 = [2, 4, 6]
        k = 3
        expected = [[1, 2], [1, 4], [1, 6]]
        actual = self.sol.kSmallestPairs(nums1, nums2, k)
        self.assertEqual(expected, actual)

    def test_example2(self):
        nums1 = [1, 1, 2]
        nums2 = [1, 2, 3]
        k = 2
        expected = [[1, 1], [1, 1]]
        actual = self.sol.kSmallestPairs(nums1, nums2, k)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
