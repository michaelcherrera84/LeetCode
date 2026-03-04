from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """Given an `m x n` integer `matrix`, if an element is `0`, set its
        entire row and column to `0`'s (in place).

        Args:
            matrix (List[List[int]]): the integer matrix
        """

        rows = len(matrix)
        cols = len(matrix[0])

        zeroRow0 = False  # true if first row should be zeros
        zeroCol0 = False  # true if first column should be zeros

        # Find zero rows and columns.
        for r in range(rows):
            for c in range(cols):
                # If the current number is zero, mark the current row and column 
                # by setting their first elements to zero.
                if matrix[r][c] == 0:
                    # Check if first row/col should be zeros.
                    if r == 0:
                        zeroRow0 = True
                    if c == 0:
                        zeroCol0 = True
                    
                    matrix[0][c] = 0
                    matrix[r][0] = 0

        # Set each value to zero where the row maker or column marker is zero.
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        # Set the first row and column to zeros if appropriate.
        if zeroRow0:
            for c in range(cols):
                matrix[0][c] = 0
        
        if zeroCol0:
            for r in range(rows):
                matrix[r][0] = 0

                



import unittest


class Test_Solution(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example1(self):
        matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
        expected = [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
        self.sol.setZeroes(matrix)  # Actual
        self.assertEqual(expected, matrix)

    def test_example2(self):
        matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
        expected = [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]
        self.sol.setZeroes(matrix)  # Actual
        self.assertEqual(expected, matrix)

if __name__ == "__main__":
    unittest.main()
