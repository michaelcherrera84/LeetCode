#include <vector>
#include <queue>
#include <unordered_set>
#include <utility>

class Solution
{
public:
    /// @brief Return *the least number of dice rolls required to reach the
    /// square* `n²`. *If it is not possible to reach the square, return* `-1`.
    ///
    /// You are given an `n x n` integer matrix `board` where the cells are
    /// labeled from `1` to `n²` in a Boustrophedon style starting from the
    /// bottom left of the board (i.e. `board[n - 1][0]`) and alternating
    /// direction each row.
    ///
    /// You start on square `1` of the board. In each move, starting from
    /// square `curr`, do the following:
    ///
    /// - Choose a destination square `next` with a label in the range
    /// `[curr + 1, min(curr + 6, n2)]`.
    ///
    /// - This choice simulates the result of a standard **6-sided die roll**:
    ///   i.e., there are always at most 6 destinations, regardless of the size
    ///   of the board.
    ///
    /// - If `next` has a snake or ladder, you **must** move to the destination
    /// of that snake or ladder. Otherwise, you move to `next`.
    ///
    /// - The game ends when you reach the square `n²`.
    ///
    /// A board square on row `r` and column `c` has a snake or ladder if
    /// `board[r][c] != -1`. The destination of that snake or ladder is
    /// `board[r][c]`. Squares `1` and `n²` are not the starting points of any
    /// snake or ladder.
    ///
    /// Note that you only take a snake or ladder at most once per dice roll.
    /// If the destination to a snake or ladder is the start of another snake or
    /// ladder, you do **not** follow the subsequent snake or ladder.
    ///
    /// - For example, suppose the board is `[[-1,4],[-1,3]]`, and on the first
    /// move, your destination square is `2`. You follow the ladder to square
    /// `3`, but do not follow the subsequent ladder to `4`.
    ///
    /// @param board an `n x n` integer matrix where the cells are labeled from
    /// `1` to `n²`
    /// @return the least number of dice rolls required to reach the square `n²`
    int snakesAndLadders(std::vector<std::vector<int>> &board)
    {
        int n = board.size();
        // Queue of positions and the number of rolls it takes to get to get there.
        std::queue<std::pair<int, int>> queue;
        std::unordered_set<int> visited;

        queue.push({1, 0});
        visited.insert(1);

        // While there are still paths to consider...
        while (!queue.empty())
        {
            // Get the first position from the queue and the number of rolls
            // required to get to this position.
            auto [pos, rolls] = queue.front();
            queue.pop();

            // Consider each possible roll of a six-sided die.
            for (int i = 1; i <= 6; i++)
            {
                int next = pos + i;

                // If the roll puts us pas the end of the board, we are done.
                if (next > n * n)
                    break;

                auto [r, c] = getIndices(next, n);

                // If this position is a snake or ladder, follow it to its end.
                if (board[r][c] != -1)
                    next = board[r][c];

                // If we land on the final space, count this roll and return.
                if (next == n * n)
                    return rolls + 1;

                // If we have already visited this space, we know this track is
                // a cycle so we do not need to add this position to the queue
                // again. Otherwise, mark this position as "visited", and add it
                // to the queue to continue along this track.
                if (!visited.count(next))
                {
                    visited.insert(next);
                    queue.push({next, rolls + 1});
                }
            }
        }

        return -1;
    }

private:
    /// @brief Get the array indices of the integer position on the game board.
    /// @param pos a position on the game board
    /// @param n the size of the board
    /// @return the array indices of the integer position
    std::pair<int, int> getIndices(int pos, int n) const
    {
        int r = (pos - 1) / n;
        int c = (pos - 1) % n;

        int row = n - 1 - r;
        int col = r % 2 == 0 ? c : n - 1 - c;

        return {row, col};
    }
};