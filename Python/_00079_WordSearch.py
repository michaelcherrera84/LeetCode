from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        Given an `m x n` grid of characters `board` and a string `word`, return
        `true` *if* `word` *exists in the grid*.

        The word can be constructed from letters of sequentially adjacent cells,
        where adjacent cells are horizontally or vertically neighboring. The
        same letter cell may not be used more than once.

        Args:
            board (List[List[str]]): an `m x n` grid of characters
            word (str): a string to search for on the `board`

        Returns:
            bool: `True` if the word exists or `False` otherwise
        """

        rows, cols = len(board), len(board[0])
        # directions (row, col) to move from a current cell
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def search(r, c, i):
            """
            Search connected elements on a board for a desired word.

            Args:
                r (int): the current row of the board
                c (int): the current col of the board
                i (int): the index of the current expected letter

            Returns:
                bool: `True` if all letters are found, or `False` otherwise
            """

            if i == len(word):  # All letter have been found
                return True

            if r < 0 or r > rows - 1 or c < 0 or c > cols - 1:
                return False

            if board[r][c] != word[i]:
                return False

            # Mark this cell as visited so we do not attempt to use it again.
            saved_val = board[r][c]
            board[r][c] = "#"

            for dr, dc in directions:
                if search(r + dr, c + dc, i + 1):
                    return True

            # If none of the searches found the next letter, restore this cell
            # to is original value so that we can backtrack and attempt to 
            # search along a different path.
            board[r][c] = saved_val

            return False

        # Search for the word from each cell on the board.
        for r in range(rows):
            for c in range(cols):
                if search(r, c, 0):
                    return True

        return False


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example1(self):
        board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
        word = "ABCCED"
        self.assertTrue(self.sol.exist(board, word))

    def test_example2(self):
        board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
        word = "SEE"
        self.assertTrue(self.sol.exist(board, word))

    def test_example3(self):
        board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
        word = "ABCB"
        self.assertFalse(self.sol.exist(board, word))

    def test_example4(self):
        board = [["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]]
        word = "ABCESEEEFS"
        self.assertTrue(self.sol.exist(board, word))


if __name__ == "__main__":
    unittest.main()
