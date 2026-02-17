class Solution:
    def climbStairs(self, n: int) -> int:
        """Given `n` steps to reach the top of a staircase, find the number of 
        distinct ways you can climb to the top if each time you can either climb 
        1 or 2 steps.

        Args:
            n (int): number steps

        Returns:
            int: number of distinct ways to climb to the top of the stairs
        """

        # If there are one or no stairs, there is only one way to climb.
        if n <= 1:
            return 1
        
        prev2 = 1   # two climbs ago
        prev1 = 1   # one climb ago

        # For each step from the second step up...
        for i in range(2, n + 1):
            # the number of ways to climb to this step is the number of ways of
            # the previous two steps.
            current = prev1 + prev2
            # Remember the previous step into the next step.
            prev2 = prev1
            # Rememver this step into the next step.
            prev1 = current

        # When the loop ends, prev1 will have the ways for the last step.
        return prev1

import unittest

class TestSolution(unittest.TestCase):
    
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.climbStairs(2), 2)

    def test_example2(self):
        self.assertEqual(self.sol.climbStairs(3), 3)

    def test_greatest_input(self):
        self.assertEqual(self.sol.climbStairs(45), 1836311903)

if __name__ == '__main__':
    unittest.main()