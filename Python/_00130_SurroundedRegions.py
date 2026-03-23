from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """You are given an `m x n` matrix `board` containing **letters** `'X'`
        and `'O'`, **capture regions** that are **surrounded**:

        - **Connect**: A cell is connected to adjacent cells horizontally or
        vertically.
        - **Region**: To form a region connect every `'O'` cell.
        - **Surround**: A region is surrounded if none of the `'O'` cells in
        that region are on the edge of the board. Such regions are **completely
        enclosed** by `'X'` cells.

        To capture a **surrounded region**, replace all `'O'`s with `'X'`s
        **in-place** within the original board. You do not need to return
        anything.

        Args:
            board (List[List[str]]): the matrix of Xs and Os
        """

        rows = len(board)
        cols = len(board[0])

        def find_not_surrounded(r, c):
            """Find a region of connected `'O'`s and set them to `'#'` indicating
            a region of cells that cannot be surrounded.

            Args:
                r (int): the row index of the board
                c (int): the column index of the board
            """

            # Stop searching if we reach the edge of the board or hit a cell
            # that is not an 'O'.
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != "O":
                return

            board[r][c] = "#"

            find_not_surrounded(r + 1, c)
            find_not_surrounded(r - 1, c)
            find_not_surrounded(r, c + 1)
            find_not_surrounded(r, c - 1)

        # Search for 'O's in the first and last rows. If an 'O' is found, find
        # any connected 'O's and mark them all as NOT surrounded ('#').
        for c in range(cols):
            if board[0][c] == "O":
                find_not_surrounded(0, c)
            if board[rows - 1][c] == "O":
                find_not_surrounded(rows - 1, c)

        # Search for 'O's in the first and last columns. If an 'O' is found, find
        # any connected 'O's and mark them all as NOT surrounded ('#').
        for r in range(rows):
            if board[r][0] == "O":
                find_not_surrounded(r, 0)
            if board[r][cols - 1] == "O":
                find_not_surrounded(r, cols - 1)

        # Find all cells that are NOT surrounded ('#') and set them to 'O'. All
        # other cells should be 'X'.
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "#":
                    board[r][c] = "O"
                else:
                    board[r][c] = "X"


import unittest


class Test_Solution(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example1(self):
        board = [
            ["X", "X", "X", "X"],
            ["X", "O", "O", "X"],
            ["X", "X", "O", "X"],
            ["X", "O", "X", "X"],
        ]
        expected = [
            ["X", "X", "X", "X"],
            ["X", "X", "X", "X"],
            ["X", "X", "X", "X"],
            ["X", "O", "X", "X"],
        ]
        self.sol.solve(board)
        self.assertEqual(expected, board)

    def test_example2(self):
        board = [["X"]]
        expected = [["X"]]
        self.sol.solve(board)
        self.assertEqual(expected, board)

    def test_Os_near_edge(self):
        board = [
            ["X", "X", "X", "X"],
            ["O", "O", "X", "X"],
            ["O", "O", "X", "X"],
            ["X", "X", "X", "X"],
        ]
        expected = [
            ["X", "X", "X", "X"],
            ["O", "O", "X", "X"],
            ["O", "O", "X", "X"],
            ["X", "X", "X", "X"],
        ]
        self.sol.solve(board)
        self.assertEqual(expected, board)


if __name__ == "__main__":
    unittest.main()
