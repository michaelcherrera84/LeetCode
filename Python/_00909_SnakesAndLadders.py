from collections import deque
from typing import List


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        """
        You are given an `n x n` integer matrix `board` where the cells are
        labeled from `1` to `n²` in a Boustrophedon style starting from the
        bottom left of the board (i.e. `board[n - 1][0]`) and alternating
        direction each row.

        You start on square `1` of the board. In each move, starting from square
        `curr`, do the following:

        - Choose a destination square `next` with a label in the range
        `[curr + 1, min(curr + 6, n²)]`.

          - This choice simulates the result of a standard **6-sided die roll**:
          i.e., there are always at most 6 destinations, regardless of the size
          of the board.

        - If `next` has a snake or ladder, you **must** move to the destination
        of that snake or ladder. Otherwise, you move to `next`.

        - The game ends when you reach the square `n²`.

        A board square on row `r` and column `c` has a snake or ladder if
        `board[r][c] != -1`. The destination of that snake or ladder is
        `board[r][c]`. Squares `1` and `n²` are not the starting points of any
        snake or ladder.

        Note that you only take a snake or ladder at most once per dice roll. If
        the destination to a snake or ladder is the start of another snake or
        ladder, you do not follow the subsequent snake or ladder.

        - For example, suppose the board is `[[-1,4],[-1,3]]`, and on the first
        move, your destination square is `2`. You follow the ladder to square
        `3`, but do **not** follow the subsequent ladder to `4`.

        Return *the least number of dice rolls required to reach the square*
        `n2`. *If it is not possible to reach the square, return* `-1`.

        Args:
            board (List[List[int]]): the `n x n` integer matrix game board

        Returns:
            int: the least number of dice rolls required to reach the end of the
            board (square `n²`)
        """

        n = len(board)
        visited = set()
        queue = deque([(1, 0)])  # queue of squares along with the number of
                                 # rolls needed to reach the square

        def get_indices(pos: int) -> tuple[int, int]:
            """
            Get the row and column indices of a square based on its position.
            """
            row, col = divmod(pos - 1, n)
            return n - 1 - row, col if row % 2 == 0 else n - 1 - col

        while queue:
            # Get the current position and the number of rolls to get there.
            pos, rolls = queue.popleft()

            # Check the outcomes of all possible rolls of a six-sided die.
            for i in range(1, 7):
                # The next position is the current position plus the roll.
                next = pos + i 

                # The are no squares beyond the final square.
                if next > n**2:
                    continue

                r, c = get_indices(next)

                # If this square is a snake or ladder, follow it to its end. 
                if board[r][c] != -1:
                    next = board[r][c]

                # If we land on the final square, count this roll and return the
                # total number of rolls to get here.
                if next == n**2:
                    return rolls + 1

                # Otherwise,...

                # Count this roll and update the queue with the next position
                # and the number of rolls. Also add the position to the set of 
                # visited positions. If we land on this position again, we know
                # that this path is a cycle.
                if next not in visited:
                    visited.add(next)
                    queue.append((next, rolls + 1))

        # If we never landed on the final square then there is no path to the 
        # final square.
        return -1


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example1(self):
        board = [
            [-1, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1, -1],
            [-1, 35, -1, -1, 13, -1],
            [-1, -1, -1, -1, -1, -1],
            [-1, 15, -1, -1, -1, -1],
        ]
        self.assertEqual(4, self.sol.snakesAndLadders(board))

    def test_example2(self):
        board = [[-1, -1], [-1, 3]]
        self.assertEqual(1, self.sol.snakesAndLadders(board))

    def test_example3(self):
        board = [
            [-1, -1, 30, 14, 15, -1],  # 36 35 34 33 32 21
            [23, 9, -1, -1, -1, 9],  # 25 26 27 28 29 30
            [12, 5, 7, 24, -1, 30],  # 24 23 22 21 20 19
            [10, -1, -1, -1, 25, 17],  # 13 14 15 16 17 18
            [32, -1, 28, -1, -1, 32],  # 12 11 10  9  8  7
            [-1, -1, 23, -1, 13, 19],  #  1  2  3  4  5  6
        ]
        self.assertEqual(2, self.sol.snakesAndLadders(board))


if __name__ == "__main__":
    unittest.main()
