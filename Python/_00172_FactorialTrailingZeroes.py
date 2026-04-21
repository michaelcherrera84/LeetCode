class Solution:
    def trailingZeroes(self, n: int) -> int:
        """
        Given an integer `n`, return *the number of trailing zeroes in* `n!`.

        Note that `n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1`.

        Args:
            n (int): an integer

        Returns:
            int: the number of trailing zeroes in `n!`
        """

        ##
        # Intuition:
        # Trailing zeros are the result of multiplying by 10. Multiplying by a
        # number is the same as multiplying by of its factors. With this in mind,
        # we can find all numbers with factors of 5 between 1 and n and count
        # them. For each factor of 5, there will always be a factor of 2 that
        # the five could be multiplied with to make 10.
        # Example:
        #            5! = 1 x 2 x 3 x 4 x 5
        #               = 1 x 2 x 3 x 2(2 x 5)
        #               = 1 x 2 x 3 x 2(10) = 120
        # One ten results in one trailing zero.
        ##

        fives = 0

        # Count the factors of 5 between 1 and n.
        # Example: n = 50
        #   Numbers with factors of 5: 5, 10, 15, 20, 25, 30, 35, 40, 45, 50
        #   Count of factors of 5:     1 + 1 + 1 + 1 + 2 + 1 + 1 + 1 + 1 + 2 = 12
        #   Note: 25 and 50 both have two factors of 5
        #   50 / 5 = 10,    10 / 5 = 2,     10 + 2 = 12
        while n > 0:
            n //= 5
            fives += n

        return fives


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example1(self):
        self.assertEqual(0, self.sol.trailingZeroes(3))

    def test_example2(self):
        self.assertEqual(1, self.sol.trailingZeroes(5))

    def test_example3(self):
        self.assertEqual(0, self.sol.trailingZeroes(0))

    def test_n_with_multiple_factors_of_5(self):
        self.assertEqual(6, self.sol.trailingZeroes(25))

    def test_max_n(self):
        self.assertEqual(2499, self.sol.trailingZeroes(10_000))


if __name__ == "__main__":
    unittest.main()
