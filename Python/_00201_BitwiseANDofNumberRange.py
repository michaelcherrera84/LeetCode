class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        """
        Given two integers `left` and `right` that represent the range 
        `[left, right]`, return *the bitwise AND of all numbers in this range, 
        inclusive*.

        Args:
            left (int): beginning of the range
            right (int): end of the range

        Returns:
            int: the bitwise AND of all numbers in the range
        """

        shift = (left ^ right).bit_length()
        return (left >> shift) << shift
    
import unittest


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example1(self):
        self.assertEqual(4, self.sol.rangeBitwiseAnd(5, 7))

    def test_example2(self):
        self.assertEqual(0, self.sol.rangeBitwiseAnd(0, 0))

    def test_example3(self):
        self.assertEqual(0, self.sol.rangeBitwiseAnd(1, 2147483647))

    def test_example4(self):
        self.assertEqual(8, self.sol.rangeBitwiseAnd(9, 15))

if __name__ == "__main__":
    unittest.main()