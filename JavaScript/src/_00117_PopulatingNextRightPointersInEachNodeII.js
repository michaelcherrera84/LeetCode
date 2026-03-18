/**
 * Definition for a _Node.
 */
function _Node(val, left, right, next) {
    this.val = val === undefined ? null : val;
    this.left = left === undefined ? null : left;
    this.right = right === undefined ? null : right;
    this.next = next === undefined ? null : next;
}

/**
 * Given a binary tree
 * ```C++
 *   struct Node {
 *       int val;
 *       Node *left;
 *       Node *right;
 *       Node *next;
 *   }
 * ```
 * Populate each next pointer to its next right node. If there is no next right
 * node, the next pointer should be set to `NULL`.
 * @param {_Node} root the root of the binary tree
 * @return {_Node} the root of the binary tree with `next` values set
 */
var connect = function (root) {
    if (!root) return root;

    let curr = root;
    let dummy = new _Node(); // dummy head that sits before the next level
    let next_level = dummy; // traverses the next level

    while (curr) {
        // Connect the left node to the node to its left. If the left node is
        // the beginning of a level, `dummy` and `next_level` will be the same.
        // Pointing `next_level.next` to the left node will set `dummy` before 
        // the next level.
        if (curr.left) {
            next_level.next = curr.left;
            next_level = next_level.next;
        }
        // Connect the right node to the node to its left.
        if (curr.right) {
            next_level.next = curr.right;
            next_level = next_level.next;
        }
        // Advance the current node to the node to its right.
        if (curr.next) {
            curr = curr.next;
        } else {
            // Move `curr` to the next level.
            curr = dummy.next;
            // Dummy will be set to the next level in the next iteration if
            // there is a next iteration. Otherwise, it will still stay null,
            // which is necessary to terminate the loop (curr = dummy.next).
            dummy.next = null;
            next_level = dummy;
        }
    }

    return root;
};

module.exports = { _Node, connect };
