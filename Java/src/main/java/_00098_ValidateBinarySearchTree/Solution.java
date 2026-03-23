package _00098_ValidateBinarySearchTree;

/**
 * Definition for a binary tree node.
 */
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode() {}

    TreeNode(int val) { this.val = val; }

    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

public class Solution {

    /**
     * Given the {@code root} of a binary tree, <i>determine if it is a valid binary
     * search tree (BST)</i>.
     * <p>
     * A <b>valid BST</b> is defined as follows:
     * 
     * <ul>
     * <li>The left subtree of a node contains only nodes with keys <b>strictly less
     * than</b> the node's key.</li>
     * <li>The right subtree of a node contains only nodes with keys <b>strictly
     * greater than</b> the node's key.</li>
     * <li>Both the left and right subtrees must also be binary search trees.</li>
     * 
     * @param root the root of a binary tree
     * @return {@code true} if the BST is valid, or {@code false} otherwise
     */
    public boolean isValidBST(TreeNode root) {

        TreeNode curr = root; // current node being validated
        TreeNode prev = null; // previous validated node

        // While there are nodes left to be validated, traverse the tree using a
        // Morris inorder traversal.
        while (curr != null) {
            // If there is a node to the left of the current node...
            if (curr.left == null) {
                // If we have already validated a node, then this node's value
                // should be greater than the previous node's value.
                if (prev != null && curr.val <= prev.val)
                    return false;
                // Otherwise, this node is valid. Set this node as the previous node.
                prev = curr;
                // Advance to right child (which may be a threaded link back to
                // and ancestor).
                curr = curr.right;
            } else {
                // The left node should be a predecessor to the current node.
                TreeNode pred = curr.left;

                // While predecessor has right nodes that are not the current node,
                // advance pred to the right.
                while (pred.right != null && pred.right != curr)
                    pred = pred.right;

                // If there is no right node, temporarily set the predecessor's
                // right node to the current node, which should be the next node
                // after this predecessor in order.
                if (pred.right == null) {
                    pred.right = curr;
                    curr = curr.left;
                } else {
                    // Otherwise, the right node is the current node. Now this
                    // predecessor's right node should be returned to its
                    // original value of `null`.
                    pred.right = null;
                    // The current node's value should be greater than the
                    // previous node's value.
                    if (prev != null && curr.val <= prev.val)
                        return false;
                    prev = curr;
                    curr = curr.right;
                }
            }
        }

        return true;
    }
}
