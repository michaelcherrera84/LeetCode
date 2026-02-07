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
 * Given the `root` of a binary tree, return *the average value on each level in
 * the form of an array*.
 * @param {TreeNode} root the root of a binary tree
 * @returns {number[]} the average value of the nodes on each level
 */
var averageOfLevels = function (root) {
    const counts = [];  // the number of nodes at each level of the tree
    const sums = [];    // the sum of the nodes at each level of the tree
    getCountsAndSums(root, 0, counts, sums);

    const averages = [];    // the averages of the nodes at each level
    for (let i = 0; i < counts.length; i++) {
        averages.push(sums[i] / counts[i]);
    }
    return averages;
};

/**
 * Get the number of nodes and the sum of the nodes for each level of the tree.
 * @param {TreeNode} node the current node of the tree
 * @param {number} level the current level of the tree
 * @param {number[]} counts the number of nodes at each level
 * @param {number[]} sums the sum of the nodes at each level
 */
const getCountsAndSums = function (node, level, counts, sums) {
    if (!node) return;

    // If the we have not previous visited this level of the tree, add new 
    // elements to the arrays to store the node count and sum.
    if (!counts[level]) {
        counts.push(0);
        sums.push(0);
    }

    counts[level] += 1;         // Increment the node count at this level by 1.
    sums[level] += node.val;    // Add the current value to the sum at this level.

    // Traverse the tree recursively keeping track of the level.
    getCountsAndSums(node.left, level + 1, counts, sums);
    getCountsAndSums(node.right, level + 1, counts, sums);
};

module.exports = { TreeNode, averageOfLevels };
