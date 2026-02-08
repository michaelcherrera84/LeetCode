package _00530_MinimumAbsoluteDifferenceInBST;

/**
 * Definition for a binary tree node.
 */
@SuppressWarnings("unused")
class TreeNode {

    int val;
    TreeNode left;
    TreeNode right;

    TreeNode() {
    }

    TreeNode(int val) {
        this.val = val;
    }

    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

public class Solution {

    /**
     * The value of the previous node
     */
    private Integer prev;
    /**
     * The minimum difference between any two nodes
     */
    private int diff;

    /**
     * Given the {@code root} of a Binary Search Tree (BST), return <i>the
     * minimum absolute difference between the values of any two different nodes
     * in the tree</i>.
     *
     * @param root the root of a Binary Search Tree
     * @return the minimum absolute difference between the values of any two
     * nodes in the tree
     */
    int getMinimumDifference(TreeNode root) {
        diff = Integer.MAX_VALUE;

        // Traverse the tree recursively to find the minimum difference.
        traverse(root);

        return diff;
    }

    /**
     * Traverse the tree recursively to find the minimum difference.
     * <p>
     * Since a Binary Search Tree is an ordered tree, the minimum difference
     * will always be between a node and the node immediately preceding it.
     * Traverse the tree in order, and get the difference between each node and
     * the previos node. If the difference is smaller than the current minimum
     * difference, set the minimum difference to this differnece.
     *
     * @param node the current node
     */
    private void traverse(TreeNode node) {
        if (node == null) {
            return;
        }
        // Go left until null to find the smallest value.
        traverse(node.left);

        // If this node is the smallest of the full BST, then get the difference 
        // between this node and the previous node.
        if (prev != null) {
            diff = Math.min(diff, node.val - prev);
        }

        // Set the previous node to this node before moving to the next node.
        prev = node.val;

        traverse(node.right);
    }
}
