/** Definition for a QuadTree node. */
function _Node(val, isLeaf, topLeft, topRight, bottomLeft, bottomRight) {
    this.val = val;
    this.isLeaf = isLeaf;
    this.topLeft = topLeft;
    this.topRight = topRight;
    this.bottomLeft = bottomLeft;
    this.bottomRight = bottomRight;
}

/**
 * Given a `n * n` matrix `grid` of `0's` and `1's` only. We want to represent
 * `grid` with a Quad-Tree.
 *
 * Return *the root of the Quad-Tree representing* `grid`.
 *
 * A Quad-Tree is a tree data structure in which each internal node has exactly
 * four children. Besides, each node has two attributes:
 * - `val`: True if the node represents a grid of 1's or False if the node
 * represents a grid of 0's. Notice that you can assign the `val` to True or
 * False when `isLeaf` is False, and both are accepted in the answer.
 * - `isLeaf`: True if the node is a leaf node on the tree or False if the node
 * has four children.
 * ```
 * class Node {
 *     public boolean val;
 *     public boolean isLeaf;
 *     public Node topLeft;
 *     public Node topRight;
 *     public Node bottomLeft;
 *     public Node bottomRight;
 * }
 * ```
 * We can construct a Quad-Tree from a two-dimensional area using the following
 * steps:
 * 1. If the current grid has the same value (i.e all `1's` or all `0's`) set
 * `isLeaf` True and set `val` to the value of the grid and set the four
 * children to Null and stop.
 * 2. If the current grid has different values, set `isLeaf` to False and set
 * `val` to any value and divide the current grid into four sub-grids as shown
 * in the photo.
 * 3. Recurse for each of the children with the proper sub-grid.
 *
 * @param {number[][]} grid the from which to build the quad-tree
 * @return {_Node} the root of the quad-tree
 */
var construct = function (grid) {
    /**
     * Return `true` if this grid represents a single `_Node` by check if all
     * values are the same.
     *
     * @param {number} i the first row of a grid
     * @param {number} j the first column of a grid
     * @param {number} len the height and width of a grid
     * @returns `true` if the grid represents a single `_Node` or `false`
     * otherwise
     */
    function isOneNode(i, j, len) {
        for (let r = i; r < i + len; r++) {
            for (let c = j; c < j + len; c++) {
                if (grid[r][c] !== grid[i][j]) return false;
            }
        }

        return true;
    }

    /**
     * Build a tree by recursively scanning the grid searching for sub-grids.
     *
     * @param {number} i the first row of a grid
     * @param {number} j the first column of a grid
     * @param {number} len the height and width of a grid
     * @returns a node of the tree
     */
    function buildTree(i, j, len) {
        if (isOneNode(i, j, len)) {
            return new _Node(grid[i][j], 1, null, null, null, null);
        }

        const node = new _Node(
            1,
            0,
            buildTree(i, j, len >> 1),
            buildTree(i, j + (len >> 1), len >> 1),
            buildTree(i + (len >> 1), j, len >> 1),
            buildTree(i + (len >> 1), j + (len >> 1), len >> 1),
        );

        return node;
    }

    return buildTree(0, 0, grid.length);
};

module.exports = { _Node, construct };
