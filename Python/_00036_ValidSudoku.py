from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """Determine if a `9 x 9` Sudoku board is valid. Only the filled cells
        need to be validated **according to the following rules**:
        1. Each row must contain the digits `1-9` wihout repetition.
        2. Each column must contain the digits `1-9` without repetition.
        3. Each of the nine `3 x 3` sub-boxes of the grid must contain the
        digits `1-9` wihout repetition.

        **Note:**
        - A Sudoku board (partially filled) could be valid but is not
        necessarily solvable.
        - Only the filled cells need to be validated according to the mentioned
        rules.

        Args:
            board (List[List[str]]): the 9 x 9 Sudoku board

        Returns:
            bool: `true` if the partially filled board is valid, or `false`
            otherwise
        """

        # Check that each row is valid.
        for row in board:
            nums = {}
            for num in row:
                if num != ".":
                    if num in nums:
                        return False
                    nums[num] = True

        # Check that each column is valid.
        for i in range(9):
            nums = {}
            for j in range(9):
                num = board[j][i]
                if num != ".":
                    if num in nums:
                        return False
                    nums[num] = True

        # Check that each box is valid.
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                nums = {}
                for i in range(3):
                    for j in range(3):
                        num = board[row + i][col + j]
                        if num != ".":
                            if num in nums:
                                return False
                            nums[num] = True

        return True


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example1(self):
        board = [
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
        expected = True
        actual = self.sol.isValidSudoku(board)
        self.assertEqual(expected, actual)

    def test_example2(self):
        board = [
            ["8", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
        expected = False
        actual = self.sol.isValidSudoku(board)
        self.assertEqual(expected, actual)

    def test_last_box_invalid(self):
        board = [
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", "2", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
        expected = False
        actual = self.sol.isValidSudoku(board)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
