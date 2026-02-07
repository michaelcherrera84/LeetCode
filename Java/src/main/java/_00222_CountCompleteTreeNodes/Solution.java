package _00222_CountCompleteTreeNodes;

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
     * Given the {@code root} of a <b>complete</b> binary tree, return the
     * number of the nodes in the tree.
     * <p>
     * Every level, except possibly the last, is completely filled in a complete
     * binary tree, and all nodes in the last level are as far left as possible.
     * It can have between {@code 1} and {@code 2^h} nodes inclusive at the last
     * level {@code h}.
     *
     * @param root the root of a complete binary tree
     * @return the number of nodes in the tree
     */
    int countNodes(TreeNode root) {
        if (root == null) {
            return 0;
        }

        int left = 0;   // left depth of tree
        int right = 0;  // right depth of tree
        
        // Calculate the left depth of the tree.
        TreeNode temp = root;
        while (temp != null) {
            left++;
            temp = temp.left;
        }

        // Calculate the right depth of the tree.
        temp = root;
        while (temp != null) {
            right++;
            temp = temp.right;
        }

        // If the left depth and the right depth are the same, the tree is has 
        // 2^h - 1 nodes.
        if (left == right) {
            return (1 << left) - 1;
        }

        // Recursively count all nodes of the tree if the left and right depths
        // are not equal.
        return 1 + countNodes(root.left) + countNodes(root.right);
    }
}
