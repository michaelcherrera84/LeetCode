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
 * Given the `root` of a **complete** binary tree, return the number of the
 * nodes in the tree.
 *
 * Every level, except possibly the last, is completely filled in a complete
 * binary tree, and all nodes in the last level are as far left as possible. It
 * can have between `1` and `2^h` nodes inclusive at the last level `h`.
 * @param {TreeNode} root the root of the complete binary tree
 * @returns {number} the number of nodes in the tree
 */
var countNodes = function (root) {
    if (root == null) return 0;
    
    let leftHeight = 1;     // the height of the left side of the tree.
    let rightHeight = 1;    // the height of the right side of the tree.

    // Calculate the height of the left side of the tree.
    let temp = root;
    while (temp.left) {
        temp = temp.left;
        leftHeight++;
    }
    // Caluculate the height of the right side of the tree.
    temp = root;
    while (temp.right) {
        temp = temp.right;
        rightHeight++;
    }

    // If the tree shape is symetrical the number of nodes is 2^height - 1.
    if (leftHeight === rightHeight) return (1 << leftHeight) - 1;

    // Otherwise, continue to the next subtree.
    return 1 + countNodes(root.left) + countNodes(root.right);
};

module.exports = { TreeNode, countNodes };
