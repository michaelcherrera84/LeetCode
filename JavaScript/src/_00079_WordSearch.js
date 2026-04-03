/**
 * Given an `m x n` grid of characters `board` and a string `word`, return `true`
 * *if* `word` *exists in the grid*.
 *
 * The word can be constructed from letters of sequentially adjacent cells,
 * where adjacent cells are horizontally or vertically neighboring. The same
 * letter cell may not be used more than once.
 *
 * @param {character[][]} board an `m x n` grid of characters
 * @param {string} word the word to search for on the board
 * @return {boolean} `true` if the word is found or `false` otherwise
 */
var exist = function (board, word) {
    const rows = board.length;
    const cols = board[0].length;
    // directions [row, col] to move from a current cell
    const directions = [
        [1, 0],
        [-1, 0],
        [0, 1],
        [0, -1],
    ];
    const visited = Array.from({ length: rows }, () => new Array(cols).fill(false));

    /**
     * Search the board for connected letters that form the desired word.
     *
     * @param {number} r current row of board
     * @param {number} c current col of board
     * @param {number} i current letter of word expected
     * @returns `true` if all letters are found or `false` otherwise
     */
    function search(r, c, i) {
        // All letters are found if `i` is equal to the word length.
        if (i == word.length) return true;
        if (r < 0 || r >= rows || c < 0 || c >= cols) return false;
        if (visited[r][c] || board[r][c] != word[i]) return false;

        // Add this cell to visited so we don't try to use it again.
        visited[r][c] = true;

        // Move in each direction recusively to search for the rest of the letters.
        for ([dr, dc] of directions) {
            if (search(r + dr, c + dc, i + 1)) return true;
        }

        // If none of searches find the next letter, remove this cell from the
        // visited set so that we can backtrack and search along a different path.
        visited[r][c] = false;

        return false;
    }

    // Begin searching for the word from each cell.
    for (let r = 0; r < rows; r++) {
        for (let c = 0; c < cols; c++) {
            if (search(r, c, 0)) return true;
        }
    }

    return false;
};

module.exports = exist;
