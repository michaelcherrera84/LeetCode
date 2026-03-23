/**
 * Definition for a binary tree node.
 */
function TreeNode(val, left, right) {
    this.val = val === undefined ? 0 : val;
    this.left = left === undefined ? null : left;
    this.right = right === undefined ? null : right;
}

/**
 * Given the `root` of a binary tree, *determine if it is a valid binary search
 * tree (BST)*.
 *
 * A **valid BST** is defined as follows:
 * - The left subtree of a node contains only nodes with keys **strictly less
 * than** the node's key.
 * - The right subtree of a node contains only nodes with keys **strictly
 * greater than** the node's key.
 * - Both the left and right subtrees must also be binary search trees.
 * @param {TreeNode} root the root of a binary tree
 * @return {boolean} `true` if the tree is valid or `false` otherwise
 */
var isValidBST = function (root) {
    /**
     * Validate each node of the tree recursively by comparing each node to its
     * minimum and maximum allowed values.
     * @param {TreeNode} node the current node being validated
     * @param {number} min the minimum valid value of the node
     * @param {number} max the maximum valid value of the node
     * @returns `true` if the node is valid or `false` otherwise
     */
    function validate(node, min, max) {
        if (!node) return true;
        if (node.val <= min || node.val >= max) return false;
        // The left node's value must be greater than the current minimum and
        // less than current node's value. The right node's value must be less
        // than the current maximum and greater than the current node's value.
        return validate(node.left, min, node.val) && validate(node.right, node.val, max);
    }

    // The root has no minimum or maximum value.
    return validate(root, -Infinity, Infinity);
};

module.exports = { TreeNode, isValidBST };
