class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        """Given an integer array nums, return all the triplets
        `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`,
        and `nums[i] + nums[j] + nums[k] == 0`, without duplicate triplets.

        Args:
            nums (list[int]): the integer array

        Returns:
            list[list[int]]: the set of triplets
        """

        nums = sorted(nums)
        n = len(nums)
        res = []

        # For each number in `nums`, seach for two other numbers such that the
        # three numbers sum to 0.
        for i in range(n - 2):
            # Skip duplicate anchor values.
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # All solution for values before `i` have alreayd been found.
            left = i + 1
            right = n - 1

            # While left is less than right, there are still values to consider.
            while left < right:
                triplet = nums[i] + nums[left] + nums[right]  # current triplet

                # If the triplet is greater than 0, the right value is too high.
                if triplet > 0:
                    right -= 1
                # If the triplet is less than 0, the left value is too low.
                elif triplet < 0:
                    left += 1
                # Otherwise, we have found a triplet. Advance left and right.
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    # Skip duplicate left values.
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    # Skip duplicate right values.
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1


        return res


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example1(self):
        nums = [-1, 0, 1, 2, -1, -4]
        expected = [[-1, -1, 2], [-1, 0, 1]]
        actual = self.sol.threeSum(nums)

        expected = sorted([sorted(triplet) for triplet in expected])
        actual = sorted([sorted(triplet) for triplet in actual])

        self.assertEqual(actual, expected)

    def test_example2(self):
        nums = [0, 1, 1]
        expected = []
        actual = self.sol.threeSum(nums)

        expected = sorted([sorted(triplet) for triplet in expected])
        actual = sorted([sorted(triplet) for triplet in actual])

        self.assertEqual(actual, expected)

    def test_example3(self):
        nums = [0, 0, 0]
        expected = [[0, 0, 0]]
        actual = self.sol.threeSum(nums)

        expected = sorted([sorted(triplet) for triplet in expected])
        actual = sorted([sorted(triplet) for triplet in actual])

        self.assertEqual(actual, expected)

    def test_0_0_0_0(self):
        nums = [0, 0, 0, 0]
        expected = [[0, 0, 0]]
        actual = self.sol.threeSum(nums)

        expected = sorted([sorted(triplet) for triplet in expected])
        actual = sorted([sorted(triplet) for triplet in actual])

        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
