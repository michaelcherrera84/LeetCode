from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Given an array `nums` of distinct integers, return all the possible
        permutations. You can return the answer in **any order**.

        Args:
            nums (List[int]): "array" of nums of distinct integers

        Returns:
            List[List[int]]: all the possible permutations of the given `nums`
        """

        n = len(nums)
        res = []

        def find_permutations(permutation):
            """
            Find all the possible permutations.

            Args:
                permutation (List[int]): the current permutation
            """

            # If the current permutation is full, add it to the list and return.
            if len(permutation) == n:
                res.append(permutation[:])
                return

            # For each number, add it to the permutation if it isn't already
            # present. Advance to the next position of the permutation
            # recursively, then backtrack to the previous position to continue
            # with the other numbers.
            for num in nums:
                if num not in permutation:
                    permutation.append(num)
                    find_permutations(permutation)
                    permutation.pop()

        find_permutations([])

        return res

    def permute1(self, nums: List[int]) -> List[List[int]]:
        """
        Given an array `nums` of distinct integers, return all the possible
        permutations. You can return the answer in **any order**.

        Args:
            nums (List[int]): "array" of nums of distinct integers

        Returns:
            List[List[int]]: all the possible permutations of the given `nums`
        """

        n = len(nums)
        res = []

        def find_permutations(curr_index):
            """
            Find all of the possible permutations by swapping each number with
            each of the other numbers.

            Args:
                curr_index (int): the index of the current number being swapped
            """

            # When the current index is the length of the list, we have found
            # a permutation to add to the list.
            if curr_index == n:
                res.append(nums[:])

            # Swap numbers.
            for i in range(curr_index, n):
                nums[i], nums[curr_index] = nums[curr_index], nums[i]
                find_permutations(curr_index + 1)
                nums[i], nums[curr_index] = nums[curr_index], nums[i]

        find_permutations(0)

        return res


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example1(self):
        nums = [1, 2, 3]
        expected = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
        actual = self.sol.permute(nums)
        self.assertEqual(set(map(tuple, expected)), set(map(tuple, actual)))

    def test_example2(self):
        nums = [0, 1]
        expected = [[0, 1], [1, 0]]
        actual = self.sol.permute(nums)
        self.assertEqual(set(map(tuple, expected)), set(map(tuple, actual)))

    def test_example3(self):
        nums = [1]
        expected = [[1]]
        actual = self.sol.permute(nums)
        self.assertEqual(set(map(tuple, expected)), set(map(tuple, actual)))


if __name__ == "__main__":
    unittest.main()
