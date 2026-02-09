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
 * Given an integer array `nums` where the elements are sorted in **ascending
 * order*, convert *it to a height-balanced binary search tree*.
 * @param {number[]} nums the integer array
 * @returns {TreeNode} the root of the binary search tree
 */
var sortedArrayToBST = function (nums) {
    /**
     * Build the BST by repeatedly dividing the array using pointers. Use the
     * lower half of array for the left side of the tree, and the upper half of
     * the array for the right side of the tree.
     * @param {number} left first value of sub-array
     * @param {number} right last value of sub-array
     * @returns the Binary Search Tree
     */
    const buildTree = (left, right) => {
        // If left is greater than right, the sub-array has no values.
        if (left > right) return null;

        const mid = (left + right) >> 1; // middle value of sub-array.

        // Assign the middle value of the sub-array to this node.
        const node = new TreeNode(nums[mid]);

        // Pass the lower half of the sub-array to build the left side of the sub-tree.
        node.left = buildTree(left, mid - 1);
        // Pass the upper half of the sub-array to build the right side of the sub-tree.
        node.right = buildTree(mid + 1, right);

        return node;
    };

    // Build the BST.
    return buildTree(0, nums.length - 1);
};

module.exports = { TreeNode, sortedArrayToBST };
