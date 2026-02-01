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
 * Given the `root` of a binary tree, invert the tree and return *its root*.
 * @param {TreeNode} root the root of a binary tree
 * @returns {TreeNode} the root of the inverted tree
 */
var invertTree = function (root) {
    // If root is null, we've reached the bottom of the tree, or there is no tree.
    if (root === null) return null;

    // Go left then right to the bottom of the tree.
    const left = invertTree(root.left);
    const right = invertTree(root.right);

    // Swap the left and right nodes coming back up the tree.
    root.left = right;
    root.right = left;

    return root;
};

module.exports = { TreeNode, invertTree };
