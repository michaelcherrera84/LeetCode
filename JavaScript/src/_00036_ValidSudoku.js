/**
 * Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be
 * validated according to the following rules:
 * 1. Each row must contain the digits 1-9 without repetition.
 * 2. Each column must contain the digits 1-9 without repetition.
 * 3. Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9
 * without repetition.
 *
 * **Note:**
 * - A Sudoku board (partially filled) could be valid but is not necessarily
 * solvable.
 * - Only the filled cells need to be validated according to the
 * mentioned rules.
 * @param {character[][]} board the Sudoku board
 * @return {boolean} `true` if the board is valid
 */
var isValidSudoku = function (board) {
    const rows = Array.from({ length: 9 }, () => new Set());
    const cols = Array.from({ length: 9 }, () => new Set());
    const boxes = Array.from({ length: 9 }, () => new Set());

    // For each row `i`,...
    for (let i = 0; i < 9; i++) {
        // ror each column `j`,...
        for (let j = 0; j < 9; j++) {
            // and for or each box `k`...
            const k = ((i / 3) | 0) * 3 + ((j / 3) | 0);
            const num = board[i][j]; // the current num from the board

            // If the current "number" is not `.`, check to see if this num has
            // been seen in this row, column, or box already. If so, the board
            // is invalid. Otherwise, add this num to the set of nums for this
            // row, column, and box.
            if (num !== ".") {
                if (rows[i].has(num) || cols[j].has(num) || boxes[k].has(num)) return false;

                rows[i].add(num);
                cols[j].add(num);
                boxes[k].add(num);
            }
        }
    }

    return true;
};

module.exports = isValidSudoku;
