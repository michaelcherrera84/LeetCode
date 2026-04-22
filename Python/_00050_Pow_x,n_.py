class Solution:
    def myPow(self, x: float, n: int) -> float:
        """
        Implement pow(x, n), which calculates `x` raised to the power `n` 
        (i.e., `xⁿ`).

        Args:
            x (float): a number to be raised to a power
            n (int): an exponent

        Returns:
            float: the number raised to the power of the exponent
        """

        if n == 0:
            return 1
        
        if n < 0:
            n = -n
            x = 1 / x

        if n % 2 == 0:
            return self.myPow(x * x, n // 2)
        else:
            return x * self.myPow(x, n - 1)

import unittest


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example1(self):
        self.assertAlmostEqual(1024.00000, self.sol.myPow(2, 10), 5)
        
    def test_example2(self):
        self.assertAlmostEqual(9.26100, self.sol.myPow(2.10000, 3), 5)

    def test_example3(self):
        self.assertAlmostEqual(0.25000, self.sol.myPow(2.00000, -2), 5)

    def test_min_n(self):
        self.assertAlmostEqual(8.56328, self.sol.myPow(0.999999999, -2147483648), 5)

    def test_max_n(self):
        self.assertAlmostEqual(0.00000, self.sol.myPow(0.0001, 2147483647), 5)


if __name__ == "__main__":
    unittest.main()