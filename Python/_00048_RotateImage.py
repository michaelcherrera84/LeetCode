from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """Given an `n x n` 2D `matrix` representing an image, rotate the image
        by 90 degrees (clockwise).

        Rotate the image in-place.

        Args:
            matrix (List[List[int]]): the 2D matrix
        """

        n = len(matrix)

        # Transpose the matrix ((row, col) -> (col, row)). 
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Reverse each row ((row, col) -> (row, n − 1 − col)).
        for i in range(n):
            j, k = 0, n - 1
            while j < k:
                matrix[i][j], matrix[i][k] = matrix[i][k], matrix[i][j]
                j += 1
                k -= 1

    def rotate1(self, matrix: List[List[int]]) -> None:
        """Given an `n x n` 2D `matrix` representing an image, rotate the image
        by 90 degrees (clockwise).

        Rotate the image in-place.

        Args:
            matrix (List[List[int]]): the 2D matrix
        """

        start, end = 0, len(matrix) - 1

        # Rotate each value one-by-one, beginning with the outermost layer and
        # working in.
        while end - start > 0:
            for i in range(end - start):
                matrix[start][start + i], matrix[start + i][end] = (
                    matrix[start + i][end],
                    matrix[start][start + i],
                )
                matrix[start][start + i], matrix[end][end - i] = (
                    matrix[end][end - i],
                    matrix[start][start + i],
                )
                matrix[start][start + i], matrix[end - i][start] = (
                    matrix[end - i][start],
                    matrix[start][start + i],
                )

            # Move in one layer.
            start += 1
            end -= 1

    def rotate2(self, matrix: List[List[int]]) -> None:
        """Given an `n x n` 2D `matrix` representing an image, rotate the image
        by 90 degrees (clockwise).

        Rotate the image in-place.

        Args:
            matrix (List[List[int]]): the 2D matrix
        """

        matrix[:] = [list(row) for row in zip(*matrix[::-1])]


import unittest


class Test_Solution(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example1(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        expected = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
        self.sol.rotate(matrix)
        self.assertEqual(expected, matrix)

    def test_example2(self):
        matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
        expected = [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]
        self.sol.rotate(matrix)
        self.assertEqual(expected, matrix)


if __name__ == "__main__":
    unittest.main()
