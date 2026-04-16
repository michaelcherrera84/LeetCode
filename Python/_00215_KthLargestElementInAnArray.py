from typing import List
import heapq
from random import randint


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Given an integer array `nums` and an integer `k`, return the `kᵗʰ`
        *largest element in the array*.

        Note that it is the `kᵗʰ` largest element in the sorted order, not the
        `kᵗʰ` distinct element.

        Can you solve it without sorting?

        Args:
            nums (List[int]): list of integers
            k (int): the element to find (kᵗʰ largest)

        Returns:
            int: the kᵗʰ largest element
        """

        return sorted(nums)[-k]
    
    def findKthLargest1(self, nums: List[int], k: int) -> int:
        """
        Given an integer array `nums` and an integer `k`, return the `kᵗʰ`
        *largest element in the array*.

        Note that it is the `kᵗʰ` largest element in the sorted order, not the
        `kᵗʰ` distinct element.

        Can you solve it without sorting?

        Args:
            nums (List[int]): list of integers
            k (int): the element to find (kᵗʰ largest)

        Returns:
            int: the kᵗʰ largest element
        """

        pq = []

        for num in nums:
            heapq.heappush(pq, num)

        for _ in range(len(nums) - k):
            heapq.heappop(pq)

        return heapq.heappop(pq)

    def findKthLargest2(self, nums: List[int], k: int) -> int:
        """
        Given an integer array `nums` and an integer `k`, return the `kᵗʰ`
        *largest element in the array*.

        Note that it is the `kᵗʰ` largest element in the sorted order, not the
        `kᵗʰ` distinct element.

        Can you solve it without sorting?

        Args:
            nums (List[int]): list of integers
            k (int): the element to find (kᵗʰ largest)

        Returns:
            int: the kᵗʰ largest element
        """

        # We will search within this range [left, right)
        left, right = 0, len(nums)

        def partition(l, r, p):
            """
            Partition the array into the following parts:
            ```
            nums[l ... <l>]     -> values > pivot
            nums[<l> ... i-1]   -> values == pivot
            nums[i ... r-1]     -> unknown
            nums[r ... end]     -> values < pivot
            ```

            Args:
                l (int): beginning of range
                r (int): end of range
                p (int): pivot index

            Returns:
                tuple: new pivot range
            """
            # Choose pivot value
            pivot = nums[p]

            # We'll move the pivot to the front (index l)
            nums[l], nums[p] = nums[p], nums[l]

            # i scans through the array
            i = l + 1

            while i < r:
                if nums[i] > pivot:
                    # Found a value greater than pivot
                    # Move it into the "greater than" section
                    nums[l], nums[i] = nums[i], nums[l]
                    l += 1
                    i += 1
                elif nums[i] == pivot:
                    # Equal values just stay in the middle
                    i += 1
                else:
                    # nums[i] < pivot
                    # Move it to the right side (smaller section)
                    r -= 1
                    nums[i], nums[r] = nums[r], nums[i]
                    # Don't increment i here, because we need to
                    # check the swapped-in value

            # Return boundaries:
            # [original_l ... l)      -> > pivot
            # [l ... i)              -> == pivot
            # [i ... original_r)     -> < pivot
            return l, i

        while True:
            # Pick a random pivot index
            pivot_index = randint(left, right - 1)

            # Partition the array into 3 parts
            low, high = partition(left, right, pivot_index)

            # Now we check where the k-th largest lies
            if low < k <= high:
                # k falls inside the "equal to pivot" region
                return nums[low]
            elif k <= low:
                # k-th largest is in the "greater than pivot" region
                right = low
            else:
                # k-th largest is in the "less than pivot" region
                left = high


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example1(self):
        nums = [3, 2, 1, 5, 6, 4]
        k = 2
        expected = 5
        actual = self.sol.findKthLargest(nums, k)
        self.assertEqual(expected, actual)

    def test_example2(self):
        nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
        k = 4
        expected = 4
        actual = self.sol.findKthLargest(nums, k)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
