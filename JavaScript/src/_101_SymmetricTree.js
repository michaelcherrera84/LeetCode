/**
 * Definition for a binary tree node.
 * @param {number} val the value of the node
 * @param {TreeNode} left the left branch
 * @param {TreeNode} right the right branch
 */
function TreeNode(val, left, right) {
    this.val = val === undefined ? 0 : val;
    this.left = left === undefined ? null : left;
    this.right = right === undefined ? null : right;
}

/**
 * Given the `root` of a binary tree, *check whether it is a mirror of itself*
 * (i.e., symmetric around its center).
 * @param {TreeNode} root the root of the binary tree
 * @returns {boolean} `true` if the sides of the tree are mirrored, or `false`
 * otherwise
 */
var isSymmetric = function (root) {
    // Compare both sides of the tree to see if they are mirrored.
    return compare(root.left, root.right);
};

/**
 * Given the roots of two binary tree `p` and `q`, check if they are mirrored.
 * @param {TreeNode} p root of first binary tree
 * @param {TreeNode} q root of second binary tree
 * @returns {boolean} `true` if the trees are mirrored, or `false` otherwise
 */
var compare = function (p, q) {
    if (p == null && q == null) return true;
    // If one node is null and the other isn't, the trees are not structurally mirrored.
    if (p == null || q == null) return false;
    // if the values aren't equal, the trees are not mirrored.
    if (p.val !== q.val) return false;

    // Traverse the opposite sides of each tree recursively and check if each
    // node is the same.
    return compare(p.left, q.right) && compare(p.right, q.left);
};

module.exports = { TreeNode, isSymmetric };
