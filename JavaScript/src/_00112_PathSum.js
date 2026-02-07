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
 * Given the `root` of a binary tree and an integer `targetSum`, return `true`
 * if the tree has a **root-to-leaf** path such that adding up all the values
 * along the path equals `targetSum`.
 *
 * A **leaf** is a node with no children.
 * @param {TreeNode} root the root of the binary tree
 * @param {number} targetSum the target sum for which to search
 * @returns {boolean} `true` if the tree has a root-to-leaf path such that
 * adding up all the values along the path equals `targetSum`, or `false`
 * otherwise
 */
var hasPathSum = function (root, targetSum) {
    // Search for the target sum.
    return search(root, targetSum, 0);
};

/**
 * Traverses the paths of the trees returning the `true` once a path is found
 * such that the values sum equals the target sum, or `false` is no such path is
 * found.
 * @param {TreeNode} node the current node of the tree
 * @param {number} targetSum the sum for which we are searching
 * @param {number} currentSum the sum of the values in the path to this point
 * @returns {boolean} `true` if a path is found such that the values sum is
 * equal to the target sum, or `false` otherwise.
 */
var search = function (node, targetSum, currentSum) {
    // If the current node is null, then the parent was not a leaf.
    if (!node) return false;
    // If the left and right nodes are null, the current node is a leaf.
    if (!node.left && !node.right) {
        // If the current sum + the value of this node is equal to the target
        // sum, the target sum has been found. Otherwise the targer sum is not 
        // found.
        if (currentSum + node.val === targetSum) return true;
        else return false;
    }

    // Traverse the tree recusively and return true if the target sum is found
    // at the leaf of any path.
    return search(node.left, targetSum, currentSum + node.val) || search(node.right, targetSum, currentSum + node.val);
};

module.exports = { TreeNode, hasPathSum };
