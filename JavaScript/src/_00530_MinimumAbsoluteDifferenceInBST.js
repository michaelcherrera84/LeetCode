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
 * Given the `root` of a Binary Search Tree (BST), return *the minimum absolute
 * difference between the values of any two different nodes in the tree.*
 * @param {TreeNode} root the root of a Binary Search Tree
 * @returns {number} the minimum absolute difference between the values of any
 * two different nodes
 */
var getMinimumDifference = function (root) {
    let prev = null;  // the value of the previous node
    let diff = Number.MAX_SAFE_INTEGER;

    // BST is an ordered tree, so the minimum absolute difference will always be
    // between a node and the one right before it in order.
    const traverse = (node) => {
        if (!node) return;

        // The lowest values will always be all the way to the left.
        traverse(node.left)

        // If this isn't the lowest value node...
        if (prev !== null) {
            // check if the difference between this node and the previous node
            // is less than the current difference.
            diff = Math.min(diff, node.val - prev);
        }

        // Set the new previous value, before moving to the next node.
        prev = node.val;

        // Now go right.
        traverse(node.right);
    }

    // Traverse the tree recusively and return the minimum difference.
    traverse(root);
    return diff;
};

module.exports = { TreeNode, getMinimumDifference };
