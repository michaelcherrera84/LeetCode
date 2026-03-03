from typing import List


class Solution:
    def spiralOrder1(self, matrix: List[List[int]]) -> List[int]:
        """Given an `m x n` `matrix`, return *all elements of the* `matrix` *in
        spiral order*.

        Args:
            matrix (List[List[int]]): the matrix

        Returns:
            List[int]: all element of the matrix in spiral order
        """

        rows = len(matrix)
        cols = len(matrix[0])
        spiral = []

        row = 0
        col = 0
        while rows > 0 or cols > 0:
            i = 0
            while i < cols:  # Add top row.
                spiral.append(matrix[row][col])
                i += 1
                col += 1
            rows -= 1  # The row is done. Shrink the matrix.
            if rows == 0:
                break

            # Reset the pointer.
            row += 1
            col -= 1

            i = 0
            while i < rows:  # Add right column.
                spiral.append(matrix[row][col])
                i += 1
                row += 1
            cols -= 1  # The column is done. Shrink the matrix.
            if cols == 0:
                break

            # Reset the pointer.
            col -= 1
            row -= 1

            i = 0
            while i < cols:  # Add the bottom row.
                spiral.append(matrix[row][col])
                i += 1
                col -= 1
            rows -= 1  # The row is done. Shrink the matrix.
            if rows == 0:
                break

            # Reset the pointer.
            row -= 1
            col += 1

            i = 0
            while i < rows:  # Add the left column.
                spiral.append(matrix[row][col])
                i += 1
                row -= 1
            cols -= 1  # the column is down. Shrink the matrix.
            if cols == 0:
                break

            # Reset the pointer.
            col += 1
            row += 1

        return spiral

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """Given an `m x n` `matrix`, return *all elements of the* `matrix` *in
        spiral order*.

        Args:
            matrix (List[List[int]]): the matrix

        Returns:
            List[int]: all element of the matrix in spiral order
        """

        spiral = []
        top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1

        # Where they are still rows and columns, follow the spiral.
        while top <= bottom and left <= right:
            # Add the top row
            for col in range(left, right + 1):
                spiral.append(matrix[top][col])
            top += 1  # Shrink the matrix

            # Add the right column
            for row in range(top, bottom + 1):
                spiral.append(matrix[row][right])
            right -= 1  # Shrink the matrix

            # If there is still a row, add the bottom row.
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    spiral.append(matrix[bottom][col])
                bottom -= 1  # Shrink the matrix

            # If there is still a column, add the left column.
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    spiral.append(matrix[row][left])
                left += 1  # Strink the matrix

        return spiral


import unittest


class Test_Solution(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example1(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        expected = [1, 2, 3, 6, 9, 8, 7, 4, 5]
        actual = self.sol.spiralOrder(matrix)
        self.assertEqual(expected, actual)

    def test_example2(self):
        matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
        expected = [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
        actual = self.sol.spiralOrder(matrix)
        self.assertEqual(expected, actual)

    def test_more_row_than_cols(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
        expected = [1, 2, 3, 6, 9, 12, 11, 10, 7, 4, 5, 8]
        actual = self.sol.spiralOrder(matrix)
        self.assertEqual(expected, actual)

    def test_one_row(self):
        matrix = [[1, 2, 3]]
        expected = [1, 2, 3]
        actual = self.sol.spiralOrder(matrix)
        self.assertEqual(expected, actual)

    def test_one_col(self):
        matrix = [[1], [2], [3]]
        expected = [1, 2, 3]
        actual = self.sol.spiralOrder(matrix)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
