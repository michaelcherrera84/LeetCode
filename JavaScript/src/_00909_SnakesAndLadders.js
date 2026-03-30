/**
 * You are given an `n x n` integer matrix `board` where the cells are labeled
 * from `1` to `n²` in a Boustrophedon style starting from the bottom left of
 * the board (i.e. `board[n - 1][0]`) and alternating direction each row.
 *
 * You start on square `1` of the board. In each move, starting from square
 * `curr`, do the following:
 *
 * - Choose a destination square `next` with a label in the range
 * `[curr + 1, min(curr + 6, n2)]`.
 *   - This choice simulates the result of a standard **6-sided die roll**:
 * i.e., there are always at most 6 destinations, regardless of the size of the board.
 * - If `next` has a snake or ladder, you **must** move to the destination of
 * that snake or ladder. Otherwise, you move to `next`.
 * - The game ends when you reach the square `n²`.
 *
 * A board square on row `r` and column `c` has a snake or ladder if
 * `board[r][c] != -1`. The destination of that snake or ladder is `board[r][c]`.
 * Squares `1` and `n²` are not the starting points of any snake or ladder.
 *
 * Note that you only take a snake or ladder at most once per dice roll. If the
 * destination to a snake or ladder is the start of another snake or ladder, you
 * do not follow the subsequent snake or ladder.
 *
 * - For example, suppose the board is `[[-1,4],[-1,3]]`, and on the first move,
 * your destination square is `2`. You follow the ladder to square `3`, but do
 * **not** follow the subsequent ladder to `4`.
 *
 * Return *the least number of dice rolls required to reach the square* `n²`.
 * *If it is not possible to reach the square, return* `-1`.
 * @param {number[][]} board an `n x n` integer matrix where cells are labeled
 * from `1` to `n²`
 * @return {number} the least number of dice rools requeired to reach the square
 * `n²` of `-1` if it is not possible
 */
var snakesAndLadders = function (board) {
    const n = board.length;

    /** Queue of positions and the number of rolls it takes to get to get there. */
    const queue = [[1, 0]];
    const visited = new Set();

    /**
     * Get the array indices of the interger position on the game board.
     * @param {number} pos a position on the game board
     * @returns the array indices of the integer position
     */
    function getIndices(pos) {
        const row = Math.floor((pos - 1) / n);
        const col = (pos - 1) % n;

        return [n - 1 - row, row % 2 == 0 ? col : n - 1 - col];
    }

    // While there are still paths to consider...
    while (queue.length > 0) {
        // Get the first position from the queue and the number of rolls 
        // required to get there.
        const [pos, rolls] = queue.shift();

        // Consider each possible roll of a six-sided die.
        for (let i = 1; i < 7; i++) {
            let next = pos + i;

            // If the roll puts us past the end of the board, we are done after.
            if (next > n * n) break;

            let [r, c] = getIndices(next);

            // If this position is a snake or ladder, follow it to its end.
            if (board[r][c] !== -1) next = board[r][c];

            // If we land on the final space, count this roll and return.
            if (next === n * n) return rolls + 1;

            // If we have already visited this space, we know this track is a 
            // cycle so we do not need to add this position to the queue again.
            // Otherwise, mark this position as visited and add it to the queue
            // to continue along this track.
            if (!visited.has(next)) {
                visited.add(next);
                queue.push([next, rolls + 1]);
            }
        }
    }

    return -1;
};

module.exports = { snakesAndLadders };
