from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """ "The **Game of Life**, also known simply as **Life**, is a cellular
        automaton devised by the British mathematician John Horton Conway in
        1970." - [Wikipedia]("https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life")

        The board is made up an `m x n` grid of cells, where each cell has an
        initial state: **live** (represented by a `1`) or **dead** (represented
        by a `0`). Each cell interacts with its eight neighbors (horizontal,
        vertical, diagonal) using the following four rules:

        1. Any live cell with fewer than two live neighbors dies as if caused by
        under-population.
        2. Any live cell with two or three live neighbors lives on to the next
        generation.
        3. Any live cell with more than three live neighbors dies, as if by
        over-population.
        4. Any dead cell with exactly three live neighbors becomes a live cell,
        as if by reproduction.

        The next state of the board is determined by applying the rules
        simultaneously to every cell in the current state of the `m x n` grid
        `board`. In this process, births and deaths occur **simultaneously**.

        Given the current state of the `board`, **update** the `board` to
        reflect it's next state.

        Args:
            board (List[List[int]]): the game board
        """

        rows = len(board)
        cols = len(board[0])

        # First pass:
        # Count the live cells around each cell. If the cell is dead and will
        # stay dead, or the cell is alive and will stay alive, leave it alone.
        # If the cell is alive and will become dead, set it to 2. If the cell is
        # dead and will become alive, set it to 3.
        for r in range(rows):
            for c in range(cols):
                lives = 0

                for i in range(r - 1, r + 2):
                    for j in range(c - 1, c + 2):
                        if (
                            i >= 0
                            and i < rows
                            and j >= 0
                            and j < cols
                            and not (i == r and j == c)
                        ):
                            if board[i][j] == 1 or board[i][j] == 2:
                                lives += 1

                if board[r][c] == 1 and (lives < 2 or lives > 3):
                    board[r][c] = 2
                elif board[r][c] == 0 and lives == 3:
                    board[r][c] = 3

        # Second pass: (apply rules "simultaneously")
        # If the cell is 0 or 1 leave it alone. Change all 2s to 0s (alive to 
        # dead). Change all 3s to 1s (dead to alive).
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 2:
                    board[r][c] = 0
                elif board[r][c] == 3:
                    board[r][c] = 1


import unittest


class Test_Solution(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example1(self):
        board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
        expected = [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]]
        self.sol.gameOfLife(board)  # actual
        self.assertEqual(expected, board)

    def test_example2(self):
        board = [[1, 1], [1, 0]]
        expected = [[1, 1], [1, 1]]
        self.sol.gameOfLife(board)  # actual
        self.assertEqual(expected, board)

    def test_one_cell_live(self):
        board = [[1]]
        expected = [[0]]
        self.sol.gameOfLife(board)  # actual
        self.assertEqual(expected, board)

    def test_one_cell_dead(self):
        board = [[0]]
        expected = [[0]]
        self.sol.gameOfLife(board)  # actual
        self.assertEqual(expected, board)

    def test_row(self):
        board = [[1, 1, 1]]
        expected = [[0, 1, 0]]
        self.sol.gameOfLife(board)  # actual
        self.assertEqual(expected, board)

    def test_one_col(self):
        board = [[1], [1], [1]]
        expected = [[0], [1], [0]]
        self.sol.gameOfLife(board)  # actual
        self.assertEqual(expected, board)

    def all_live(self):
        board = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
        expected = [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
        self.sol.gameOfLife(board)  # actual
        self.assertEqual(expected, board)


if __name__ == "__main__":
    unittest.main()
